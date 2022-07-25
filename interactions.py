from selenium import webdriver
# This needs to be imported to use keys within Selenium
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/joshwood/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
article_count.click()

# Find method through links & clicking on them...

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

# Using search bars
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

#####-------------------------Example of using Selenium to fill in a form------------------------------------------####

driver.get("testform.com")
first_name = driver.find_element_by_name("Firstname")
first_name.send_keys("Timmy")
last_name = driver.find_element_by_name("Lastname")
last_name.send_keys("Timpson")
email = driver.find_element_by_name("email")
email.send_keys("test@test.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()

#####-------------------------Example of using Selenium to fill in a form------------------------------------------####


