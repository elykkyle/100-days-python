import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
import time

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"


def pos_or_neg(diff):
    if diff > 0:
        return "🔺"
    else:
        return "🔻"

# Get stock price at closing for yesterday and day before yesterday. Calculate the % difference.
def get_stock_change(stock_ticker):

    stock_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock_ticker,
        "outputsize": "compact",
        "apikey": stock_api_key
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=params)
    data = stock_response.json()
    data_to_list = [(k, v) for (k, v) in data["Time Series (Daily)"].items()]
    prev_two_days = data_to_list[:2]
    yesterday_close = float(prev_two_days[0][1]["4. close"])
    day_before_yesterday_close = float(prev_two_days[1][1]["4. close"])
    difference = yesterday_close - day_before_yesterday_close
    indicator = pos_or_neg(difference)
    percent_change = round(abs((difference / day_before_yesterday_close) * 100), 2)
    return indicator, percent_change


def get_news(company_name: str, num_articles: int):

    params = {
        "apiKey": os.environ.get("NEWSAPI_API_KEY"),
        "pageSize": num_articles,
        "sortBy": "relevancy",
        "language": "en",
        "qInTitle": company_name
    }

    response = requests.get(NEWS_ENDPOINT, params=params)
    articles = response.json()["articles"]
    return articles


def send_message(stock, indicator, percent_change, articles):

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    notify_phone = os.environ.get("MY_PHONE_NUMBER")
    client = Client(account_sid, auth_token)
    formatted_articles = [f"{stock}: {indicator} {percent_change}\nHeadline: {article['title']}\nBrief: {article['description']}" for article in articles]
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=os.environ.get('TWILIO_PHONE_NUMBER'),
            to=notify_phone
        )
        print(message.sid)


stock_change = get_stock_change(STOCK)
if stock_change[1] >= 5:
    news_articles = get_news(COMPANY_NAME, 3)
    send_message(stock=STOCK, indicator=stock_change[0], percent_change=stock_change[1], articles=news_articles)
