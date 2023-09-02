import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os
import lxml

load_dotenv()
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL")

notifier = NotificationManager(NOTIFY_EMAIL)

headers = {
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': 'macOS'
}

product_url = "https://www.amazon.com/dp/B075CYMYK6?th=1"
target_price = 100
response = requests.get(product_url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
title_span = soup.find("span", id="productTitle")
item_name = title_span.getText().strip()

price_span = soup.find("span", class_="a-offscreen")
current_price = float(price_span.getText().split("$")[1])

if current_price <= target_price:
    notifier.notify(item_name=item_name, target_price=target_price, current_price=current_price)
