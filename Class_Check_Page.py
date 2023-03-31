import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Check_page(unittest.TestCase):
    FORM_AUTHENTICATION_LINK=(By.XPATH,'//a[text()="Form Authentication"]')
    LOGIN_BUTTON=(By.XPATH,'//*[@id="login"]/button/i')
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

    # Test 1 - Verificare URL
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected,actual, 'URL-ul nu este corect')

    # Test 2 - Verificare page title
    def test_page_title(self):
        actual=self.chrome.title
        expected='The Internet'
        self.assertEqual(expected, actual,
                         f' Titlul paginii este {actual}, '
                         f'dar ar fi trebuit sa fie {expected}')


    # Test 3 - Verificare Login button
    def test_login_displayed(self):
        button=self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(),'Butonul de LOGIN nu este vizibil')

    # Test 4 - Verificare eroare user/pass goale
    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')



