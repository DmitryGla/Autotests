from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sub = browser.find_element_by_css_selector("[type='submit']")
    sub.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)
    inp = browser.find_element_by_css_selector("#answer")
    inp.send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    '''
    кусок кода для парсинга ответа и попытка вставить на сайт степика ответ
    alert = browser.switch_to.alert
    answer_text = alert.text
    answer_text = answer_text.split(': ')[-1]
    browser.quit()
    browser = webdriver.Chrome()
    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    input_answer = browser.find_element_by_css_selector("#ember16169")
    input_answer.send_keys(int(answer_text))
    button1 = browser.find_element_by_css_selector(".submit-submission")
    button1.click()
    '''
finally:
    time.sleep(10)
    browser.quit()