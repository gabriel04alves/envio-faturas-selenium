from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
import time
import fitz  
import re
import requests

# Configuração do ChromeDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Rodar com interface gráfica para depuração
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")