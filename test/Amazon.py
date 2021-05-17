import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_google():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/')
    driver.find_element_by_xpath("//*[@id = 'twotabsearchtextbox']").send_keys("pen")
    driver.find_element_by_xpath("//*[@id ='nav-search-submit-button']").send_keys(Keys.ENTER)
    time.sleep(5)

    driver.close()


