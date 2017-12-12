#!/usr/bin/env python3
# import pytesser3
# use for login outside network 
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
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler 
import logging

url = r'http://202.103.24.68:90/p/30247dd99271a6806206be0598a1cf9e/index.html?d3d3LnRjbC50ay9tYW4vdGNsOC41L1RjbExpYi9jb250ZW50cy5odG0='


def login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    # 打开网址
    driver.get(url)
    locator = (By.ID, 'submit_button_1')
    WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(locator))

    element=driver.find_element_by_id('username')
    element.clear()
    element.send_keys('xhchen5865')

    element=driver.find_element_by_id('password1')
    element.clear()
    element.send_keys('fh0211005865')

    element=driver.find_element_by_id('submit_button_1')
    element.click()

    logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='login.log',
                filemode='a')

    logging.info('login success at %s' %datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


    driver.quit()

    return driver


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(login, 'cron', day_of_week='*', hour='*/2')
    # driver.quit()
    try:
        scheduler.start()
    except Exception as e:
        scheduler.shutdown(wait=false)
        print ("Exception found in login", format(e))
        logging.basicConfig(level=logging.DENUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='login.log',
                filemode='a')
        logging.debug("Exception found in login %s" %format(e))
