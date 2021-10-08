import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.data.models import Comment, Base
from reddit_comment_web_scraper import RedditCommentWebScraper

engine = create_engine("sqlite:///data/raw/comment.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main(subreddit, limit):
    subreddit = subreddit
    limit = limit
    start_epoch = (2007, 1, 1)

    comment_scraper = RedditCommentWebScraper(
        subreddit, limit, start_epoch
    )
    comment_scraper.scrape()

    for comment in comment_scraper.get_comments():
        new_comment = Comment(
            created_utc=int(comment["created_utc"]),
            subreddit=str(comment["subreddit"]),
            body=str(comment["body"]),
            score=int(comment["score"])
        )
        session.add(new_comment)

    session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--subreddit",
        metavar="path",
        required=True,
        help="the subreddit to scrape",
    )
    parser.add_argument(
        "-l",
        "--limit",
        metavar="path",
        required=True,
        help="the upper bound on comments to scrape",
    )
    args = parser.parse_args()

    main(subreddit=args.subreddit, limit=int(args.limit))
