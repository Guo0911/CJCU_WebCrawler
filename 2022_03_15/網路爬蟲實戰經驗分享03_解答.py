#---------------------------------------
# 題目：讓程式抓取Dcard首頁的文章標題與連結
#---------------------------------------

from selenium import webdriver

options = webdriver.ChromeOptions() #瀏覽器設定
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False, 'profile.default_content_setting_values' :{'notifications' : 2}})
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(chrome_options = options)
chrome.maximize_window() #最大化Chrome的畫面

url = "https://www.dcard.tw/f"
chrome.get(url)

data = chrome.find_elements_by_xpath("//a[@class='tgn9uw-3 bJQtxM']")#請自行補上抓取的方式與元素定位

#請自行新增輸出的程式碼
for i in data:
    print(i.text)
    print(i.get_attribute('href'))