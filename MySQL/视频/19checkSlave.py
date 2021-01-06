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

cur = conn.cursor(pymysql.cursor.DictCursor)
cur.execute("show slave status")
slave_status = cur.fetchone()

if len(slave_status)<30:
    print "slave replication setup error";
    sys.exit(2)


if slave_status['Slave_IO_Running'] != 'Yes' or slave_status['Slave_SQL_Running'] != 'Yes':
    print "Replication error:replication from host=%s,port=%s,io_thread=%s,sql_thread=%s,error info %s %s" 
    % (slave_status['Master_Host'],slave_status['Master_Port'],slave_status['Slave_IO_Running'],slave_status['Slave_SQL_Running'],slave_status['Last_IO_Error'],slave_status['Last_SQL_Error'])
    sys.exit(1)
print slave_status

sys.exit(0)
cur.close()
conn.close()

