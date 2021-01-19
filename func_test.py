import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://127.0.0.1:8000/');

assert driver.page_source.find('zuzuzaza')