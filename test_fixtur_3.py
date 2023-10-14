"""
Ймовірно, ви помітили, що в попередньому прикладі ми не використовували команду browser.quit().
Це призвело до того, що кілька процесів браузера залишалися активними після закінчення тестів,
а закрилися вони тільки після завершення всіх тестів.
Закриття браузерів сталося завдяки вбудованій фікстурі — "збирача сміття".
Але якби кількість тестів налічувала більше кількох десятків,
то така кількість браузерів могла призвести до того, що оперативна пам'ять закінчилася дуже швидко.
Тому треба закривати браузери після кожного тесту. Для цього ми можемо скористатися фіналізаторами.
Один із варіантів фіналізатора – використання ключового слова Python: yield.
Після завершення тесту, який викликав фікстуру, виконання фікстури продовжиться з рядка, наступного за рядком зі словом yield.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"

"""
Якщо активуємо цей код, то область видимості буде в рамках класу, і тоді браузер відкриється і закриється лише один раз, 
а всі тести будуть виконуватись один за одним. в одному й тому ж екземплярі браузера. Так робити НЕ рекомендується.
"""
# @pytest.fixture(scope="class")
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # цей код виконається після завершення всього тесту
    print("\nquit browser..")
    browser.quit()


"""Автовикористання фікстур"""
# @pytest.fixture(autouse=True)
# def prepare_data():
#     print("print this str for every test")


class TestPage1():
    # викликаємо фікстуру в тесті, передавши її як параметр
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

"""
Допоміжні функції - це дуже потужна штука, яка вирішує багато проблем під час роботи з автотестами. 
Основний плюс у тому, що їх зручно використовувати у будь-яких тестах без дублювання зайвого коду.
Додаткові матеріали про фікстури:
https://docs.pytest.org/en/stable/fixture.html
"""

