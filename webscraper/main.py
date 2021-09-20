import os
import datetime as dt

from pmaw import PushshiftAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Comment, Base

engine = create_engine("sqlite:///comment.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

subreddit = "Liberal"  # os.environ["SUBREDDIT"]
limit = 250_000  # int(os.environ["LIMIT"])

api = PushshiftAPI()

start_epoch = int(dt.datetime(2015, 1, 1).timestamp())

results = list(
    api.search_comments(
        after=start_epoch,
        subreddit=subreddit,
        filter=["subreddit", "body", "created_utc"],
        limit=limit,
        mem_safe=True,
        nest_level=3,
    )
)

for comment in results:
    new_comment = Comment(
        created_utc=int(comment["created_utc"]),
        subreddit=comment["subreddit"],
        body=comment["body"],
    )
    session.add(new_comment)

session.commit()
