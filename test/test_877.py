# # -*- coding:utf-8 -*-

from os import path

from sqlalchemy.engine.url import make_url

cur_dir = path.dirname(path.dirname(path.abspath(__file__)))

# 该环境给前端开发使用,因为我们的内网环境有数据库,避免了给前端开发者部署数据库的麻烦
# default port
portDFLT = 8888
server_port = str(portDFLT)

# debug
server_debug = True

sqlalchemy_uline_db = 'postgresql+psycopg2://uline:uline2015@127.0.0.1:5432/uline'
sqlalchemy_uline_trade_db = 'postgresql+psycopg2://uline:uline2015@127.0.0.1:5432/uline_trade'

uline_db = make_url(sqlalchemy_uline_db)
uline_trade_db = make_url(sqlalchemy_uline_trade_db)

pg_db, pg_host, pg_passwd, pg_port, pg_user = map(lambda x: getattr(uline_db, x),
                                                  ['database', 'host', 'password', 'port', 'username'])
pg_trade_db, pg_trade_host, pg_trade_passwd, pg_trade_port, pg_trade_user = map(lambda x: getattr(uline_trade_db, x),
                                                                                ['database', 'host', 'password', 'port',
                                                                                 'username'])