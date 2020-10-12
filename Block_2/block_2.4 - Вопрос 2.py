from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element_by_xpath("//button[@id='book']").click()

    input_value = calc(browser.find_element_by_xpath("//span[@id='input_value']").text)
    print(input_value)

    input_str = browser.find_element_by_tag_name("input").send_keys(input_value)

    submit = browser.find_element_by_xpath("//*[contains(text(),'Submit')]").click()




finally:
    time.sleep(5)
    browser.quit()

