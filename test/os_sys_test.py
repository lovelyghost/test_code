# # -*- coding:utf-8 -*-

import os,sys

# python os模块的主要用法
#
# python中的os模块可以用来编写于平台无关的一些文件系统操作。
#
# 主要的方法如下：
# 一些标记属性
print(os.linesep) #文件中分割行的字符串
print(os.sep) #文件路径名的分隔符
print(os.curdir) #当前工作目录的字符串名称
print(os.pardir) #父目录字符串名称
# 常用方法
# os.remove()
# os.rename()
# for i in (os.walk("/Users/lx/uline")):
#     print(i)
# os.walk(top, topdown=True, onerror=None, followlinks=False)
# 可以得到一个三元tupple(dirpath, dirnames, filenames),
# 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
# dirpath 是一个string，代表目录的路径，
# dirnames 是一个list，包含了dirpath下所有子目录的名字。
# filenames 是一个list，包含了非目录文件的名字。


#获得当前工作目录
print (os.getcwd())

#——返回路径的目录和文件名。
print(os.path.split("/Users/lx/pagekite.py"))

#——获得文件的大小，如果为目录，返回0
print(os.path.getsize("/Users/lx/requirements.txt"))
#——获得绝对路径
print(os.path.abspath("."))

#——连接目录和文件名

print(os.path.join("/Users/lx/", "hhe.txt"))

#——返回文件名
print(os.path.basename("/Users/lx/hhe.txt"))
#——返回文件路径

print(os.path.dirname("/Users/lx/hhe.txt"))

#获得程序所在的实际目录
print(sys.argv)

# [root@ansheng ~]# cat scripts.py
#!/usr/bin/env python
# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# [root@ansheng ~]# python scripts.py canshu1 canshu2
# scripts.py
# canshu1
# canshu2

print (os.path.realpath(sys.argv[0]))
print (os.path.split(os.path.realpath(sys.argv[0])))
print (os.path.split(os.path.realpath(sys.argv[0]))[0])

#: 获取系统当前编码，一般默认为ascii。
print(sys.getdefaultencoding())
#获取当前文件夹所有的文件组成的列表
print(sys.path)
#获取返回Python解释器在当前系统中的绝对路径
print(sys.executable)
#获取平台信息
print(sys.platform)
#获取环境变量
print(os.environ)
print(os.getenv('USER'))
# 方法用于从一个命令打开一个管道。执行命令
os.popen("mkfile 1MB test_one.py")
