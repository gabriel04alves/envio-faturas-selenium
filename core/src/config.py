from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Uncomment the line below to run the browser in headless mode
options.add_argument("--headless") 

service = Service("/usr/bin/chromedriver")
