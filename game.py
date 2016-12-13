import cgitb
import json
import os.path
import random
cgitb.enable()

import sys
import cgi
form = cgi.FieldStorage()
if form.getvalue('user'):
   users = form.getvalue('user')
if form.getvalue('balls'):
   balls = form.getvalue('balls')
if form.getvalue('cmd'):
   cmd = form.getvalue('cmd')
if form.getvalue('yourPokemon'):
   yourPokemon = form.getvalue('yourPokemon')
if form.getvalue('enemPokemon'):
   enemPokemon = form.getvalue('enemPokemon')
if form.getvalue('yourHp'):
   yourHp = form.getvalue('yourHp')
if form.getvalue('enemHp'):
   enemHp = form.getvalue('enemHp')
if form.getvalue("St1"):
   saveUser("bulbasaur",20)
   yourPokemon="bulbasaur"
   cmd="trainingS"
if form.getvalue("St2"):
   saveUser("squirtle",20)
   yourPokemon="squirtle"
   cmd="trainingS"
if form.getvalue("St3"):
   saveUser("charmander",20)
   yourPokemon="charmander"
   cmd="trainingS"
if form.getvalue("switch"):
   cmd="switch"
if form.getvalue("Atack1"):
   enemHp-=4
   types=1
if form.getvalue("Atack2"):
	types=2
	x=attatck(yourPokemon,enemPokemon)
	if x==1:
		enemHp-=4
	if x==2:
		enemHp-=8
	if x==0:
		enemHp-=2
if form.getvalue("1"):
	count=0
	for key, value in d.iteritems():
		if count==1:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("0"):
	count=0
	for key, value in d.iteritems():
		if count==0:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("2"):
	count=0
	for key, value in d.iteritems():
		if count==2:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("3"):
	count=0
	for key, value in d.iteritems():
		if count==3:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("4"):
	count=0
	for key, value in d.iteritems():
		if count==4:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("5"):
	count=0
	for key, value in d.iteritems():
		if count==6:
			if yourHp>0:
				saveUser(yourPokemon,yourHp)
			yourPokemon=key
			yourHp=value
		count+=1
if form.getvalue("Quit"):
	saveUser(yourPokemon,yourHp)
	cmd="save"
if form.getvalue("catch"):
	cmd="catch"
	if balls>0:
		x=random.randint(0,100)
		x+=(20-enemHp)
		if(x>50):
			saveUser(enemPokemon,enemHp)
			x=loadpokemonEM()
			enemPokemon=random.choice(x.keys())
			enemHp=x.[enemPokemon]
			catches=true
# prints a minimal HTTP header
print ('Content-Type: text/html')
print()

# print the HTTP body, which is the HTML file representing lecture1.html)

print ('<html>')
print ('	<head>')

print ('		<title>')

