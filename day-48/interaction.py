from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

form_fname = driver.find_element(By.NAME, "fName")
form_lname = driver.find_element(By.NAME, "lName")
form_email = driver.find_element(By.NAME, "email")
form_btn = driver.find_element(By.TAG_NAME, "button")

form_fname.send_keys("Kyle")
form_lname.send_keys("Will")
form_email.send_keys("email@example.com")
form_btn.send_keys(Keys.ENTER)



# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count_el = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count_el.text)

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

