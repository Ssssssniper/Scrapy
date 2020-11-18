# coding=utf-8
import os
import time
import pickle
import winsound
import configparser
from time import sleep
from selenium import webdriver

"""
扫码登录方式
大麦网抢票
第一次需要人工，后续保存cookie自动化登录。
只需配置config文件的url，即可更改抢票目标
"""

config = configparser.RawConfigParser()         # 对ini文件的基础读取类
config.read("config.ini", encoding="utf-8")     # 读取配置文件
target_url = config.get("config", "url")        # 读取config段中url变量的值     str
ticket_number = config.get("config", "number")  # 读取config段中number变量的值

# 大麦网主页
damai_url = "https://www.damai.cn/"

class Concert(object):
    def __init__(self):
        self.status = 0
        self.login_method = 1

    def set_cookie(self):
        self.browser.get(damai_url)
        print("自动跳转中——————")
        login_xpath = "/html/body/div[2]/div/div[3]/div[1]/div[1]/span"
        login_btn = self.browser.find_element_by_xpath(login_xpath)
        # 鼠标操作 自动点击登录
        leftClick = webdriver.ActionChains(self.browser)
        leftClick.move_to_element(login_btn)
        leftClick.click(login_btn).perform()
        # ——————————
        # print("###请点击登录###")
        # while self.browser.title.find('大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！') != -1:   # 修改，直接自动化点击登录按钮跳转到大麦登录。
        #     sleep(1)
        # ——————————
        print("###请扫码登录###")
        while self.browser.title == '大麦登录':
            sleep(1)
        print("###扫码成功###")
        # get_cookies获取cookies  然后保存到cookies.pkl文件中。运用pickle.dump（）序列化存入目标文件
        pickle.dump(self.browser.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie保存成功###")
        self.browser.get(target_url)

    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            for cookie in cookies:
                cookie_dict = {
                    'domain': '.damai.cn',          # 域名
                    'name': cookie.get('name'),     # 名称
                    'value': cookie.get('value'),   # 内容
                    "expires": "",
                    'path': '/',
                    'httpOnly': False,
                    'HostOnly': False,
                    'Secure': False}
                self.browser.add_cookie(cookie_dict)
            print('###载入Cookie###')
        except Exception as e:
            print(e)

    def login(self):
        print('###请使用扫码登录###')
        # if self.login_method == 0:
        #     self.browser.get(login_url)
        #     print('###开始登录###')

        if self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                self.set_cookie()
            else:
                self.browser.get(target_url)
                self.get_cookie()

    def enter_concert(self):
        print('###进入大麦网中........###')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-infobars")  # 关闭自动检测提示
        self.options.add_argument('--log-level=3')      # 取消log信息
        #            INFO = 0,
        #            WARNING = 1,
        #            LOG_ERROR = 2,
        #            LOG_FATAL = 3
        #            default is 0
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.browser.maximize_window()
        self.login()
        self.browser.refresh()
        self.status = 2
        print("###登录成功###")

    def choose_ticket(self):
        if self.status == 2:
            self.num = 1        # delete
            print("=" * 30)
            print("###请手动进行日期及票价选择###")  # 手动选择票档 和 场次

            while self.browser.title.find('确认订单') == -1:         # browser.title.find("")对标题信息进行比对，返回0/-1
                buybutton = self.browser.find_element_by_class_name('buybtn').text
                if buybutton == "即将开抢":
                    self.status = 2
                    self.browser.get(target_url)     # 重新访问该网站。等于刷新
                    print('###抢票未开始，刷新等待开始###')
                    continue

                elif buybutton == "立即预定":
                    self.browser.find_element_by_class_name('buybtn').click()
                    self.status = 3
                    self.num = 1

                elif buybutton == "立即购买":
                    self.browser.find_element_by_class_name('buybtn').click()
                    self.status = 4

                elif buybutton == "选座购买":
                    self.browser.find_element_by_class_name('buybtn').click()
                    self.status = 5

                elif buybutton == "提交缺货登记":
                    print('###抢票失败，请手动提交缺货登记###')
                    break

                title = self.browser.title
                if title == "确认订单":
                    self.check_order()

                elif self.status == 5:
                    print("###请自行选择位置和票价###")
                    break

    def check_order(self):
        if self.status in [3, 4]:
            if(ticket_number == '1'):       # 购票数==1
                # 观演人checkbox勾选状态
                stat = self.browser.find_elements_by_xpath(
                            '//div[@id="confirmOrder_1"]/div[2]/div[2]/div[1]/div[1]/label/span/input')[
                            0]
                while(stat.get_attribute('aria-checked') == 'false'):
                    time.sleep(0.5)
                    stat = self.browser.find_elements_by_xpath(
                        '//div[@id="confirmOrder_1"]/div[2]/div[2]/div[1]/div[1]/label/span/input')[
                        0]
                    self.browser.find_elements_by_xpath(
                            '//div[@id="confirmOrder_1"]/div[2]/div[2]/div[1]/div[1]/label/span/input')[
                            0].click()
                    print("调试使用状态：{}".format(stat.get_attribute('aria-checked')))

            print('———————快快快———————')
            print('———————买买买———————')

            time.sleep(1)
            # //*[@id="confirmOrder_1"]/div[9]/button  同意以上协议并提交订单按钮
            self.browser.find_elements_by_xpath('//*[@id="confirmOrder_1"]/div[9]/button')[0].click()

    # def finish(self):
    #     self.browser.quit()


if __name__ == '__main__':
    con = Concert()
    con.enter_concert()
    con.choose_ticket()

    # 发出报警声，提醒付款
    duration = 10000
    freq = 600
    while(1):
        winsound.Beep(freq, duration)