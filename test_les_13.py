import pytest
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

def test_exeption_1():
    try:
        driver = webdriver.Chrome()
        driver.get("https://casenik.com.ua/")  # открываем страницу
        with pytest.raises(NoSuchElementException):
            driver.find_element("xpath", "//button[@class='header_search_button trans_300']")
            pytest.fail("Не повинно бути кнопки")
    finally:
        driver.quit()

def test_exeption_2():
    try:
        driver = webdriver.Chrome()
        driver.get("https://casenik.com.ua/")  # открываем страницу
        with pytest.raises(NoSuchElementException):
            driver.find_element("css selector", "no_such_button.btn")
            pytest.fail("Не повинно бути кнопки")
    finally:
         driver.quit()

