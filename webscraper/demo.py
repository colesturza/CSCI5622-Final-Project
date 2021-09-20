from pmaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()

start_epoch = int(dt.datetime(2015, 1, 1).timestamp())

results = list(
    api.search_comments(
        after=start_epoch,
        subreddit="Communism",
        filter=["subreddit", "body", "author_created_utc"],
        limit=10,
        mem_safe=True,
        nest_level=3,
    )
)

print(results)
