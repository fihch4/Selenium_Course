from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_tag_name("button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input_value = calc(browser.find_element_by_xpath("//span[@id='input_value']").text)
    print(input_value)

    input_str = browser.find_element_by_tag_name("input").send_keys(input_value)

    submit = browser.find_element_by_xpath("//*[contains(text(),'Submit')]").click()

finally:
    time.sleep(5)
    browser.quit()