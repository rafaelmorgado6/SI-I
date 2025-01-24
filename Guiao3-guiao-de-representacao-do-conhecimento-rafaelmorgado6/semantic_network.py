

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from collections import Counter
from statistics import mean
from functools import reduce

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
            str(self.entity2) + ")"
    def __repr__(self):
        return str(self)

# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

class AssocOne(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, e2)

class AssocNum(Relation): # Só aceita valores numericos para e2
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, float(e2))

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return str(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
    

    
    def list_associations(self):
        associations = [d.relation.name for d in self.declarations if isinstance(d.relation, Association)]
        return list(set(associations))

    def list_objects(self):
        objects = [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)]
        return list(set(objects))

    def list_users(self):
        users = [d.user for d in self.declarations]
        return list(set(users))

    def list_types(self):
        types = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, Member) or isinstance(d.relation, Subtype)]
        return list(set(types))
    
    def list_local_associations(self, entity):
        associations = [d.relation.name for d in self.declarations if isinstance(d.relation, Association) and d.relation.entity1 == entity]
        return list(set(associations))

    def list_relations_by_user(self, user):
        relations = [d.relation.name for d in self.declarations if (isinstance(d.relation, Association) or isinstance(d.relation, Member)) and d.user == user]
        return list(set(relations))

    def associations_by_user(self, user):
        associations = [d.relation.name for d in self.declarations if isinstance(d.relation, Association) and d.user == user]
        return len(list(set(associations)))
    
    def list_local_associations_by_entity(self, entity):
        associations = [(d.relation.name, d.user) for d in self.declarations if isinstance(d.relation, Association) and d.relation.entity1 == entity]
        return list(set(associations))

    def predecessor(self, pred, entity):
        parent = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]
        for p in parent:
            if p == pred:
                return True
            elif self.predecessor(pred, p):
                return True
        return False
    
    def predecessor_path(self, pred, entity):
        parent = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]
        for p in parent:
            if p == pred:
                return [pred, entity]
            path = self.predecessor_path(pred, p)
            if path != None and path[0] == pred:
                return path + [entity]
        return None

    def query(self, entity, association = ""):
        parent = [d.relation.entity2 for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity] 
        r = []
        for p in parent:
            r += self.query(p, association)
        
        return r + [d for d in self.declarations if d.relation.entity1 == entity and (association == "" or d.relation.name == association ) and not isinstance(d.relation, Subtype) and not isinstance(d.relation, Member)]

    def query2(self, entity, association = ""):
        parent = [d.relation.entity2 for d in self.declarations if d.relation.entity1 == entity and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype))]
        r = []
        for p in parent:
            r += self.query(p, association)
        
        return r + [d for d in self.declarations if d.relation.entity1 == entity and (association == "" or d.relation.name == association )]

    def query_cancel(self, entity, association):
        
        '''Esta condição verifica se existem declarações associadas à entity com o nome de relação igual a association.'''
        if any(d.relation.name == association for d in self.declarations if d.relation.entity1 == entity and isinstance(d.relation, Association)):
            # Retorna uma lista de todas as declarações diretamente associadas a entity com a associação especificada.
            return [d for d in self.declarations if d.relation.entity1 == entity and d.relation.name == association]

        # Constroi lista de ancestrais(entity2) de entity
        parent = [d.relation.entity2 for d in self.declarations if d.relation.entity1 == entity and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype))]
        
        r = []
        for p in parent:
            # p, chamamos query_cancel para verificar se p possui a associação 'association'
            r += self.query_cancel(p, association)
        
        return r

    def query_down(self, entity, association):

        # Encontra todas as entidades que têm entity como seu tipo superior ou ancestral,    
        sons = [d.relation.entity1 for d in self.declarations if d.relation.entity2 == entity and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype))]
        
        r = []
        for s in sons:
            # Para cada descendente direto s, o método chama recursivamente query_down
            #  para continuar a busca em um nível mais profundo na hierarquia.
            r += self.query_down(s, association)

            # Lista com todas as declarações que representam uma associação direta entre s e association
            r += [d for d in self.declarations if d.relation.entity1 == s and d.relation.name == association]

        return r

    
    def query_induce(self, entity, association):
        # Usar query_down para obter todas as associações dos descendentes
        sons = self.query_down(entity, association)

        # Extrair os valores associados (entidade 2 na relação) dos descendentes que possuem a associação
        values = [d.relation.entity2 for d in sons if d.relation.name == association]

        # Se não houver valores associados, retornar None
        if not values:
            return None
        
        # Contar a frequência de cada valor
        value_counts = Counter(values)
        
        # Retornar o valor mais frequente
        most_common_value, _ = value_counts.most_common(1)[0]
        return most_common_value

    def query_local_assoc(self, entity,relation=None):
        # obtem todas as declarações locais associadas à entidade entity para a relação relation
        local = self.query_local(e1=entity, rel=relation)

        for l in local:
            if isinstance(l.relation, AssocNum):
                # Cria uma lista contendo os valores(e2) de todas as declarações da relação AssocNum
                values = [d.relation.entity2 for d in local]
                return sum(values)/len(local)
            
            if isinstance(l.relation, AssocOne):
                # Cria uma lista dos valores e2, Counter para contar a frequência de cada valor e seleciona o valor mais frequente(val)
                val, count = Counter([d.relation.entity2 for d in local]).most_common(1)[0]
                return val, count/len(local)
            
            if isinstance(l.relation, Association):
                mc = []
                freq = 0

                for val, count in Counter([d.relation.entity2 for d in local]).most_common():
                    
                    # Armazena o Par (valor, frequência relativa)
                    mc.append((val, count/len(local)))
                    
                    # Acumula a Frequência Relativa
                    freq += count/len(local)
                    if freq > 0.75:
                        return mc
    
    def query_assoc_value(self, e2, assoc):
        local = self.query_local(e1=e2, rel=assoc)
        
        val_count = Counter([l.relation.entity2 for l in local]).most_common()
        
        if len(val_count) == 1:
            return val_count[0][0]
        
        decl = self.query(e1=e2, rel=assoc)
        
        val_count = Counter([d.relation.entity2 for d in local + decl]).most_common()
        print(val_count)        
        return val_count[0][0]