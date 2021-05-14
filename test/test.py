import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_google():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    driver.find_element_by_xpath("//*[@name = 'q']").send_keys("amazon")
    driver.find_element_by_xpath("//*[@name = 'q']").send_keys(Keys.ENTER)

    driver.close()


