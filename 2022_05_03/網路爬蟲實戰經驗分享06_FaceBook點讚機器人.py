# 使用「pip install selenium」先安裝Selenium
# 使用「pip install webdriver_manager 」 安裝WebDriver_manager

import msvcrt, time, random # 導入msvcrt實現隱藏輸入密碼；導入time用於暫停程式；導入random用於隨機暫停時長
from selenium import webdriver # 導入WebDriver
from selenium.webdriver.common.keys import Keys # 導入Keys用於使用ENTER登入
from webdriver_manager.chrome import ChromeDriverManager # 導入ChromeDriverManager用於更新ChromeDriver版本

options = webdriver.ChromeOptions() # 瀏覽器設定
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False, 'profile.default_content_setting_values' :{'notifications' : 2}})
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options) # 自動更新ChromeDriver及調整預設的chrome瀏覽器設定
chrome.maximize_window() # 最大化Chrome的畫面


def input_password(): # 用於隱藏密碼的輸入方式
    chars = []
    while True:
        newChar = msvcrt.getch().decode(encoding="utf-8") # 獲得輸入的文字

        if newChar in "\r\n": # 如果是換行，則輸入結束
            print() #換行
            break
        elif newChar == "\b": # 如果是backspace，則刪除密碼末尾一位並且刪除一個星號
            if chars:
                del chars[-1]
                msvcrt.putch("\b".encode(encoding="utf-8")) # 輸入點退一格
                msvcrt.putch( " ".encode(encoding="utf-8")) # 輸出一個空格覆蓋原來的星號
                msvcrt.putch("\b".encode(encoding="utf-8")) # 輸入點退一格
        else:
            chars.append(newChar)
            msvcrt.putch("*".encode(encoding="utf-8")) # 顯示為星號
    return ("".join(chars)) # 將陣列chars的所有字變為String


def login():
    email = input("Please input your email : ") # 每次都輸入同組的話，也可將input部分改為自己帳號即可免除輸入email的步驟
    context = chrome.find_element_by_name('email') # 尋找輸入email的位置，也就是登入的帳號
    context.send_keys(email) # 輸入變數email的值到上一行尋找到的位置
    
    print("Please input your password : ", end = "") # 「end = "1"」的話會在最後輸出結尾輸出1，並且不會做換行
    password = input_password()
    context = chrome.find_element_by_name('pass') # 尋找輸入password的位置，也就是帳號的密碼
    context.send_keys(password) # 輸入變數password的值到上一行尋找到的位置

    context.send_keys(Keys.ENTER) # 輸入ENTER進行登入，與我們輸入完帳號密碼後按ENTER一樣
    time.sleep(7) # 等待網站更新完成

    try: # 當try內的程式出現錯誤時，並不會讓程式中斷，而是掉到except裡面的程式碼執行，避免程式執行時中斷的方式
        hint = chrome.find_element_by_class_name("_9ay7") # 抓取訊息提示框
        if "未與帳號連結" in hint.text or "密碼錯誤" in hint.text: # 如果帳號錯誤或密碼錯誤在提示框內
            login() # 再次執行登入
    except: # 程式出現錯誤時執行except內的程式碼，若except內出現錯誤則程式會直接中斷
        print("登入成功") # 因為當程式找不到訊息提示框，代表已成功登入
        chrome.get("https://www.facebook.com") # 跳至facebook首頁，新帳號才需要使用此行，因新帳號登入後常出現無任何貼文的狀況


chrome.get("https://www.facebook.com/login") # 讓Chrome進入facebook登入頁面
time.sleep(3) # 讓程式停止3秒，用於等待網頁完全進入

login() # 執行登入的function

times = 0 # 紀錄目前按到的位置，避免程式重複按之前的按鈕

while True:
        chrome.execute_script("window.scrollBy(0, 2000)") # 下滑2000像素的距離
        # 「execute_script」執行JavaScript
        # 「window.scrollBy(x,y)」向右滑動x個像素，並向下滑動y個像素，若為負則往左x個像素、往上y個像素
        time.sleep(random.randint(2,4)) # 等待網站更新完成，如果更新未完成會導致找不到新的按鈕
        
        likes = chrome.find_elements_by_xpath('//div[contains(@class, "oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz i1ao9s8h esuyzwwr du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh p8dawk7l lzcic4wl pphx12oy b4ylihy8 rz4wbd8a b40mr0ww a8nywdso hmalg0qr q45zohi1 g0aa4cga pmk7jnqg gokke00a")]')
        # 抓取要按讚的元素位置
        if len(likes) > times: # 偵測找到的按鈕是否比按過的按鈕多，如果比較少代表程式找到的按鈕數有問題或更新有問題
            for i in range(times,len(likes)): # 跳過按過的按鈕，直接從最後一次的下一個開始
                time.sleep(random.randint(1,3)) # 每次按讚的間隔，不建議等待時間太短，可能會被伺服器偵測為機器人而封鎖
                times += 1 # 增加按下的次數
                webdriver.ActionChains(chrome).move_to_element(likes[i]).click(likes[i]).perform() #按下按鈕
                # ActionChains為一種非立即執行的方式，他會先將設定好的操作儲存，直到「perform()」才會執行
                # 「move_to_element(x)」會將滑鼠移到()內指定的元素x的位置；「click(x)」用於點擊元素x；「perform()」代表讓ActionChains執行動作
        else:
            chrome.refresh() # 讓程式刷新頁面
            times = 0 # 因網頁刷新，因此要重製紀錄