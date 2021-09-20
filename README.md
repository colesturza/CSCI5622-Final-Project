# CSCI5622-Final-Project
A machine learning model to predict the subreddit of users' comments.

**Team Members:** Cole Sturza, Alex Book, Will Mardick-Kanter 

## Resources

- [PSAW: Python Pushshift.io API Wrapper (for comment/submission search)](https://psaw.readthedocs.io/en/latest/)

## Running the Web Scraper

The web scraper can be run with the following command. The `--subreddit` flag can be changed to and 
subreddit of your choosing. The `--limit` flag is a limit on the number of comments to 
scrape. A SQLite database will be generated with the scraped comments.

```bash
$ python ./webscraper/main.py --subreddit Communism --limit 100
```
