import smtplib, random
import datetime as dt

MY_EMAIL = "kw2120713@gmail.com"
PASSWORD = "gulbouqazahmhhjs"

now = dt.datetime.now()
if now.weekday() == 5:

    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()

    todays_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="kw2120713@yahoo.com",
                            msg=f"Subject:Today's Motivational Quote\n\n{todays_quote}")


