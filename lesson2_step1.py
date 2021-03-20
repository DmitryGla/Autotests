from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
    return str(int(x) + int(y))
try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element= browser.find_element_by_css_selector("#num2")
    y = y_element.text
    summa = calc(x, y)
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(summa)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()