import tweepy
from bs4 import BeautifulSoup
from logger_config import logger


class TwitterClient:

    def __init__(self , consumer_key , consumer_secret , access_token, access_token_secret , bearer) -> None:
        # auth = tweepy.OAuth1UserHandler(
        # consumer_key, consumer_secret, access_token, access_token_secret)
        self.client = tweepy.Client(
            bearer_token = bearer,
            consumer_key = consumer_key,
            consumer_secret = consumer_secret,
            access_token = access_token,
            access_token_secret = access_token_secret
        )
        # self.twitter_api = tweepy.API(auth)
        

    def clean_text(self , text):
        soup = BeautifulSoup(text , 'html.parser')
        cleaned_text = soup.get_text(separator=' ', strip=True)
        return cleaned_text
    
    def post_to_twitter(self , article):
        logger.info("Posting the article to Twitter")
        summary = self.clean_text(article.get('summary', ''))
        link = article.get('link', '')
        tweet_content = f"{summary[:200]}... {link}"
       
        try:
            logger.info("Trying to tweet following : ")
            respone = self.client.create_tweet(text = tweet_content , user_auth = True)
        except Exception as e :
            raise RuntimeError(f"Error posting to Twitter : {e}")
        
