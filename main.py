from selenium import webdriver


chrome_driver_path = "/User/Etc"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
price = driver.find_element_by_id("webid")

# Other ways to find elements
find_element_by_name - very useful, especially when filling in webforms.

x = driver.find_element_by_name("elementname")


y = driver.find_element_by_class_name("name of class")



l = driver.find_element_by_css_selector(".exampleclass a")


# way to get an element by a path.

driver.find_element_by_xpath("xpath")


# Finding multple elements
driver.find_elements()


# Example

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
for names in event_names:
    print(names.text)
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
