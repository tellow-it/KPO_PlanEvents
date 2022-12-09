from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time


link = 'http://localhost:3000/SignUp'


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
    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required" 
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
    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required" 
    time.sleep(1)

def test_empty_all_field(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert username_error_div_information.text=="Required" 
    assert password_error_div_information.text=="Required"
    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required"  
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
    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required"  
    
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

    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required"  
    
    time.sleep(1)

def test_long_email(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите email']")
    input_email.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaap19052016@gmail.com")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Required" 
    assert username_error_div_information.text=="Required"

    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Too Long!"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required"  
    
    time.sleep(1)

def test_bad_email(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите email']")
    input_email.send_keys("aaa190520")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()


    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Invalid email"

    
    time.sleep(1)

def test_long_email(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите email']")
    input_email.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaap19052016@gmail.com")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Required" 
    assert username_error_div_information.text=="Required"

    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Too Long!"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Required"  
    
    time.sleep(1)


def test_small_phone(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите номер телефона']")
    input_phone.send_keys("78879")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Required" 
    assert username_error_div_information.text=="Required"

    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Too Short!"  
    
    time.sleep(1)


def test_success_registration(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_username = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите логин']")
    input_username.send_keys("asdf" + str(random.randint(0, 100000000000000)))

    input_password = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_password.send_keys("asdf")

    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите номер телефона']")
    input_phone.send_keys(str(random.randint(10000000000, 99999999999)))

    input_password = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите email']")
    input_password.send_keys("asdf" + str(random.randint(1000, 999999)) + "p19052016@gmail.com")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()



def test_long_phone(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите номер телефона']")
    input_phone.send_keys("7777777777777777777777777777777777777")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    username_error_div_information = browser.find_element(By.NAME, 'username-error-messege')
    password_error_div_information = browser.find_element(By.NAME, 'password-error-messege')

    assert password_error_div_information.text=="Required" 
    assert username_error_div_information.text=="Required"

    email_error_div_information = browser.find_element(By.NAME, 'email-error-messege')
    assert email_error_div_information.text=="Required"
    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="Too Long!"  
    
    time.sleep(1)


def test_not_number_in_phone_field(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    input_phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите номер телефона']")
    input_phone.send_keys("asdf")

    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    phone_error_div_information = browser.find_element(By.NAME, 'phone-error-messege')
    assert phone_error_div_information.text=="phone must be a `number` type, but the final value was: `NaN` (cast from the value `\"asdf\"`)."  
    
    time.sleep(1)



