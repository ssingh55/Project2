#!/usr/bin/python

import MySQLdb as   sql
import cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print ""

var=cgi.FieldStorage()
email=var.getvalue("email")
password=var.getvalue("password")
firstname=var.getvalue("firstname")
lastname=var.getvalue("lastname")


db=sql.connect("localhost","root","redhat","adhoc")
cur = db.cursor()
x=cur.execute("select password from ad where email='%s' "%email)
if cur.fetchall()!=0:
        cur.execute('insert into ad values("%s", "%s","%s","%s")' % \
             (email, password,firstname,lastname))
        db.commit()
else :
        print "already exists"


#print "<meta http-equiv=\"refresh\" content=\"0;url=http://example.com\">"
