import pytest
from selenium import webdriver



@pytest.fixture()
def browser():
    
    driver = webdriver.Chrome()
   
    page = driver.get('https://www.onliner.by/')
    
    yield driver
    
    driver.close()
