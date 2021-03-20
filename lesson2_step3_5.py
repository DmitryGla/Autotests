from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)
    inp = browser.find_element_by_css_selector("#answer")
    inp.send_keys(y)
    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
    