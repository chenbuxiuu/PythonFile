#!/usr/bin/env python3
# import pytesser3
# use for clear mail 
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from datetime import datetime
import time
import os

url = r'http://mail.fiberhome.com'

# 判断元素是否存在
def isElementExist(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
        print(xpath,' exist')
        return True
    except Exception as e:
        # print(format(e))
        print(xpath,' not exist')
        return False

def login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    # 打开网址
    driver.get(url)
    locator = (By.ID, 'uid')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(locator))

    element=driver.find_element_by_id('uid')
    element.clear()
    element.send_keys('')

    element=driver.find_element_by_id('password')
    element.clear()
    element.send_keys('')

    element=driver.find_element_by_id('login_button')
    element.click()

    return driver

def refresh(driver):
    element=driver.find_element_by_name('refreshBtn')
    element.click()

def delete(driver):
    driver.switch_to.frame('folder')
    element=driver.find_element_by_id('listMessage')
    xpath=r'//div[@id="listMessage"]/div[@class="emptymail"]'
    while not isElementExist(driver,xpath):
        # 全选当前页面
        element=driver.find_element_by_id('selectCheckBox')
        element.click()
        # 删除
        element=driver.find_element_by_xpath('//div[@name="delete"]')
        element.click()
        # 刷新
        refresh(driver)
    driver.switch_to.default_content()

def clear(driver):
    locator=(By.ID,'navFid_1')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(locator))
    # 收件箱     
    element=driver.find_element_by_id('navFid_1')
    element.click()
    delete(driver)    
    # 遍历收件箱子文件夹
    
    element=driver.find_element_by_xpath('//*[@id="nav_system"]/li[1]/i')
    element.click()
    elements=driver.find_elements_by_xpath('//*[@id="nav_system"]/li[1]//li')
    delete(driver)
    for item in elements:
        item.click()
        delete(driver)

    # 清空已删除
    xpath=r'//a[@class="nav_empty"]'
    driver.switch_to.default_content()
    if isElementExist(driver,xpath):
        # 清空
        element=driver.find_element_by_xpath(xpath)
        element.click()
        # 确认
        element=driver.find_element_by_xpath('//div[@class="sigbtn sigbtn-on"]')
        element.click()

        print('clear done')
    else:
        print('The mailbox is empty')
    driver.quit()



if __name__ == '__main__':

    driver=login()
    clear(driver)
