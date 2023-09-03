from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_el = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count = article_count_el.text

print(article_count)