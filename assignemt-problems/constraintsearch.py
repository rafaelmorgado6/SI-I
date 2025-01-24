
variables = [ 'q1', 'q2', 'q3', 'q4' ]

columns = [ 1,2,3,4 ]

domains = { v:columns for v in variables}

edges = { (v1,v2) for v1 in variables
                  for v2 in variables if v1 != v2 }

'''This function ensures two queens (Q1 and Q2) do not threaten each other'''
def queen_constraint( Q1,Col1,Q2,Col2 ):

    # Check vertical
    if Col1 == Col2:
        return False
    
    Row1 = int(Q1[1])   # 'q1' -> Q1[0]='q', Q1[1]='1'
    Row2 = int(Q2[1])   # 'q2' -> Q2[0]='q', Q2[1]='2'

    # Check diagonal
    if abs( Col1 - Col2 ) == abs( Row1-Row2 ):
        return False 
    
    return True

constraints = { e:queen_constraint for e in edges }

class ConstraintSearch:

    def __init__( self,domains,constraints ):
        self.domains = domains
        self.constraints = constraints
    
    def search( self,domains=None ):

        if domains == None:
            domains = self.domains

        #! one domain is empty: Fail
        if  any(domains[v] == [] for v in domains):
            return None

        #* all domains have a single value: Solution
        if all(len(domains[v]) == 1 for v in domains):
            # Ensure the solution is consistent
            solution = { v:domains[v][0] for v in domains}
            c = self.constraints
            if all(c[v1,v2](v1,solution[v1],v2,solution[v2]) for (v1,v2) in c):
                return solution
        
        #TODO otherwise: continue search
        for v in domains:
            if len(domains[v]) == 1:
                continue
            
            for x in domains[v]:
                newdomains = domains.copy()
                newdomains[v] = [x]
                edges = [e for e in self.constraints if e[1] == v]
                solution = self.search(newdomains)
                if solution is not None:
                    return solution
        return None

        def propagate(self,domains,edges):
            queue = edges[:]
            while queue != []:
                (v1,v2) = queue.pop(0)
                c = self.constraints[v1,v2]
                values = [x for x in domains[v1]
                          if any(c(v1,x,v2,y) for y in domains[v2])]
                if len(values) < len(domains[v1]):
                    edges2 = [e for e in self.constraints if e[1] == v1]
                    queue.extend(edges2)
                    domains[v1] == values
            
    
cs = ConstraintSearch( domains,constraints )
print(cs.search())




