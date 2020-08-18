from selenium import webdriver
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_use_API_1(self):
        # Peter is me, and Peter want to access /user/list to get the list of
        # user's list (by GET)
        self.browser.get('http://localhost:8000/v1/user/list')

        # Peter find that it return a JSON reponse
        help(self.browser)
        self.fail("assert that the return reponse is JSON")
        self.fail("Finish test!")

        # Peter want to access /user, but it return a error
        self.browser.get('http://localhost:8000/v1/user')
        self.fail('need get a error')

        # Peter post a request with vaild session and it works
        self.fail('Finish test!')
