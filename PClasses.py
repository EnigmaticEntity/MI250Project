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
	def __init__(self, name, currentHP, element, maxHP=20):
		self.n = name
		self.mhp = maxHP
		self.chp = currentHP
		self.lmnt = element
		
class Attack: #Type (1: normal, 2: elemental), damage depending on type
	def __init__(self,name,element=None,damage=4):
		self.n = name
		self.lmnt = element
		self.dmg = damage
	def get_type(self):
		if self.n == 'Tackle':
			self.lmnt = 'Normal'
		elif self.n == 'Leafage':
			self.lmnt = 'Grass'
		elif self.n == 'Ember':
			self.lmnt = 'Fire'
		elif self.n == 'Water Gun':
			self.lmnt = 'Water'
		else:
			return("Invalid move")
