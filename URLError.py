# coding=utf-8
import urllib.request
import urllib.error

try:
    pass
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)