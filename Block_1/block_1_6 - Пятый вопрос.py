from selenium import webdriver
import time

first_name = "Vanya"
last_name = "Skvorcov"
email = "v_skvorcov@mail.ru"

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div[contains(@class,'first_class')]/input")
    input1.send_keys(first_name)

    input2 = browser.find_element_by_xpath("//div[contains(@class,'second_class')]/input")
    input2.send_keys(last_name)

    # input3 = browser.find_element_by_css_selector("input.third") #Так как используется class, ставим точку
    input3 = browser.find_element_by_xpath("//div[contains(@class,'third_class')]/input")
    input3.send_keys(email)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#последняя пустая строка