print ('''
			Game
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
def loadpokemonEM():
    res=dict()
    if os.path.exists("Pokemon.json") and not os.stat("Pokemon.json").st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
        return res;
    return None
def deletePerson(name):
    res=dict()
    datafile=form['my_name'].value+".json"
    if os.path.exists(datafile) and not os.stat(datafile).st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
            res.pop(name, None)
        with open(datafile,"w") as f:
            json.dump(res,f)
def saveUser(name,hp):
    res=dict()
    datafile=form['my_name'].value+".json"
    if not os.path.exists(datafile):
        with open(datafile,"w") as f:
            pass
    if not os.stat(datafile).st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
            print(res)
    res[name]=hp
    with open(datafile,"w") as f:
        json.dump(res,f)
def loadUsersP():
    res=dict()
    datafile=form['my_name'].value+".json"
    if os.path.exists(datafile) and not os.stat(datafile).st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
        return res;
    return None       
def loadHP(name,hp):
    res=dict()
    if os.path.exists("Pokemon.json") and not os.stat("Pokemon.json").st_size == 0:
        with open(datafile,"r") as f:
            res=json.load(f)
			if name in res:
                return res[name]
    return 0
def lose(name,hp):
    res=dict()
    datafile=form['my_name'].value+".json"
    if os.path.exists(datafile) and not os.stat(datafile).st_size == 0:
        return True
    return False
print ('<body>')
print ('<h2>Your name is: ' + form['my_name'].value + '</h2>')

if cmd=="switch":
	p=loadUsersP()
	lens=len(p)
	print('<form method="POST" action=".\cgi-bin\game.py">')
	count=0
	for key in d:
		print key, 'corresponds to', d[key]
		print ('<input type="submit" name="'+str(count)+'" value="'+key+'"/>')
		count+=1
	print ('</form>')
	cmd=="training"
if cmd=="catch":
	if(catches==true):
		print ('<h2>You caught the Pokemon</h2>')
	else if(balls<1):
		print ('<h2>You have no balls</h2>')
	else:
		print ('<h2>They broke free</h2>')
	cmd=="training"
if cmd=="trainingS":
	x=loadpokemonEM()
	enemPokemon=random.choice(x.keys())
	enemHp=x.[enemPokemon]
	print ('<h2>You run into a ' + enemPokemon+ '</h2>')
	print ('''
	<form method="POST" action=".\cgi-bin\game.py">
		<input type="submit" name="Atack1" value="Atack1"/>
		<input type="submit"  name="Attack2" value="Atack2"/>
		<input type="submit"  name="Catch" value="catch"/>
		<input type="submit"  name="switch" value="switch"/>
		<input type="submit"  name="Quit" value="Quit"/>
	</form>''')
if cmd=="training":
	if enemHp<1:
		print ('<h2>'+enemPokemon+' has fainted</h2>')
		x=loadpokemonEM()
		enemPokemon=random.choice(x.keys())
		enemHp=x.[enemPokemon]
		print ('<h2>You run into a ' + enemPokemon+ '</h2>')
	else:
		yourHp-=2
		x=attatck(yourPokemon,enemPokemon)
		if x==1:
			enemHp-=4
		if x==2 and types==2:
			print ('<h2>IT WAS SUPER EFFECTIVE</h2>')
		if x==0 and types==2:
			print ('<h2>it was not very effective</h2>')
		if yourHp<1:
			deletePerson(yourPokemon)
			if lose():
				print ('<h2>All your Pokemon are dead you loseHp</h2>')
				print ('''</body></html>''')
				sys.exit(0)
			else:
				print ('<h2>You must chose a new Pokemon</h2>')
		else:	
			print ('<h2>Your enemy has ' + enemHp+ 'Hp</h2>')
			print ('<h2>Your '+yourPokemon+' has ' + yourHp+ 'Hp</h2>')
	print ('''
	<form method="POST" action=".\cgi-bin\game.py">
		<input type="submit" name="Atack1" value="Atack1"/>
		<input type="submit"  name="Attack2" value="Atack2"/>
		<input type="submit"  name="Catch" value="satch"/>
		<input type="submit"  name="switch" value="switch"/>
		<input type="submit"  name="Quit" value="Quit"/>
	</form>''')
if cmd=="start":
	x=loadpokemonEM()
	y=random.choice(x.keys())
	enemey=pokemon(y)
	balls=5
	print ('<h2>Which pokemon would you like to start with?</h2>')
	print ('''
	<form method="POST" action=".\cgi-bin\game.py">
		<input type="submit" value="St1" name="bulbasaur"/>
		<input type="submit" value="St2" name="squirtle"/>
		<input type="submit" value="St3" name="charmander"/>
	</form>''')
if cmd=="quit":
	print ('<h2>Thanks for palying your data was saved</h2>')
print ('<input type="hidden" name="user" value="'+user+'"/>')
print ('<input type="hidden" name="yourPokemon" value="'+yourPokemon+'"/>')
print ('<input type="hidden" name="enemPokemon" value="'+enemPokemon+'"/>')
print ('<input type="hidden" name="yourHp" value="'+yourHp+'"/>')
print ('<input type="hidden" name="enemHp" value="'+enemHp+'"/>')
print ('<input type="hidden" name="cmd" value="'+cmd+'"/>')
print ('<input type="hidden" name="balls" value="'+balls+'"/>')
print ('''
	</body>
</html>''')
