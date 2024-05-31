import feedparser
from article import Article
import certifi
import ssl
import requests

class RSSFeedFetcher:
    def __init__(self , url) -> None:
        self.url  = url
        self.articles = []

    def fetch_articles(self):
        try:
            #ssl_context = ssl.create_default_context(cafile=certifi.where())
            response = requests.get(self.url)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
            if feed.bozo:
                raise ValueError(f"Error parsin feed : {feed.bozo_exception}")
            for entry in feed.entries:
                article = Article(
                    title = entry.title,
                    link = entry.link,
                    summary = entry.summary
                )
                self.articles.append(article)
        except Exception as e:
            print(f"An error occurred while fetching articles : {e}")
    
    def get_articles(self):
        return self.articles