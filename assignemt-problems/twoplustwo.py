'''
    T W O
  + T W 0
 ----------
   F O U R
'''
from constraintsearch import *

variables = ['T', 'W', 'O', 'F', 'U','R', ]

digits = list(range(10))

domains = {v:digits for v in variables}

domains['X1'] = [0,1]
domains['X2'] = [0,1]

# 2*O = R + 10*X1

domains['ORX1'] = [(o,r,x1) for o in domains['O']
                            for r in domains['R']
                            for x1 in domains['X1']
                            if 2*0 == r+10*x1]

# 2*W + X1 = U + 10*X2

domains['WX1UX2'] = [(w,x1,u,x2) for w in domains['W']
                             for u in domains['U']
                             for x1 in domains['X1']
                             for x2 in domains['X2']
                             if 2*w + x1 == u + 10*x2]                            

# 2*T + X2 = O + 10*F

domains['TX2OF'] = [(t,x2,o,f) for t in domains['T']
                               for x2 in domains['X2']
                               for o in domains['O']
                               for f in domains['F']
                               if 2*t + x2 == o + 10*f]                            


print(domains['ORX1'])
print(domains['WX1UX2'])
print(domains['TX2OF'])

constraints = {(v1,v2):(lambda w1,x1,w2,x2: x1 != x2)
               for v1 in domains for v2 in domains if v1 != v2}

constraint_0 = lambda v,x,tv,t: x==t[0]
constraint_1 = lambda v,x,tv,t: x==t[1]
constraint_2 = lambda v,x,tv,t: x==t[2]
constraint_3 = lambda v,x,tv,t: x==t[3]

constraints_aux =  {}

# 2*O = R + 10*X1
constraints_aux['O', 'ORX1'] = constraint_0
constraints_aux['R', 'ORX1'] = constraint_1
constraints_aux['X1', 'ORX1'] = constraint_2

# 2*W + X1 = U + 10*X2
constraints_aux['W', 'WX1UX2'] = constraint_0
constraints_aux['X1', 'WX1UX2'] = constraint_1
constraints_aux['U', 'WX1UX2'] = constraint_2
constraints_aux['X2', 'WX1UX2'] = constraint_3

# 2*T + X2 = O + 10*F
constraints_aux['T', 'TX2OF'] = constraint_0
constraints_aux['X2', 'TX2OF'] = constraint_1
constraints_aux['O', 'TX2OF'] = constraint_2
constraints_aux['F', 'TX2OF'] = constraint_3

constraints.update(constraints_aux)

constraints_rev = {(v,tv):(lambda tv,t,v,x: c(v,x,tv,t)) 
                   for ((v,tv),c) in constraints_aux.items()}

constraints.update(constraints_rev)

print(constraints)

cs = ConstraintSearch(domains,constraints)
print(cs.search())