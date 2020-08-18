from selenium import webdriver
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_use_API_1(self):
        self.fail("Hello")
