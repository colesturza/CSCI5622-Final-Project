from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Comment(Base):
    __tablename__ = "comment"
    comment_id = Column(Integer, primary_key=True)
    created_utc = Column(Integer, nullable=False)
    subreddit = Column(String, nullable=False)
    body = Column(String, nullable=False)
    score = Column(Integer, nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine("sqlite:///data/raw/comment.db")

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
