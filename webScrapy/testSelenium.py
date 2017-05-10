import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
curDir  = os.path.dirname(os.path.realpath(__file__))
strExecutable_path = os.path.join(curDir,'chromedriver_win32//chromedriver.exe')
browser = webdriver.Chrome(executable_path=strExecutable_path)
browser.get('http://www.163.com')

##
##elem = browser.find_element_by_name('p')  # Find the search box
##elem.send_keys('seleniumhq' + Keys.RETURN)
##
##browser.quit()
