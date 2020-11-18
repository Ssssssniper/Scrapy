# http://www.xs4.cc/so/?书名.html
# 分别适用了urllib和requests两种方式请求
# 成功  2019/7/3
from urllib import request
from urllib.request import urlopen
from urllib.parse import quote
import string
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests

target_url = "http://www.xs4.cc/so/?"
target_novel = input("请输入小说的完整名称：")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100'}

real_url = quote(target_url + target_novel + ".html", safe=string.printable)    # 转换下quote
request = request.Request(real_url, headers=headers)
ret = urlopen(request)  # 连接地址中不能出现中文
html = ret.read()
soup = BeautifulSoup(html, 'html5lib')
sousuoname = soup.find(class_='SoList')
# print(sousuoname)
# for child in sousuoname.h2.children:
#     print(child)
list_li = sousuoname.find_all('li')

Result = {}
wb = Workbook()
# ws1 = wb.create_sheet[0]('{}'.format("查询结果"))
ws1 = wb['Sheet']
ws1.title = "查询结果"

if list_li[0].string == "请搜索您喜欢的小说...":
    print("查无此书")
else:
    for novel in list_li:           # 可以用next_sibling获取并列子节点
        state = novel.find(class_='words').find(class_='state')
        introduce = novel.find(class_='words').find(class_='jianjie')
        address = novel.find(class_='words').find(class_='arcurl').find_all('a')  # find_all返回列表属性
        print("Author :", state.a.string)
        Result["Author"] = "".join(state.a.string)  # bs4.element.NavigableString 转换string
        print("Profile:", introduce.get_text())
        Result["Profile"] = introduce.get_text()
        print("阅读地址:", address[0]['href'])
        Result["阅读地址"] = address[0]['href']
        print("下载地址:", address[1]['href'])
        Result["下载地址"] = address[1]['href']
        ws1.append(["Author", "Profile", "阅读地址", "下载地址"])
        ws1.append([Result["Author"], Result["Profile"], Result["阅读地址"], Result["下载地址"]])
stop = input("是否下载该小说？Y/N")
if stop in ["Y","y"]:
    download = requests.get(Result["下载地址"]).content
    print("ok")
    with open(target_novel+".txt",'wb') as f:
        f.write(download)






