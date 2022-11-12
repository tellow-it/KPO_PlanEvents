from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


link = 'http://localhost:3000/'


def test_short_username(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    input_username = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите логин']")
    input_username.send_keys("a")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    assert username_error_div_information.text=="Too Short!"
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')
    assert password_error_div_information.text=="Required" 
    time.sleep(1)





def test_long_username(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_username = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите логин']")
    input_username.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert username_error_div_information.text=="Too Long!" 
    assert password_error_div_information.text=="Required" 
    time.sleep(1)

def test_empty_username_and_password(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert username_error_div_information.text=="Required" 
    assert password_error_div_information.text=="Required" 
    time.sleep(1)


def test_short_password(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_password = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_password.send_keys("a")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Too Short!" 
    assert username_error_div_information.text=="Required" 
    
    time.sleep(1)


def test_long_password(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_password = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_password.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Too Long!" 
    assert username_error_div_information.text=="Required" 
    
    time.sleep(1)

def test_success_password(browser):
    # Зайти на сайт https://mail.yandex.ru/
    browser.get(link)
    browser.implicitly_wait(10)

    input_username = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите логин']")
    input_username.send_keys("asdf")

    input_password = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_password.send_keys("asdf")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    time.sleep(4)

    assert 'Plan Events' == browser.find_element(By.TAG_NAME, 'h1').text

