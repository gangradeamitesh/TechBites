from rss_feed_fetcher import RSSFeedFetcher

if __name__ == "__main__":
    techcrunch_fetcher = RSSFeedFetcher('https://techcrunch.com/feed/')
    techcrunch_fetcher.fetch_articles()
    articles = techcrunch_fetcher.get_articles()

    for article in articles:
        print(article)