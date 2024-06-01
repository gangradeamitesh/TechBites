from flask import Flask , jsonify ,request
from rss_feed_fetcher import RSSFeedFetcher
import json
from twitter_client import TwitterClient
from logger_config import logger

app = Flask(__name__)

with open('config.json', 'r') as file:
    config = json.load(file)

CONSUMER_KEY = config.get('TECHBITES_CONSUMER_KEY')
CONSUMER_KEY_SECRET = config.get('TECHBITES_CONSUMER_SECRET_KEY')
ACCESS_TOKEN = config.get('TECHBITES_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config.get('TECHBITES_ACCESS_TOKEN_SECRET')
BEARER = config.get('BEARER')


if not all ([CONSUMER_KEY, CONSUMER_KEY_SECRET , ACCESS_TOKEN , ACCESS_TOKEN_SECRET]):
    raise ValueError("Twitter API credentials are not set in the env!!")

twitter_client = TwitterClient(CONSUMER_KEY , CONSUMER_KEY_SECRET , ACCESS_TOKEN , ACCESS_TOKEN_SECRET , BEARER)


# @app.route('/fetch_feed', methods = ['GET'])
# def fetch_feed():
#     url = request.args.get('url')
#     if not url:
#         return jsonify({'error':'URL parameter is required'})
#     fetcher = RSSFeedFetcher(url)
#     fetcher.fetch_articles()
#     articles = [article.to_dict() for article in fetcher.get_articles()]
#     return jsonify({'articles':articles})

@app.route("/call_back", methods = ['GET'])
def callback():
    return jsonify("Hello World")

@app.route('/post_feed', methods=['POST'])
def fetch_feed():
    logger.info("/post_feed end point called!")
    techcrunch_feed_url = 'https://techcrunch.com/feed/'
    feed_fetcher = RSSFeedFetcher(techcrunch_feed_url)
    articles = feed_fetcher.fetch_articles()

    for article in articles:
        if not twitter_client.post_to_twitter(article):
            return jsonify({'error':'Failed to post '+article['title']+' to twitter'})
        
    return jsonify({'articles':articles})


if __name__=='__main__':
    app.run(debug=True)