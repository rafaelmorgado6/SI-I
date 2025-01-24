#!/usr/bin/env python3
#
# Module: cidades
#
# Implements a SearchDomain for find paths between cities
# using the tree_search module
#
# (c) Luis Seabra Lopes
# Introducao a Inteligencia Artificial, 2012-2020
# Inteligência Artificial, 2014-2023
#

from math import sqrt
from tree_search import *

class Cidades(SearchDomain): # Cidades herda as funções abstratas de SearchDomain

    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates

    '''Retorna as ações possíveis (cidades conectadas) a partir de uma cidade dada.'''
    def actions(self,city):
        actlist = []
        #C1,C2,D percorrem os valores das connections -> (C1='Coimbra',C2='Leiria',D=73)
        for (C1,C2,D) in self.connections: 
            if C1==city: # se C1 é cidade, C2 é o destino, adiciona (C1,C2) à lista
                actlist += [(C1,C2)]
            elif C2==city: # se C2 é cidade, C1 é o destino, adiciona (C2,C1) à lista
               actlist += [(C2,C1)]
        return actlist

    '''Retorna a cidade resultante da aplicação de uma ação a partir de uma cidade.'''
    def result(self,city,action):
        (C1,C2) = action
        if C1==city:
            return C2

    '''Calcula o custo da ação (distância entre as cidades).'''
    def cost(self, city, action):
        (C1,C2) = action
        for connection in self.connections: # Vê a lista de connections ('Coimbra', 'Leiria', 73),...
            if(connection[0]==C1 and connection[1]==C2) or (connection[0]==C2 and connection[1]==C1):
                return connection[2]
        return None

    '''Fornece uma estimativa do custo restante para chegar a um objetivo (city->goal_city)'''
    def heuristic(self, city, goal_city):
        # Obter as coordenadas das cidades
        x_city, y_city = self.coordinates[city]                # 'Braga': ( 61, 317),
        x_goal_city, y_goal_city = self.coordinates[goal_city] #  'Faro': (120, -250),

        x_d = x_goal_city - x_city
        y_d = y_goal_city - y_city

        return sqrt((x_d)**2 + (y_d)**2)
    
    '''Verifica se a cidade atual é a cidade objetivo.'''    
    def satisfies(self, city, goal_city):
        return goal_city==city  # Caso sejam iguais retorna TRUE


cidades_portugal = Cidades(#SearchDomain)
                    # Ligacoes por estrada
                    [
                      ('Coimbra', 'Leiria', 73),
                      ('Aveiro', 'Agueda', 35),
                      ('Porto', 'Agueda', 79),
                      ('Agueda', 'Coimbra', 45),
                      ('Viseu', 'Agueda', 78),
                      ('Aveiro', 'Porto', 78),
                      ('Aveiro', 'Coimbra', 65),
                      ('Figueira', 'Aveiro', 77),
                      ('Braga', 'Porto', 57),
                      ('Viseu', 'Guarda', 75),
                      ('Viseu', 'Coimbra', 91),
                      ('Figueira', 'Coimbra', 52),
                      ('Leiria', 'Castelo Branco', 169),
                      ('Figueira', 'Leiria', 62),
                      ('Leiria', 'Santarem', 78),
                      ('Santarem', 'Lisboa', 82),
                      ('Santarem', 'Castelo Branco', 160),
                      ('Castelo Branco', 'Viseu', 174),
                      ('Santarem', 'Evora', 122),
                      ('Lisboa', 'Evora', 132),
                      ('Evora', 'Beja', 105),
                      ('Lisboa', 'Beja', 178),
                      ('Faro', 'Beja', 147),
                      # extra
                      ('Braga', 'Guimaraes', 25),
                      ('Porto', 'Guimaraes', 44),
                      ('Guarda', 'Covilha', 46),
                      ('Viseu', 'Covilha', 57),
                      ('Castelo Branco', 'Covilha', 62),
                      ('Guarda', 'Castelo Branco', 96),
                      ('Lamego','Guimaraes', 88),
                      ('Lamego','Viseu', 47),
                      ('Lamego','Guarda', 64),
                      ('Portalegre','Castelo Branco', 64),
                      ('Portalegre','Santarem', 157),
                      ('Portalegre','Evora', 194) ],

                    # City coordinates
                     { 'Aveiro': (41,215),
                       'Figueira': ( 24, 161),
                       'Coimbra': ( 60, 167),
                       'Agueda': ( 58, 208),
                       'Viseu': ( 104, 217),
                       'Braga': ( 61, 317),
                       'Porto': ( 45, 272),
                       'Lisboa': ( 0, 0),
                       'Santarem': ( 38, 59),
                       'Leiria': ( 28, 115),
                       'Castelo Branco': ( 140, 124),
                       'Guarda': ( 159, 204),
                       'Evora': (120, -10),
                       'Beja': (125, -110),
                       'Faro': (120, -250),
                       #extra
                       'Guimaraes': ( 71, 300),
                       'Covilha': ( 130, 175),
                       'Lamego' : (125,250),
                       'Portalegre': (130,170) }
                     )



'''Criando um problema de busca entre Braga e Faro'''
p = SearchProblem(cidades_portugal,'Braga','Faro')
t = SearchTree(p,'uniform') # depth / breadth / uniform / greedy / a*

print(t.search())


# Atalho para obter caminho de c1 para c2 usando strategy:
def search_path(c1,c2,strategy):
    my_prob = SearchProblem(cidades_portugal,c1,c2)
    my_tree = SearchTree(my_prob)
    my_tree.strategy = strategy
    return my_tree.search()
