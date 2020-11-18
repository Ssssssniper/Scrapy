# # coding=utf-8
# import re
# class cl1:
#     def __init__(self, name):
#         self.myname = name
#
#     def Hi(self):
#         print("hi~~{}".format(self.myname))
#
# a = cl1("Jack")
# a.Hi()
#
# '''继承与重载'''
#
# string = 'abc123aba'
# pat = "ab[ac]"
# pat2 = "ab[^cb]"        # 除了cd之外都可以进行匹配
# x = re.search(pat, string)
# print(x)
#
'''

进度条实现
'''
import sys
import time

# for i in range(31):
#     sys.stdout.write('\r')  #
#
#     sys.stdout.write("%s%% |%s" % (int(i / 30 * 100), int(i / 30 * 100) * '#'))
#
#     sys.stdout.flush()  # 强制刷新到屏幕
#
#     time.sleep(0.3)

# for i in range(100):
#     print("\r{}%".format(i),end="")
#     time.sleep(0.2)

'''
返回字符对应的十进制数——ASCII码十进制数
'''
string = 'k'
a = ord(string)
print(a)
