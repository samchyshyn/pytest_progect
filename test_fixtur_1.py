"""
Важливою складовою використання PyTest є концепція фікстур. Фікстури в контексті PyTest – це допоміжні функції для наших тестів,
які не є частиною тестового сценарію.
Призначення фікстур може бути різним.
Одне з поширених застосувань фікстур - це підготовка тестового оточення
а очищення тестового оточення та даних після завершення тесту.
Докладніше про фікстури в широкому сенсі можете прочитати у Вікіпедії.
Класичний спосіб роботи з фікстурами - створення setup- і teardown-методів у файлі з тестами (документація PyTest).
Можна створювати фікстури для модулів, класів та окремих функцій.
Спробуємо написати фікстуру для ініціалізації браузера, який ми потім зможемо використовувати в наших тестах.
Після закінчення тестів ми автоматично будемо закривати браузер за допомогою команди browser.quit(),
щоб у нашій системі не було безліч відкритих вікон браузера.
Винесемо ініціалізацію та закриття браузера у фікстурі, щоб не писати цей код для кожного тесту.
Зразу об'єднуватимемо наші тести в тест-сьюти, роль тест-сьюту гратимуть класи, в яких ми зберігатимемо наші тести.
Розглянемо два приклади:
створення екземпляра браузера та його закриття лише один раз для всіх тестів першого тест-сьюту
та створення браузера для кожного тесту у другому тест-сьюті.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://casenik.com.ua/"


class TestPage1():

    @classmethod
    def setup_class(self): #буде впливати на весь клас
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self): #буде впливати на весь клас
        print("\nquit browser for test suite..")
        self.browser.quit()

    def test_is_button_search(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//a[@href = 'cart/show']")


class TestPage2():

    def setup_method(self): #буде впливати лише на окремий метод/функцію
        print("\nstart browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self): #буде впливати лише на окремий метод/функцію
        print("\nquit browser for test..")
        self.browser.quit()

    def test_is_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//div[@class = 'top_bar_user']/a[@href = 'user/login']")

    def test_is_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

"""
Це класичний спосіб використання фікстур.
PyTest пропонує продвинутий підхід до фікстур, коли фікстури можна задавати глобально, 
передавати їх у тестові методи як параметри.
В наступному скрипті розглянему це на прикладі.
"""
