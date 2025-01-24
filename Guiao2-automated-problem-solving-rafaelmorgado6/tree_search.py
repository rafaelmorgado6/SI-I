#!/usr/bin/env python3
#
# Module: tree_search
#
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2020,
#  Inteligência Artificial, 2014-2023

from abc import ABC, abstractmethod

'''A classe SearchDomain serve para dizer às suas subclasses (como Cidades) quais funções 
elas devem implementar. Como ela é uma classe abstrata, ela define apenas a estrutura ou 
o contrato que todas as subclasses precisam seguir, sem fornecer uma implementação concreta.'''
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de ações possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma ação num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma ação num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado ao outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass



'''Problemas concretos a resolver dentro de um determinado dominio'''
class SearchProblem:
    def __init__(self, domain, initial, goal):  # (cidades_portugal,'Braga','Faro')
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)



''' Representação de um nó numa árvore de pesquisa. '''
class SearchNode:
    def __init__(self,state,parent, cost=0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = 0 if parent is None else parent.depth + 1
        self.heuristic = heuristic
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)



''' Árvore de pesquisa '''
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'):
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.solution = None
        self.non_terminals = 0
        self.terminals = 0
        self.highest_cost_nodes = []
        self.average_depth = 0

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None: # Se o nó atual não tem pai (é o nó raiz)
            return [node.state] # Retorna uma lista contendo apenas o estado do nó atual
        path = self.get_path(node.parent)  # Chamada recursiva para obter o caminho do pai
        path += [node.state]  # Adiciona o estado do nó atual à lista do caminho
        return(path) # Retorna a lista completa de estados


     # procurar a solucao
    def search(self, limit=None):
        while self.open_nodes != []:    # Enquanto houver nós abertos
            node = self.open_nodes.pop(0)   # Remove o primeiro nó da lista de nós abertos

            '''Verificação do Objetivo:'''
            if self.problem.goal_test(node.state): # Verifica se o estado do nó é o estado objetivo
                self.solution = node # Armazena a solução encontrada
                
                '''Nó mais caro:'''
                for i in reversed(self.open_nodes): # vai do ultimo nó aberto até ao primeiro devido aos nós estarem ordenados por custo
                    max_cost = self.open_nodes[-1].cost # max_cost = valor do custo do ultimo nó da lista
                    if i.cost < max_cost:   # i.cost -> custo do nó atual
                        break
                    self.highest_cost_nodes = [i] + self.highest_cost_nodes # adiciona nó i à lista
                
                self.terminals = len(self.open_nodes) + 1 #Contagem de nós terminais 
                self.average_depth = self.average_depth /(self.non_terminals + self.terminals) # Cálculo da prof. média apos objetivo
                return self.get_path(node) # Retorna o caminho para a solução
            
            '''Contagem de Não Terminais:'''
            self.non_terminals += 1
            
            '''Expansão de Nós:'''
            lnewnodes = []  # Lista para armazenar novos nós gerados pela expansão do nó atual

            for a in self.problem.domain.actions(node.state): # Vê ações possíveis a partir do estado do nó atual
                newstate = self.problem.domain.result(node.state,a) # Calcula o novo estado resultante da ação
                
                if newstate not in self.get_path(node) and (limit is None or node.depth < limit): # Verifica se o novo estado não faz parte do caminho já percorrido (para evitar ciclos) ou se é menor que o limite
                    added_cost = self.problem.domain.cost(node.state, (node.state,newstate)) # Retorna distância(custo) entre duas cidades
                    heuristic_value = self.problem.domain.heuristic(newstate, self.problem.goal) # Calcula a heurística
                    newnode = SearchNode(newstate,node,node.cost+added_cost, heuristic_value) # Cria um novo nó com o estado gerado e o nó atual como pai
                    self.average_depth += newnode.depth # A cada nó novo gerado, a profundidade desse nó é acrescentada
                    lnewnodes.append(newnode) # Adiciona o novo nó à lista de novos nós
            
            '''Adicionar Nós Novos:'''
            if lnewnodes:  # Se houver novos nós, adiciona à lista de nós abertos
                self.add_to_open(lnewnodes)
            else:  # Caso contrário, incrementa o contador de nós terminais
                self.terminals += 1
        return None 



    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth': #Novos nós serão adicionados ao final da lista, dando prioridade ao mais antigos(largura)
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':  #Novos nós serão adicionados ao inicio da lista, sendo processados primeiro(profundidade)
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform': # Nós com menos custo acumulado terão prioridade 
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda n: n.cost) 
        elif self.strategy == 'greedy': # Nós com menos heuristica (distância) acumulado terão prioridade
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda n: n.heuristic)
        elif self.strategy == 'a*': # Nós com menos (heuristica (distância) + custo) terão prioridade
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key=lambda n: n.heuristic + n.cost)

    @property 
    def length(self):
        return len(self.get_path(self.solution))-1

    @property
    def avg_branching(self):
        return (self.terminals + self.non_terminals -1) / self.non_terminals

    @property
    def cost(self):
        return self.solution.cost
