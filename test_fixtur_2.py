"""
Фікстури можуть повертати значення, яке можна використовувати в тестах.
Давайте перепишемо наш попередній приклад із використанням PyTest фікстур.
Ми створимо фікстуру browser, яка створюватиме об'єкт WebDriver.
Цей об'єкт ми зможемо використовувати у тестах для взаємодії із браузером.
Для цього ми напишемо метод browser та вкажемо, що він є фікстурою за допомогою декоратора @pytest.fixture.
Після цього ми можемо викликати фікстуру у тестах, передавши її як параметр.
За замовчуванням фікстура створюватиметься для кожного тестового методу,
тобто для кожного тесту запуститься свій екземпляр браузера.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestPage1():
    # викликаємо фікстуру в тесті, передавши її як параметр
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")



