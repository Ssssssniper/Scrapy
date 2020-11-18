# coding=utf-8
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
"""
2019/7/12   B站排行榜视频下载。     完成
"""
# https://www.bilibili.com/v/anime/serial/#/all/default/0/1         1 :第几页。
# div class=vd-list-cnt  内含ul class= vd-list mod-2  ;  翻页 div class= pager pagination

def sort_file():
    save_dir = 'D:/软件安装包/'
    dir_lists = os.listdir(save_dir)
    if len(dir_lists)==0:
       return ""
    else:
        for name in dir_lists:
            if name.split(".")[-1] == "crdownload":
                print("下载进行中....")
        return True


"""①"""
def get_html(url,N):
    option = webdriver.ChromeOptions()
    option.add_argument("disable-infobars")  # 关闭自动检测提示
    option.add_argument("--disable-gpu")
    option.add_argument("--headless")
    browser = webdriver.Chrome('chromedriver', chrome_options=option)
    browser.implicitly_wait(5)  # 隐性等待。
    browser.get(url)      # 可设置成不显示界面
    soup = BeautifulSoup(browser.page_source)
    url_list = soup.find('ul',class_='rank-list').find_all('li')
    # 只要下载排名前N的视频
    list = url_list[:eval(N)]
    link = []
    for li in list:
        link.append(li.find('div',class_='info').select('a')[0].get('href'))        # ['','']
    browser.close()
    return link

"""②"""
# 获得下载目标地址 https://www.kanbilibili.com/video/av57728971/
def transfer_url(url_list):
    print("——开始转换目标url——")
    download_url = []
    for url in url_list:
        head = 'https:'
        index = url.index('bilibili')
        str1 = url[:index]
        str2 = url[index:]
        key = 'kan'
        download_url.append(head + str1 + key + str2)
    return download_url

"""③ download_url is a list"""
def download_video(download_url):
    # profile = {'download.default_directory': 'E://video'}
    option = webdriver.ChromeOptions()
    # option.add_experimental_option('prefs', profile)
    option.add_argument("disable-infobars")  # 关闭自动检测提示
    browser = webdriver.Chrome('chromedriver', chrome_options=option)
    browser.maximize_window()
    browser.implicitly_wait(5)  # 隐性等待。
    path = "//*[@id=\"download-pages\"]/div[2]/div/a/div"
    for i in download_url:
        browser.get(i)
        time.sleep(2)
        target = browser.find_element_by_xpath(path)
        WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,path)))
        # 鼠标操作
        leftClick = webdriver.ActionChains(browser)
        leftClick.move_to_element(target)
        leftClick.click(target).perform()
        print("————开始下载—————")
        browser.implicitly_wait(4)
        # 判断文件下载完成
        while sort_file():
            print("下载完成")
            break
    #         需要修改第一个下载完成后的内容
    browser.implicitly_wait(3)


if __name__ == '__main__':
    url = 'https://www.bilibili.com/ranking'
    path = 'E:/video'
    num = input("下载排行榜排名前多少的视频：")
    url_list = transfer_url(get_html(url,num))
    download_video(url_list)
