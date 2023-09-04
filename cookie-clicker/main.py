import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.implicitly_wait(0.5)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(0.5)
driver.find_element(By.ID, "langSelect-EN").click()
time.sleep(1)

cookie = driver.find_element(By.ID, "bigCookie")

timeout = 1
timeout_start = 0

def set_timeout_start():
    global timeout_start
    timeout_start = time.time()

set_timeout_start()

def check_if_exists_by_css_selector(css_selector):
    try:
        driver.find_element(By.CSS_SELECTOR, css_selector)
    except NoSuchElementException:
        return False
    return True

while True:
    if time.time() > timeout_start + timeout:
        if check_if_exists_by_css_selector("#upgrade0.crate.upgrade.enabled"):
            driver.find_element(By.CSS_SELECTOR, "#upgrade0.crate.upgrade.enabled").click()
        if check_if_exists_by_css_selector(".product.unlocked.enabled"):
            enabled_products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            enabled_products[-1].click()
        # print(enabled_products)
        set_timeout_start()
    cookie.click()

