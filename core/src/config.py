from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
