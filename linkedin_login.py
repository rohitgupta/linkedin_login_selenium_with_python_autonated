#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:16:16 2018

@author: rohit
"""

from selenium import webdriver
linkusrname = str(input('Enter email address or number with country code: '))
linkusrpwd=input('Enter Password:')
driver = webdriver.Chrome()
url = 'https://www.linkedin.com/'
driver.get(url)
driver.find_element_by_id('login-email').send_keys(linkusrname)
print ('Email ID Entered successfully.')
driver.find_element_by_id('login-password').send_keys(linkusrpwd)
print ('Password Entered successfully.')
driver.find_element_by_id('login-submit').click()
print('Submit Button clicked successfully')
driver.find_element_by_xpath('/html/body')
print('Linkdin reach till Top of Button.')
driver.quit()