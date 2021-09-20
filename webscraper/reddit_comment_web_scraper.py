import datetime as dt

from pmaw import PushshiftAPI
from typing import Tuple


class RedditCommentWebScraper:
    def __init__(
        self,
        subreddit: str = "politics",
        limit: int = 100,
        start_epoch: Tuple[int, int, int] = (2015, 1, 1),
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
        self._api = PushshiftAPI()

        self._comments = []

    def scrape(self) -> None:
        """
        Scrapes comments from reddit and stores them.

        :return: None
        """
        self._comments = list(
            self._api.search_comments(
                after=self._start_epoch,
                subreddit=self._subreddit,
                filter=["subreddit", "body", "created_utc"],
                limit=self._limit,
                mem_safe=True,
                nest_level=3,
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
