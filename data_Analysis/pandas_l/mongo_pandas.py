# -*- coding: utf-8 -*-
import pymongo
import pandas as pd
import numpy as np
import json

client = pymongo.MongoClient('localhost',27017)
db = client.project1
print(db)
collection = db.page
print(collection)
frame = pd.DataFrame(np.arange(16).reshape((4,4)),index=["a",'b',"c","d"],columns=["green","red","purple","yellow"])
print(frame)
frame_json = frame.to_json()
print(frame_json)
json_loads = json.loads(frame_json)
print(json_loads)
records = json_loads.values()
print(records)
collection.mydocument.insert(records)



# 读取 mongo 数据
cursor = collection['mydocument'].find()
mydata = pd.DataFrame(list(cursor))
del mydata["_id"]
print(mydata)