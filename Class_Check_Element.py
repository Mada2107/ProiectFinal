import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Check_text_element(unittest.TestCase):
    FORM_AUTHENTICATION_LINK = (By.XPATH, '//a[text()="Form Authentication"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    H2_ELEMENT = (By.XPATH, '//h2')
    HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="flash"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()

    # Test 1 - Verificare element
    def test_element(self):
        actual=self.chrome.find_element(*self.H2_ELEMENT).text
        print(f'Denumirea elementului este {actual}')
        expected='Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului '
                                           f'este {actual}, dar ar fi '
                                           f'trebuit sa fie {expected}')

    # Test 2 - Verificare href link
    def test_href_link(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')

     # Test 3 - Verificare mesaj eroare
    def test_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tom')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # Test 4 - Verificare elemente secure si flash succes
    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')




