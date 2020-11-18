# coding=utf-8
import requests
import urllib.request
import re
'''
() 返回括号内的
'''
target_url = "https://read.douban.com/provider/all"
data = requests.get(target_url)
pat = '<div class="name">(.*?)</div>'
target = re.compile(pat).findall(data.content.decode('utf-8'))
with open("publisher.txt","w") as f:
    for i in range(0,len(target)):
        print(target[i])
        f.write(target[i]+"\n")
    f.close()

'''
用urllib.request

html = urllib.request.urlopen(target_url)
data = html.read().decode("utf-8")
print(html.info())

'''