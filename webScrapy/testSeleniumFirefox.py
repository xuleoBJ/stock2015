from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



browser = webdriver.Firefox(executable_path=r'geckodriver-v0.15.0-win64//geckodriver.exe')

browser.get('http://www.yahoo.com')
assert 'Yahoo!' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
print("ok")
browser.quit()
