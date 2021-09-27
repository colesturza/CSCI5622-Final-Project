from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Comment

engine = create_engine("sqlite:///data/database/comment.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# make this a class

for comment in Comment.query().all():

    pass

