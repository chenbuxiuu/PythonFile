#!/usr/bin/env python3
# import pytesser3
# use for login outside network 
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler 
import logging
import random


url = r'http://10.78.13.126:8080/ProtocolManagement/protocol/index'


def login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    # 打开网址
    driver.get(url)
    locator = (By.ID, 'loginId')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(locator))

    element=driver.find_element_by_id('loginId')
    element.clear()
    element.send_keys('guest')

    element=driver.find_element_by_id('password')
    element.clear()
    element.send_keys('123456')

    element=driver.find_element_by_id('login-submit')
    element.click()

    driver.get(r'http://10.78.13.126:8080/ProtocolManagement/protocol/index')

    locator = (By.ID, '3')
    WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located(locator))
    element=driver.find_element_by_xpath('//*[@id="3"]/ins')
    element.click()

    locator = (By.ID, '1194')
    WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located(locator))
    element=driver.find_element_by_xpath('//*[@id="1194"]/ins')
    element.click()

    # element=driver.find_element_by_xpath('//*[@id="3701"]/ins')
    # element.click()

    locator = (By.ID, '3701')
    WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located(locator))
    element=driver.find_element_by_xpath('//*[@id="3701"]/a')
    element.click()

    locator = (By.ID, 'indextabstrip')
    WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located(locator))
    element=driver.find_element_by_xpath('//*[@id="indextabstrip"]/ul/li[3]/span')
    element.click()
    # driver.quit()

    return driver

def move_mouse(driver):
    while 1:
        random.seed()
        x=random.randint(0,100)
        y=random.randint(0,100)
        ActionChains(driver).move_by_offset(x,y). perform()
        time.sleep(50)
        ActionChains(driver).move_by_offset(0,0). perform()


if __name__ == '__main__':
    try:
        driver=login()
        move_mouse(driver)
    except Exception as e:
        print ("Exception found in login", format(e))
    
