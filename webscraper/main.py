import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webscraper.models import Comment, Base
from webscraper.reddit_comment_web_scraper import RedditCommentWebScraper

engine = create_engine("sqlite:///comment.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main(subreddit, limit):
    subreddit = subreddit
    limit = limit
    start_epoch = (2015, 1, 1)

    comment_scraper = RedditCommentWebScraper(subreddit, limit, start_epoch)
    comment_scraper.scrape()

    for comment in comment_scraper.get_comments():
        new_comment = Comment(
            created_utc=int(comment["created_utc"]),
            subreddit=comment["subreddit"],
            body=comment["body"],
        )
        session.add(new_comment)

    session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--subreddit", metavar="path", required=True, help="the subreddit to scrape"
    )
    parser.add_argument(
        "--limit",
        metavar="path",
        required=True,
        help="the upper bound on comments to scrape",
    )
    args = parser.parse_args()

    main(subreddit=args.subreddit, limit=args.limit)
