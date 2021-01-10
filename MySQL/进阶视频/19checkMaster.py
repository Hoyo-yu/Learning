#!/usr/bin/python
import sys
import os
import pymysql

port = int(sys.argv[1])
var={}
conn=pymysql.connect(host='127.0.0.1',port=port,user='monitor',passwd='monitor')
cur=conn.cursor()
cur.execute("show global variables like \"%read_only%\"");
rows = cur.fetchall()

for r in rows:
    var[r[0]]=r[1]
if var['read_only']='OFF' and var['super_read_only']='OFF':
    print "mysql %d master instance" % port
else:
    print "mysql %d is readonly instance" % port

sys.exit(0)
cur.close()
conn.close()





