#pokemon = {}
#Rowlett, Snivy, Bulbasaur - Tackle, Leafage
#Litten, Tepig, Charmander - Tackle, Ember
#Popplio, Oshawott, Squirtle - Tackle, Water Gun
#20 HP
#4 damage, 8 if SE, 2 if NE
#Win by catching/defeating all Pokemon
#Capture: More likely at 25% HP, impossible at 100
#Pokemon only has type, all have 20 HP
#Getters and setters


class Pokemon: #Constructor only name, MaxHP - 20, currentHP
	def __init__(self, name, currentHP, element=None, maxHP=20):
		self.n = name
		self.mhp = maxHP
		self.chp = currentHP
		self.lmnt = element
	def get_type(self):
		if(self.n == 'Rowlett' or self.n == 'Bulbasaur' or self.n == 'Snivy'):
			self.lmnt = 'Grass'
		elif(self.n == 'Litten' or self.n == 'Charmander' or self.n == 'Tepig'):
			self.lmnt = 'Fire'
		elif(self.n == 'Popplio' or self.n == 'Squirtle' or self.n == 'Oshawott'):
			self.lmnt = 'Water'
	def attack(name1,name2):
		p1 = get_type(name1)
		p2 = get_type(name2)
		if(p1 == p2):
			return 1
		elif(p1 == 'Grass' and p2 == 'Fire' or p1 == 'Fire' and p2 == 'Water' or p1 == 'Water' and p2 == 'Grass'):
			return 0
		elif(p1 == 'Grass' and p2 == 'Water' or p1 == 'Fire' and p2 == 'Grass' or p1 == 'Water' and p2 == 'Fire'):
			return 2
		
class Attack: #Type (1: normal, 2: elemental), damage depending on type
	def __init__(self,special=False,element=None,damage=4):
		self.kind = special
		self.lmnt = element
		self.dmg = damage
	def is_special(self):
		if self.kind == False:
			self.lmnt = 'Normal'
		else:
			self.lmnt = 'Elemental'
