class BayesNet:
	
	def __init__(self):
		self.probabilities = {}
	
	
	def insert(self, var, mothers, prob):
		if var not in self.probabilities:
			self.probabilities[var] = {}
		self.probabilities[var][mothers] = prob
			

	def jointProb(self,conjunction):
		prod = 1
		for var in self.probabilities:
			for mothers in self.probabilities[var]:
				if all(x in conjunction for x in mothers):
					prob = self.probabilities[var][mothers]
					if (var,False) in conjunction:
						prob = 1-prob
					prod *=  prob
		return prod
		

bn = BayesNet()
bn.insert('t',(),0.002)
bn.insert('r',(),0.001)

bn.insert('a',(('r',True),('t',True)),0.95)
bn.insert('a',(('r',True),('t',False)),0.94)
bn.insert('a',(('r',False),('t',True)),0.29)
bn.insert('a',(('r',False),('t',False)),0.001)

bn.insert('m',(('a',True),),0.70)
bn.insert('m',(('a',False),),0.10)

bn.insert('j',(('a',True),),0.90)
bn.insert('j',(('a',False),),0.05)
		
# P(j & m & a & ~r & ~t)
conjunction = ('j',True),('m',True),('a',True),('r',False),('t',False)

print(bn.jointProb(conjunction))