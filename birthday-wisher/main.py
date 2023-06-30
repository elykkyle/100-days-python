import smtplib, random, pandas
import datetime as dt

MY_EMAIL = "kw2120713@gmail.com"
PASSWORD = "gulbouqazahmhhjs"

# get today
now = dt.datetime.now()
# create tuple of today's month and dae
today = (now.month, now.day)

# import birthdays and convert to dictionary
# set tuple of month and day as key.
birthdays_df = pandas.read_csv("birthdays.csv")
# Use dictionary comprehension to convert to dataframe to dictionary.
birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays_df.iterrows()}


# check if there's any birthdays today.
if today in birthdays_dict:
    # Pick one of the letter templates
    letter_num = random.randint(1, 3)
    letter_template = f"letter_templates/letter_{letter_num}.txt"
    # Extract the name from the data record
    name = birthdays_dict[today]["name"]
    # Get the contents from the letter template and replace NAME placeholder with name.
    with open(letter_template) as letter_file:
        contents = letter_file.read()
        final_letter = contents.replace("[NAME]", name)

# Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="kw2120713@yahoo.com",
                            msg=f"Subject:Happy Birthday, {name}!\r\n{final_letter}")
