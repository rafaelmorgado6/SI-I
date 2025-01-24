from constraintsearch import *


def queens():
    variables = ["q1","q2","q3","q4"]

    columns = [1,2,3,4]

    domains = {v:columns for v in variables}

    edges = { (v1,v2)for v1 in variables 
                    for v2 in variables if v1 != v2 }
    
    def queen_constraint(Q1,C1,Q2,C2):
        if C1 == C2:
            return False
        R1 = int(Q1[1])
        R2 = int(Q2[1])
        if abs(C1 - C2) == abs(R1 - R2):
            return False
        return True

    constraints = { e:queen_constraint for e in edges } # stores the function 
    
    cs = ConstraintSearch(domains,constraints)
    print(cs.search())

def colormapA():

    variables = ["a","b","c","d","e"]

    colors = ["red","blue","green","yellow","white"]

    domains = {v:colors for v in variables}

    edges = [ ("e",v) for v in variables if v != "e"]
    edges += [("a","b"),("b","c"),("c","d"),("d","a")]
    edges += [(v2,v1) for (v1,v2) in edges]
    
    constraint = lambda v1,x1,v2,x2: x1!=x2

    constraints = { e:constraint for e in edges } # stores the function 
    
    cs = ConstraintSearch(domains,constraints)
    print(cs.search())

def amigos():

    variables = ["Andre","Bernardo","Claudio"]

    bike = variables #["Andre","Bernardo","Claudio"]
    hat = variables #["Andre","Bernardo","Claudio"]

    domains = {v:[(b,h) for b in bike if b != v for h in hat if h != v and h != b] for v in variables} #if v != "Andre"}
    #domains["Andre"] =[("Bernardo","Claudio")]

    edges = [ (v1,v2) for v1 in variables  for v2 in variables if v1 != v2]

    constraint = lambda v1,x1,v2,x2: x1[0]!=x2[0] and x1[1]!=x2[1] and (x1[0] != "Bernardo" or x1[1] == "Claudio")

    constraints = { e:constraint for e in edges } # stores the function 
    
    cs = ConstraintSearch(domains,constraints)
    print(cs.search())

amigos()