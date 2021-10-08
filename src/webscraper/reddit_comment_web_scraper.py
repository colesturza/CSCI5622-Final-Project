import os
import datetime as dt

from typing import Tuple


import praw

from pmaw import PushshiftAPI
from dotenv import load_dotenv, find_dotenv


class RedditCommentWebScraper:
    def __init__(
        self,
        subreddit: str = "politics",
        limit: int = 100,
        start_epoch: Tuple[int, int, int] = (2015, 1, 1)
    ):
        """
        Initializes a RedditCommentWebScrapper object.

        :param subreddit: the subreddit to scrape
        :param limit: the upper bound on comments to scrape
        :param start_epoch: the earliest post time to scrape from
            formatted as a tuple (year , month, day)
        :raises ValueError if limit < 1
        """
        self._subreddit = subreddit

        if limit < 1:
            raise ValueError("limit must be strictly positive")

        self._limit = limit
        self._start_epoch = int(dt.datetime(*start_epoch).timestamp())

        # find .env automagically by walking up directories until it's found
        dotenv_path = find_dotenv()

        # load up the entries as environment variables
        load_dotenv(dotenv_path)

        client_id = os.environ.get("praw_client_id")
        client_secret = os.environ.get("praw_client_secret")
        redirect_uri = os.environ.get("praw_redirect_uri")
        user_agent = os.environ.get("praw_user_agent")
        refresh_token = os.environ.get("praw_refresh_token")

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            user_agent=user_agent,
            refresh_token=refresh_token,
        )
        self._api = PushshiftAPI(praw=reddit)

        self._comments = []

    def scrape(self) -> None:
        """
        Scrapes comments from reddit and stores them.

        :return: None
        """

        def fxn(item):
            return (
                item["score"] > 1
                and item["body"] != "[removed]"
                and item["body"] != "[deleted]"
                and len(item["body"]) > 25
            )

        self._comments = list(
            self._api.search_comments(
                after=self._start_epoch,
                subreddit=self._subreddit,
                filter=["subreddit", "body", "created_utc", "score"],
                filter_fn=fxn,
                limit=self._limit,
                mem_safe=True
            )
        )

    def get_comments(self) -> dict:
        """
        Yields each of the scraped comments.

        The keys of the returned dictionary are {subreddit, body, created_utc}.

        :return: a dictionary representing a comment
        """
        for comment in self._comments:
            yield comment

    def get_subreddit(self) -> str:
        return self._subreddit

    def set_subreddit(self, subreddit: str) -> None:
        self._subreddit = subreddit

    def get_limit(self) -> int:
        return self._limit

    def set_limit(self, limit: int) -> None:
        if limit < 1:
            raise ValueError("limit must be strictly positive")

        self._limit = limit

    def get_start_epoch(self) -> int:
        return self._start_epoch

    def set_start_epoch(self, start_epoch: Tuple[int, int, int]) -> None:
        self._start_epoch = int(dt.datetime(*start_epoch).timestamp())
