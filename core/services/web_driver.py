from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import options, service

def create_driver(additional_options=None):
    chrome_options = webdriver.ChromeOptions()
    for option in options.arguments:
        chrome_options.add_argument(option)
    if additional_options:
        for option in additional_options:
            chrome_options.add_argument(option)
    return webdriver.Chrome(service=service, options=chrome_options)
