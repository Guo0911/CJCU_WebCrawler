#---------------------------------------
# 題目：抓取自己班級的課程綱要
# 提示：若需要填空都有註解標明
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

url = "https://eportal.cjcu.edu.tw/syllabus"
chrome.get(url)

# select.select_by_index(0) 透過選項排序,0為第一個選項
# select.select_by_value("AME") 透過value
# select.select_by_visible_text("航運管理學系") 透過text

select = Select(chrome.find_element_by_id('deps'))
select.select_by_visible_text("資訊工程學系") #選定資訊工程學系

select = Select(chrome.find_element_by_id('grade'))
select.select_by_value("2") #選定二年級

select = Select(chrome.find_element_by_id('class_no'))
select.select_by_value("2") #選定B班

button = chrome.find_element_by_id('depcourses_button')
button.click() #按下搜尋

find = chrome.find_elements_by_xpath('//td') #搜尋元素

for i in range(len(find)//9):
     td = [find[j + (i * 9)] for j in range(9)]
     date = td[5].text.replace('\n','').replace('(','/').replace(')','/').split('/')

     print(
          '-----------第',i+1,'筆資料-----------', '\n' \
          '課程名稱 : ', td[0].text, '\n' \
          '開課碼 : ' , td[1].text, '\n' \
          '學分 : ', td[2].text, '\n' \
          '開課班級 : ', td[3].text, '\n' \
          '選必修 : ', td[4].text, '\n' \
          '日期 : ', date[0], '\n' \
          '時間 : ', date[1], '\n' \
          '地點 : ', date[2], '\n' \
          '教師 : ', td[6].text, '\n' \
          '課程大綱 : ', f'https://eportal.cjcu.edu.tw/Syllabus/Info/Course?syear=110&semester=2&openno={td[1].text}', '\n' \
          '----------------------------------\n'
     )