from django.test import TestCase
from selenium import webdriver
# Create your tests here.

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.

    def test_there_is_homepage(self):
        self.driver.get('http://127.0.0.1:8000/');
        self.assertIn('Enter hash here:', self.driver.page_source)

    def test_hash_of_hello(self):
        self.driver.get('http://127.0.0.1:8000/');
        text = self.driver.find_element_by_id('id_text')
        text.send_keys('hello')
        self.driver.find_element_by_name('submit').click()
        self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824',self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

