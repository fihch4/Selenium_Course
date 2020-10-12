from selenium import webdriver
import time
import os


name = "Test_Name"
last_name = "Test_Last_Name"
email = "test@test.ru"
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла


try:
    browser = webdriver.Chrome()
    browser.get(link)


    upload_file = browser.find_element_by_xpath("//input[@type='file']").send_keys(file_path)

    name_input = browser.find_element_by_xpath("//input[@name='firstname']").send_keys(name)
    last_name_input = browser.find_element_by_xpath("//input[@name='lastname']").send_keys(last_name)
    email = browser.find_element_by_xpath("//input[@name='email']").send_keys(email)

    button2 = browser.find_element_by_xpath("//*[text()='Submit']")
    button2.click()


finally:
    time.sleep(10)
    browser.quit()


# element.send_keys(file_path)