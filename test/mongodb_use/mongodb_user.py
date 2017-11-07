# -*- coding:utf-8 -*-
import pymongo
from pymongo import MongoClient
# client = MongoClient()

# //使用上面的代码片段，将建立连接到默认主机（localhost）和端口（27017）。您还可以指定主机和/或使用端口：

# client = MongoClient('localhost', 27017)

# //或者使用MongoURl格式：

client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test
# db = client['pymongo_test']
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1,post_2,post_3])
# print('One post: {0}'.format(result.inserted_id))

#检索文档
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)