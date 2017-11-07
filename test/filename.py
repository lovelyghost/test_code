# # -*- coding:utf-8 -*-

import os
#获取路径
print os.path.dirname('/Users/lx/Downloads/requirements.txt')
#分割文件名
print os.path.basename('/Users/lx/Downloads/requirements.txt')
#分割文件的后缀
print os.path.split('/Users/lx/Downloads/requirements.txt')
#创建目录
if not os.path.exists('/Users/lx/Downloads/happyday'):
    os.mkdir('/Users/lx/Downloads/happyday')

#列出当前目录下的所有文件和文件夹
print os.listdir('.')
#walk()会生成当前目录下的所有文件和目录
# print list(os.walk('/Users/lx/Downloads/uline/uline/handlers'))
#删除目录
os.rmdir('/Users/lx/Downloads/happyday')

#判断是否为文件
print os.path.isfile('/Users/lx/requirements.txt')
print os.path.isfile('/Users/lx/Downloads/happyday')

#判断是否为目录
print os.path.isdir('/Users/lx/Downloads/happyday')
#判断是否为符号link
# 在linux里面会有一些link的文件
print os.path.islink('link_file')

import webbrowser
webbrowser.open("http://v.youku.com/v_show/id_XNDc2NDk5OTI0.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0")