import unittest
from selenium import webdriver


class OnlinerSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_vacancy(self):
        driver = self.driver
        driver.get("https://www.onliner.by/")
        self.assertIn("Onliner", driver.title)
        driver.implicitly_wait(5)
        elem = driver.find_element_by_link_text("Вакансии")
        elem.click()
        self.assertIn("Вакансии", driver.page_source)


    def test_facebook_link(self):
        driver = self.driver
        driver.get("https://www.onliner.by/")
        driver.implicitly_wait(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/footer/div/div/div/div[2]/div[1]/a[2]")
        elem.click()
        self.assertIn("Facebook", driver.page_source)


    def test_superprice(self):
        driver = self.driver
        driver.get("https://www.onliner.by/")
        driver.implicitly_wait(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[1]/div")
        elem.click()
        assert "по суперцене" in driver.page_source


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()