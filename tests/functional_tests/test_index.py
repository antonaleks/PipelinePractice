from selenium import webdriver
import unittest
import os

url = 'http://localhost:5000'
chrome_driver = "C:/Users/IIoT_Lab/PycharmProjects/flaskProject/tests/functional_tests/yandexdriver.exe" if "ChromeWebDriver" not in os.environ.keys() else os.path.join(
    os.environ["ChromeWebDriver"], 'chromedriver.exe')


class FunctionalTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_driver,
                                       chrome_options=options)

    def test_add(self):
        self.driver.get(f'{url}/add/1&2')
        self.assertEqual("Add 1 and 2. Got 3!", self.driver.find_element_by_tag_name("body").text)

    def test_multiply(self):
        self.driver.get(f'{url}/multiply/2&2')
        self.assertEqual("Multiply 2 and 2. Got 4!", self.driver.find_element_by_tag_name("body").text)

    def test_divide(self):
        self.driver.get(f'{url}/divide/10&2')
        self.assertEqual("Divide 10 and 2. Got 5.0!", self.driver.find_element_by_tag_name("body").text)

    def test_subtract(self):
        self.driver.get(f'{url}/subtract/9&2')
        self.assertEqual("Subtract 9 and 2. Got 7!", self.driver.find_element_by_tag_name("body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
