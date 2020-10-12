from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

def sum_all(x_sum, y_sum):
    z_sum = int(x_sum) + int(y_sum)
    return z_sum

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_xpath("//span[@id='num1']").text
    num2 = browser.find_element_by_xpath("//span[@id='num2']").text
    summa = sum_all(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))

    submit = browser.find_element_by_xpath("//*[contains(text(),'Submit')]").click()


finally:
    time.sleep(10)
    browser.quit()
