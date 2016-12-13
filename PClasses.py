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
	def attack(p1,p2):
		offense = get_type(p1)
		defense = get_type(p2)
		if(offense == defense):
			return 1
		elif(offense == 'Grass' and defense == 'Fire' or offense == 'Fire' and offense == 'Water' or offense == 'Water' and offense == 'Grass'):
			return 0
		elif(offense == 'Grass' and defense == 'Water' or defense == 'Fire' and defense == 'Grass' or defense == 'Water' and defense == 'Fire'):
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
