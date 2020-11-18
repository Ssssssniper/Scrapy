# coding=utf-8
import requests
import re

url = "https://www.csdn.net/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url,headers=headers)
pat_url = '<a href="(.*?://blog.csdn.net/[\S]*)"'
ret_url = re.compile(pat_url).findall(response.text)
print(ret_url)
