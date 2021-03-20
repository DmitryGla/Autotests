from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)
    inp = browser.find_element_by_css_selector("#answer")
    inp.send_keys(y)
    robo_check = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robo_check.click()
    robo_rule = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robo_rule)
    robo_rule.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()