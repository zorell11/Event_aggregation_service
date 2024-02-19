from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from django.test import TestCase
import time


class SignUpTestWithSelenium(TestCase):

    def test_index(self):
        selenium_webdriver = webdriver.Firefox()

        selenium_webdriver.get('http://127.0.0.1:8000')

        assert 'EventDB - najlepsie eventy u nas' in selenium_webdriver.page_source

    def test_sing_up(self):
        selenium_webdriver = webdriver.Firefox()
        selenium_webdriver.get('http://127.0.0.1:8000')
        time.sleep(2)
        signup_button = selenium_webdriver.find_element(By.ID, 'signup-user')
        signup_button.send_keys(Keys.RETURN)

        assert 'Registrácia' in selenium_webdriver.page_source

        input_email = input('Add user email: ')
        time.sleep(5)
        email_input = selenium_webdriver.find_element(By.NAME, 'email')
        email_input.send_keys(input_email)
        time.sleep(1)
        # email_input.send_keys('test_user@user.sk')
        first_name = selenium_webdriver.find_element(By.NAME, 'first_name')
        first_name.send_keys('custom_user_first_name')
        time.sleep(1)
        last_name = selenium_webdriver.find_element(By.NAME, 'last_name')
        last_name.send_keys('custom_user_last_name')
        time.sleep(1)
        password1 = selenium_webdriver.find_element(By.NAME, 'password1')
        password1.send_keys('Test_pass123')
        time.sleep(1)
        password2 = selenium_webdriver.find_element(By.NAME, 'password2')
        password2.send_keys('Test_pass123')
        time.sleep(1)
        phone = selenium_webdriver.find_element(By.NAME, 'phone')
        phone.send_keys('123456')
        address = selenium_webdriver.find_element(By.NAME, 'address')
        address.send_keys('custom_user_test_address')

        button = selenium_webdriver.find_element(By.ID, 'register-button')
        button.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_sing_up(self):
        selenium_webdriver = webdriver.Firefox()
        selenium_webdriver.get('http://127.0.0.1:8000')
        time.sleep(2)
        signup_button = selenium_webdriver.find_element(By.ID, 'login')
        signup_button.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Prihlásenie' in selenium_webdriver.page_source

        email = selenium_webdriver.find_element(By.NAME, 'username')
        email.send_keys('xxxx@azet.sk')
        time.sleep(1)
        password1 = selenium_webdriver.find_element(By.NAME, 'password')
        password1.send_keys('Test_pass123')
        time.sleep(1)
        login_button = selenium_webdriver.find_element(By.ID, 'login-button')
        login_button.send_keys(Keys.RETURN)
        time.sleep(5)

        assert 'test_user@user.sk' in selenium_webdriver.page_source
        #assert 'Prihlásený ako: test_user@user.sk' in selenium_webdriver.page_source
