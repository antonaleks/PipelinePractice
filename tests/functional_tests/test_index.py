from selenium import webdriver
import pytest
import os

from selenium.webdriver.common.by import By

chrome_driver = "E:/Учёба 2 сем/Облачка/PipelinePractice/tests/functional_tests/yandexdriver.exe" if "ChromeWebDriver" not in os.environ.keys() else os.path.join(
    os.environ["ChromeWebDriver"], 'chromedriver.exe')


class TestBackend:

    def setup(self):
        self.driver = webdriver.Chrome(chrome_driver)

    def test_add(self, url):
        self.driver.get(f'{url}/add/1&2')
        assert "Add 1 and 2. Got 3!" == self.driver.find_element(By.TAG_NAME, "body").text

    def test_multiply(self, url):
        self.driver.get(f'{url}/multiply/2&2')
        assert "Multiply 2 and 2. Got 4!" == self.driver.find_element(By.TAG_NAME, "body").text

    def test_divide(self, url):
        self.driver.get(f'{url}/divide/10&2')
        assert "Divide 10 and 2. Got 5.0!" == self.driver.find_element(By.TAG_NAME, "body").text

    def test_subtract(self, url):
        self.driver.get(f'{url}/subtract/9&2')
        assert "Subtract 9 and 2. Got 7!" == self.driver.find_element(By.TAG_NAME, "body").text

    def teardown(self):
        self.driver.quit()
