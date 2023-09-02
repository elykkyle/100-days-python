import os
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()

EMAIL_ACCOUNT = os.environ.get("EMAIL_ACCOUNT")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:
    def __init__(self, user_email):
        self.user_email = user_email

    def notify(self, item_name, target_price, current_price):
        message = f"Subject: Amazon Price Alert!\n\n{item_name} is ${current_price}".encode("utf-8")

        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ACCOUNT, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=EMAIL_ACCOUNT, to_addrs=self.user_email, msg=message)
