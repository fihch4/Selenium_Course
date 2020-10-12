from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//div[@class='form-group']//span[@id='input_value']")
    x = calc(x_element.text)

    input = browser.find_element_by_id("answer")
    input.send_keys(x)

    radio = browser.find_element_by_css_selector("[for='robotCheckbox']")
    radio.click()

    robots = browser.find_element_by_css_selector("[for='robotsRule'")
    robots.click()

    button = browser.find_element_by_xpath("//*[text()='Submit']")
    button.click()





finally:
    time.sleep(10)
    browser.quit()