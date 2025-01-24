recompensas = { (c,l):-0.04 for c in [1,2,3,4] for l in [1,2,3] if (c,l) not in [(2,2),(4,2),(4,3)]}
recompensas[4,3] = 1
recompensas[4,2] = -1

def transitionprob(s1,action,s2):
    (dec,dl) = action
    if abs(dc) + abs(dl) != 1:
        return None
    (c1,l1) = s1
    (c2,l2) = s2 
    if abs(c2-c1) + abs(l2-l1) > 1:
        return 0.0 
    if c1+cl==c1 and l1+dl==l2:
        return 0.8
    if c2==c1-dc and l2==l1-dl:
        return 0.0

    # incompleto, casos junto a paredes nao estao tratados
    return 0.1

gama = 0.9
epsillon = 0.001

v = { s:0 for s in recompensas}
while true:
    u = dict(v)
    for s in v:
        best = None
        for a in actions:
            aux = sum(transitionprob(s,a,x)*u[x] for x in recompensas)
            best = aux if best==None or aux>best else best
        v[s] = recompensas[s] + gama*
    if abs(v[s]-u[s]) > delta:
        delta = abs(v[s]-u[s])
    if delta<epsilon*(1-gama)/gama
        break

print(u)


