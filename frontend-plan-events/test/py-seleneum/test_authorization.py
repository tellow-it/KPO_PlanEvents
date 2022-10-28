from selenium.webdriver.common.by import By
import time


link = 'http://localhost:3000/'


def test_search(browser):
    # Зайти на сайт https://mail.yandex.ru/
    browser.get(link)
    browser.implicitly_wait(10)

    

    # # Кликнуть по кнопке "Почта", т.е. войти по почте
    # button_mail = browser.find_element(By.CSS_SELECTOR, "[data-type='login']")
    # button_mail.click()

    # Ввести в поле "Логин или email" почту
    input_mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите логин']")
    input_mail.send_keys("asdf")

    # # Кликнуть по кнопке "Войти"
    # button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # button_enter.click()

    # Ввести в поле "Введите пароль" пароль
    input_mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_mail.send_keys("asdf")

    # Кликнуть по кнопке "Войти"
    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    # Кликнуть по кнопке "Пропустить"
    try:
        button_enter = browser.find_element(By.CSS_SELECTOR, "span a[class*='Button2']")
        button_enter.click()
    except:
        pass

    time.sleep(3)
