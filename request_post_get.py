# coding=utf-8
import requests

'''
自动模拟 get请求和post请求
'''
url = "http://www.baidu.com"
urlload = {"key":"value","key2":"value2"}
requests.get(url,params=urlload)            # 向URL传递参数  params

payload = {'name':'userid','password':'12345'}
requests.post(url, data=payload)        # 表单 data

header = {'user-agent': 'my-app/0.0.1'}
requests.get(url,headers=header)        # 请求头  headers 伪装成浏览器 User-Agent
