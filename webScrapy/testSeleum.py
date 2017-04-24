import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path=r'chromedriver_win32//chromedriver.exe')
browser.get('http://www.163.com')

##
##elem = browser.find_element_by_name('p')  # Find the search box
##elem.send_keys('seleniumhq' + Keys.RETURN)
##
##browser.quit()
