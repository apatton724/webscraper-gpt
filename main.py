import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# URL of the forex news page
url = "https://www.fxstreet.com/currencies/eurusd"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the elements containing the news articles
    news_articles = soup.find_all("div", class_="your-new-class-name")

    # Iterate through the articles and perform sentiment analysis
    for article in news_articles:
        # Extract the text content of the article
        article_text = article.text.strip()  # Use .strip() to remove leading/trailing whitespace
        
        # Create a TextBlob object for sentiment analysis
        blob = TextBlob(article_text)
        
        # Calculate sentiment polarity (-1 to 1, where -1 is negative, 1 is positive)
        sentiment_polarity = blob.sentiment.polarity
        
        # Determine sentiment based on polarity
        if sentiment_polarity > 0:
            sentiment = "Positive"
        elif sentiment_polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Print sentiment analysis results for each article
        print("Article:")
        print(article_text)
        print(f"Sentiment: {sentiment}")
        print(f"Sentiment Polarity: {sentiment_polarity}")
        print("-" * 50)
else:
    print("Failed to retrieve the web page.")
