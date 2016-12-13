#!"C:\Users\Seth\AppData\Local\Programs\Python\Python36-32\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 3 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit:
#

# useful for debugging
import cgitb
import json
import os.path
cgitb.enable()


import cgi
form = cgi.FieldStorage()
def logins(name,pw):
	x=userCheck(name,"userdata.json")
	if(x=pw):
		print ('Login Success')
		return True
	else:
		print ('Login Failed')
		return False
def userCheck(name,datafile):
    res=dict()
    if os.path.exists(datafile) and not os.stat(datafile).st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
            if name in res:
                return res[name]
    else:
        return None
    return None
def addUserData(name,pw,datafile):
    res=dict()
    x=userCheck(name,datafile)
    if(x==None):
		if not os.path.exists(datafile):
			with open(datafile,"w") as f:
				pass
		if not os.stat(datafile).st_size == 0:
			with open(datafile,"r") as f:
				res=json.load(f)
				print(res)
		res[name]=pw
		with open(datafile,"w") as f:
			json.dump(res,f)

# prints a minimal HTTP header
print ('Content-Type: text/html')
print()

# print the HTTP body, which is the HTML file representing lecture1.html)

print ('<html>')
print ('	<head>')

print ('		<title>')

print ('''
			Project Seth and Jordan
		</title>

		<style type="text/css">
			h1 {
				font-size: 100px;
				font-family: arial;
			}

			img {
				width: 300px;
			}

			p#myLine {
				color: red;
			}
		</style>

	</head>
''')

print ('<body>')
print ('<h2>Your name is: ' + form['my_name'].value + '</h2>')

print ('<h2>Your Password is: ' + form['my_pw'].value + '</h2>')
val=logins(form['my_name'].value, form['my_pw'].value)
if(val==True):
	print ('<form method="post" action=".\cgi-bin\game.py">')
	print ('<input type="hidden" name="user" value="'+form['my_name'].value+'"/>')
	print ('<input type="hidden" name="cmd" value="cont"/>')
	print ('<input type="submit" value="Continue Game"/>')
else:
	print ('<form method="post" action=".\cgi-bin\game.py">')
	print ('<input type="hidden" name="user" value="'+form['my_name'].value+'"/>')
	print ('<input type="hidden" name="cmd" value="start"/>')
	print ('<input type="submit" value="Start New Game"/>')
	addUserData(form['my_name'].value, form['my_pw'].value,"userdata.json")
print ('''
	</body>
</html>''')
