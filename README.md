# Political News Sentiment Analyzer 📰🔍
Analyze the sentiment of political news articles by processing RSS feeds with this Python-based tool.
## Features
- RSS Feed Parsing: Extracts news articles from a given Google RSS feed.
- Sentiment Analysis: Uses NLP techniques to generate sentiment scores for each article.
- Simple Output: Prints the first article with its sentiment directly to the console.
## Setup and Usage
1. Clone the Repository:
```
git clone https://github.com/krishcpatel/political-news-sentiment.git
cd political-news-sentiment
```
3. Install Dependencies: Ensure you have Python 3.x installed. If necessary, install required libraries:
```
pip install -r requirements.txt
```
5. Modify RSS Feed URL: In main.py, update the RSS feed URL to your desired Google News RSS.
6. Run the Script: Execute the program:
```
python main.py
```
It will display the sentiment of the first article from the RSS feed.
## File Overview
- **Model.py**: Contains the logic for sentiment analysis.
- **Parse.py**: Handles RSS feed parsing.
- **main.py**: Orchestrates the entire process.
