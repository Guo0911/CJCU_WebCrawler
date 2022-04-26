#下載ChromeDriver並啟用
#pip install selenium 先安裝Selenium

from selenium import webdriver #導入WebDriver

options = webdriver.ChromeOptions() #瀏覽器設定
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False, 'profile.default_content_setting_values' :{'notifications' : 2}})
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(chrome_options = options)

chrome.maximize_window() #最大化Chrome的畫面

url = "https://tw.news.yahoo.com/archive/"
chrome.get(url) #讓Chrome進到url的頁面

data = chrome.find_elements_by_xpath("//a[@class='Fw(b) Fz(20px) Lh(23px) Fz(17px)--sm1024 Lh(19px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled']") #搜尋元素
# ***find_element若有s則為搜尋多個，類似BeautifulSoup的find_all；反之若沒有s則為搜尋第一個，類似find。

for i in data:
    print(i.text) #獲取文字
    print(i.get_attribute('href')) #獲取連結
