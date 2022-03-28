#---------------------------------------
# 題目：抓取自己班級的課程綱要
# 提示：若需要填空都有註解標明，選項及按鈕id不一定與範例的相同。
#---------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False, 'profile.default_content_setting_values' :{'notifications' : 2}})
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(chrome_options=options)
chrome.maximize_window()

url = "" #自行填空
chrome.get(url)

select = Select(chrome.find_element_by_id()) #自行填空
select.select_by_visible_text() #自行填空

select = Select(chrome.find_element_by_id()) #自行填空
select.select_by_value() #自行填空

select = Select(chrome.find_element_by_id()) #自行填空
select.select_by_value() #自行填空

button = chrome.find_element_by_id() #自行填空
button.click()

find = chrome.find_elements() #自行選擇功能及抓取的元素

for i in range(): #自行填空
     print() #自行填空，依照個人喜好設計輸出即可。