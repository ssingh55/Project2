#!/usr/bin/python

import cgi,cgitb
import MySQLdb as   sql
cgitb.enable()

print "content-type:text/html"
print ""

db=sql.connect("localhost","root","redhat","adhoc")
cur = db.cursor()
x=cur.execute("select password from add where email='%s' "%email)
if x.fetchall()!=0:
    print "<meta http-equiv=\"refresh\" content=\"0;url=http://example.com\">"




"""con.execute('insert into Login values("%s", "%s")' % \
             (user_id, password))"""
