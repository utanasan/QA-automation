import pytest
from selenium import webdriver


# фикстура для запуска браузера перед тестом и закрытия после теста
@pytest.fixture()
def browser():
    # запуск Chrome при начале каждого теста (до yield)
    driver = webdriver.Chrome()
    # открытие страницы при начале каждого теста
    page = driver.get('https://www.onliner.by/')
    # передача драйвера для использования в тесте
    yield driver
    # закрытие браузера после теста (после yield)
    driver.close()