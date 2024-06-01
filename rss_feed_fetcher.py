import feedparser
from article import Article
import certifi
import ssl
import requests
from logger_config import logger

class RSSFeedFetcher:
    def __init__(self , url) -> None:
        self.url  = url
        ##self.articles = []

    def fetch_articles(self):
        logger.info("Fetching the articles from the RSS feed")
        try:
            #ssl_context = ssl.create_default_context(cafile=certifi.where())
            response = requests.get(self.url)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
            articles = []
            if feed.bozo:
                raise ValueError(f"Error parsin feed : {feed.bozo_exception}")
            for entry in feed.entries:
                # article = Article(
                #     title = entry.title,
                #     link = entry.link,
                #     summary = entry.summary
                # )
                article = {
                    'title' : entry.title,
                    'link' : entry.link,
                    'summary':entry.summary
                }
                articles.append(article)
        except Exception as e:
            print(f"An error occurred while fetching articles : {e}")
            raise RuntimeError("An Error occured while fetching articles from Feed : " , e )
            
        #logger.info("Feteched Articles : " , articles)
        return articles
    
#    def get_articles(self):
#        return self.articles