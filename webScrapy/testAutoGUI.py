import pyautogui
import webbrowser
chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'
url = "http://www.dwnews.com"
webbrowser.get(chrome_path).open(url)
