from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li a")
event_dict = {}

for i in range(len(event_dates)):
    event_dict[i] = {
        "date": event_dates[i].text,
        "name": event_names[i].text}

driver.quit()

print(event_dict)
