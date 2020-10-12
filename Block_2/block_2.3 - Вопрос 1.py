from selenium import webdriver
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)


    button_click = browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert.accept()

    input_value = calc(browser.find_element_by_xpath("//span[@id='input_value']").text)
    print(input_value)

    input_str = browser.find_element_by_tag_name("input").send_keys(input_value)

    submit = browser.find_element_by_xpath("//*[contains(text(),'Submit')]").click()

finally:
    time.sleep(10)
    browser.quit()