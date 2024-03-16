import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_twitter():
    # Scrapes Twitter for tweets mentioning RIL
    twitter_url = "https://twitter.com/search?q=RIL%20since%3A" + (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    response = requests.get(twitter_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = soup.find_all('div', class_='tweet')
    twitter_data = []
    for tweet in tweets:
        tweet_text = tweet.find('div', class_='tweet-text').get_text()
        twitter_data.append({'source': twitter_url, 'text': tweet_text})
    return twitter_data

def scrape_news_websites():
    # Scrapes news websites for articles mentioning RIL
    news_sources = [
        "https://www.moneycontrol.com/news/tags/reliance-industries.html",
        "https://www.livemint.com/topic/reliance-industries",
        # Add more news sources if needed
    ]
    news_data = []
    for source in news_sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('a', class_='headline')
        for article in articles:
            article_text = article.get_text()
            news_data.append({'source': source, 'text': article_text})
    return news_data

def scrape_ril_mentions():
    # Combines data from Twitter and news websites
    ril_data = []
    ril_data.extend(scrape_twitter())
    ril_data.extend(scrape_news_websites())
    return ril_data

# Example usage
if __name__ == "__main__":
    ril_mentions = scrape_ril_mentions()
    for mention in ril_mentions:
        print(mention)
