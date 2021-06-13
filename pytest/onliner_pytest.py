from fixtures_onliner import *


def test_vacancies(browser):
    elem = browser.find_element_by_link_text("Вакансии")
    elem.click()
    elem = browser.find_element_by_tag_name("h1")
    assert elem.text == 'Вакансии'

def test_empty_basket(browser):
    elem = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[3]/div/div[2]/div[2]/div[3]/div/a")
    elem.click()
    elem = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div[2]")
    assert elem.text == 'Ваша корзина пуста'


