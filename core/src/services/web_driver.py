from selenium import webdriver
from config import options, service

def create_driver():
    return webdriver.Chrome(service=service, options=options)
