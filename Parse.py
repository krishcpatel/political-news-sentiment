import feedparser
from newspaper import Article
import requests
import nltk

nltk.download('punkt')

def parseFeed(url: str):
    news_feed = feedparser.parse(url)
    return news_feed

def downloadArticle(url: str):
    try:
        response = requests.get(url, allow_redirects=True)
        article = Article(response.url)
        article.download()
        article.parse()
        article.nlp()
        return article
    except Exception as error:
        print("An exception occurred when downloading:", error)
        return None
