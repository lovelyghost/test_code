#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
r = redis.StrictRedis(host='localhost',port=6379,db=1)
r.set("foo","bar")
print(r.get("foo"))
r.hmset("iamdict",{"name":"mengjia","name1":"wuguobin"})
print(r.hgetall("iamdict"))
print(r.hget("iamdict","name"))
pipe = r.pipeline()
pipe.set("hha","jja")
pipe.get("hha")

result = pipe.execute()
print(result)