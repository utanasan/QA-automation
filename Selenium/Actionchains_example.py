
from selenium.webdriver import ActionChains
from selenium import webdriver


chrome = webdriver.Chrome()
actions = ActionChains(chrome)
chrome.implicitly_wait(5)
chrome.get("https://sketch.io/sketchpad/en/")
elem = chrome.find_element_by_xpath("/html/body/dialog/alertify-dialog/p/div/alert-close-link")
elem.click()
area = chrome.find_element_by_xpath("/html/body/sketchpad/sketch-primarytoolbar/sketch-toolgroup[1]/sketch-tool[3]")
actions.move_to_element_with_offset(area,150, 150).click_and_hold().move_by_offset(150, 300).move_by_offset(0, 100).release().perform()

