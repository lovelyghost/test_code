# -*- coding:utf-8 -*-
#正则表达式
import re
#如果做大量的匹配和搜索最好先预编译
# # 将正则表达式编译成Pattern对象
# pattern = re.compile(r'hello')
#
# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match('hello world!')
#
# if match:
#     # 使用Match获得分组信息
#     print(match.group())
#
# ### 输出 ###
# # hello
#使用多个界定符分割字符串
# line = 'asd djuf  fdfr, daddd;seff,wdqew wew'
# print(re.split(r'[;,\s]\s*',line))
# print(re.split(r'(?:;|,|\s)\s*',line))
#
# #字符串开头或者结尾匹配
# #startswith endswith
# import os
# filenames = os.listdir('.')
# print(filenames)
# print([name for name in filenames if name.endswith(('.log','.txt'))])


#字符串匹配和搜索
# text = 'yeah but no , but yeah , but no ,fuck'
# print(text.startswith('yeah'))
# print(text.endswith('fuck'))
# print(text.find('fuck'))  #find方法找到匹配的位置
#
# text1 = "27/12/2017"
# text2 = 'nov 27,2017'
com = re.compile(r'\d+/\d+/\d+')
# print(re.match(r'\d+/\d+/\d+',text1))
# print(re.match(r'\d+/\d+/\d+',text2))
# print(com.match(text2))
# print(com.match(text1))
#
#
text3 = 'yeah but no 27/12/2017, but yeah , but 27/12/2017 no ,fuck'
print(com.findall(text3)) #find 找到具体的匹配信息

#正则捕获分组
com1 = re.compile(r'(\d+)/(\d+)/(\d+)')
print(com1.findall(text3))

#字符串替换

print(text3.replace('no','yes'))

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text3))

#忽略大小写的替换
text_U = 'yeah But no 27/12/2017, bUt yeah , buT 27/12/2017 no ,fuck'
print(re.findall('but',text_U,flags=re.IGNORECASE))
print(re.sub('but','fucks',text_U,flags=re.IGNORECASE))

#左对齐,右对齐,居中
print('hello'.ljust(20, '*'))
print('hello'.rjust(20, '*'))
print('hello'.center(20, '*'))

#字符串处理xml和html字符
import html
s = 'fuck the fucking world <tag>hhahh</tag>'
print(html.escape(s))

