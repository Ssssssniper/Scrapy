# coding=utf-8
"""
使用requests进行访问，设置代理IP。
下载wallpaper——https://wallhaven.cc/toplist?page=     数字代表几页的图片。
soup.select(""html head title)  可以逐层查找(CSS选择器)  返回是个列表
soup.select("head > title")   找到某tag下的直接子标签 该功能很强大，查资料
soup.select("#link1")   通过id查找
soup.select("a[href]")  通过是否存在该属性查找
"""
import requests
import random

proxy = [
    {
        'http': 'http://61.135.217.7:80',
        'https': 'http://61.135.217.7:80',
    },
{
        'http': 'http://118.114.77.47:8080',
        'https': 'http://118.114.77.47:8080',
    },
{
        'http': 'http://112.114.31.177:808',
        'https': 'http://112.114.31.177:808',
    },
{
        'http': 'http://183.159.92.117:18118',
        'https': 'http://183.159.92.117:18118',
    },
]
url = "https://wallhaven.cc/toplist?page="
number = input("请问您想要下载多少页的内容？")
real_url = url+number
# requests.post(url , data=) 传参 data= 可以是{}、json.dumps({})表单数据序列化
s = requests.Session()
r = s.get(real_url, verify=True) # headers=  params= 都是键值对形式{} verify = True 验证SSL证书
if r.status_code == 200:
    print("访问成功")
else:
    print("访问地址拒绝访问")
# print(r.cookies)
print(r.text)
