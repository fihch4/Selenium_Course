from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_xpath("//span[@id='input_value']").text
    result_x = calc(x_value)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    sent_value = browser.find_element_by_id("answer").send_keys(result_x)

    robot_check_box = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()

    robots = browser.find_element_by_css_selector("[for='robotsRule'")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots)
    robots.click()

    button2 = browser.find_element_by_xpath("//*[text()='Submit']")
    button2.click()




finally:
    time.sleep(10)
    browser.quit()