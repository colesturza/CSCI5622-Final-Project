from psaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()

start_epoch = int(dt.datetime(2017, 1, 1).timestamp())

results = list(api.search_comments(q="Trump",
                                   after=start_epoch,
                                   subreddit='Communism',
                                   limit=10))

print(results[0].body)
