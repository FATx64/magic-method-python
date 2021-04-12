#magic method

class hero:

	def __init__ (self,name,jumlah):
		self.name = name
		self.jumlah = jumlah

	def __repr__ (self):
		return "Repr - Hero : {} , dengan Power = {}".format(self.name,self.jumlah)

	
	def __add__(self,objek):
		return self.jumlah + objek.jumlah

	@property
	def __dict__(self):
		return "hero ini mempunyai nama dan jumlah"

hero1 = hero("traveler",20)
hero2 = hero("klee",30)
print(hero1)
print(hero2)
print("jumlah power =",hero1 + hero2)
print(hero1.__dict__)