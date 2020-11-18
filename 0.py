# coding=utf-8
import os

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui      # 右键菜单选择

profile = {'download.default_directory': 'E://video'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
str = "https://www.kanbilibili.com/video/av57728971/"
option = webdriver.ChromeOptions()
option.add_experimental_option('prefs',profile)
option.add_argument("disable-infobars")     # 关闭自动检测提示
option.add_argument("--disable-gpu")    # 和下面语句一起使用
option.add_argument("--headless")       # 不显示界面运行
browser = webdriver.Chrome('chromedriver', chrome_options=option)
# browser.maximize_window()
browser.implicitly_wait(5)      # 隐性等待。
browser.get("https://www.baidu.com/")
print(browser.title.find("大麦"))
time.sleep(2)
path = "//*[@id=\"download-pages\"]/div[2]/div/a/div"
target = browser.find_element_by_xpath(path)
# 鼠标操作
leftClick = webdriver.ActionChains(browser)
leftClick.move_to_element(target)
leftClick.click(target).perform()

# pyautogui.typewrite(['down', 'down', 'down', 'down'])  # 选中右键菜单中第2个选项
# time.sleep(5)
# pyautogui.typewrite(['enter'])  # 最后一个按键： mac电脑用的return，Windows应用enter
# time.sleep(5)

wait = WebDriverWait(browser,10)
wait.until(EC.presence_of_element_located((By.XPATH,path)))   # 等待直到这个元素加载完。

# wait = WebDriverWait(browser,5)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "grid")))   通过clas名定位“grid”元素,等他加载。
# soup = BeautifulSoup(browser.page_source,"html5lib")

# 判断文件下载是否完成 ,通过判断未完成文件后缀为.crdownload

global name
def file_name(path):
    for root, dirs, files in os.walk(path):
        name = files
    return name


while True:
    for oldname in name:
        file_type = oldname.split('.')[-1]
        if oldname != '' and file_type != 'crdownload':
            print('下载已完成')
            break
        else:
            print("等待下载。。。")
            time.sleep(10)
    break

browser.close()
# vd = soup.find(class_="toolbar")

# url = soup.find(soup.find('a',id='downloadita').get('href'))

# with requests.get(url,stream=True) as r:
#     with open("E://video//f.mp4",'wb') as f:
#         f.write(r.iter_content(1024))
#         f.close()


# https://www.ibilibili.com/video/av57278360/

# r = requests.get(str, verify=False,headers=headers)
# soup = BeautifulSoup(r.text,'html5lib')
#
# print(soup.find('a',id='downloadita').get('href'))


