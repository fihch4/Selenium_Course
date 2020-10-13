from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element_by_xpath("//h2/img")
    value_x_attrubute = calc(value_x.get_attribute("valuex"))


    input = browser.find_element_by_xpath("//input[@id='answer']")
    input.send_keys(value_x_attrubute)

    checkbox = browser.find_element_by_xpath("//input[@type='checkbox']").click()

    robots = browser.find_element_by_css_selector("[id='robotsRule'")
    robots.click()

    button = browser.find_element_by_xpath("//*[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

