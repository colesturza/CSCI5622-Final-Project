import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Comment, Base
from reddit_comment_web_scraper import RedditCommentWebScraper

engine = create_engine("sqlite:///data/database/comment.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main(subreddit, limit, epoch="2007-1-1"):
    subreddit = subreddit
    limit = limit
    start_epoch = tuple(epoch.split("-")[:])

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
    parser.add_argument(
        "--epoch",
        metavar="path",
        required=False,
        help="the date to start collecting comments from",
    )
    args = parser.parse_args()

    main(subreddit=args.subreddit, limit=int(args.limit))
