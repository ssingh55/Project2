#!/usr/bin/python

import MySQLdb as   sql

db=sql.connect("localhost","root","redhat","adhoc")
cur = db.cursor()
x=cur.execute("select password from add where email='%s' "%email)
if x.fetchall()!=0:
    print "<meta http-equiv=\"refresh\" content=\"0;url=http://example.com\">"




"""con.execute('insert into Login values("%s", "%s")' % \
             (user_id, password))"""
