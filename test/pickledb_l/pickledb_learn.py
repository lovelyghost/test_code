# -*- coding:utf-8 -*-

import pickledb

db = pickledb.load('example.db', False)

db.set('key', 'fuck')
db.set('k',"ll")
gg = db.get('key')
print(db.get('kk'))
print(gg)
print(db.dump())