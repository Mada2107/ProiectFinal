import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    FORM_AUTHENTICATION_LINK = (By.XPATH, '//a[text()="Form Authentication"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    ELEM_H4 = (By.XPATH, '//h4[@class="subheader"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    # Test 1 - Verificare login - logout
    def test_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.url_contains('/login'))
        url_dupa_delogare = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert url_dupa_delogare == expected_url, f'Invalid url: {url_dupa_delogare} ' \
                                                  f'este diferit de {expected_url}'

    # Test 2 - Brute force password hacking
    def test_brute_force_pass(self):
        var_parole = self.chrome.find_element(*self.ELEM_H4).text.split()
        url = None
        for password in var_parole:
            self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            url = self.chrome.current_url
            if "secure" in url:
                print(f'Parola secreta este {password}')
                break
            else:
                print("Nu am reusit sa gasesc parola.")
        assert "secure" in url, "Eroare: parola nu a fost gasita"
