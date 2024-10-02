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

# Dominios de pesquisa
# Permitem calcular
# as ações possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent):
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth', limit=None):
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.solution = None
        self.limit = limit
        self.non_terminal_nodes_count = 0
        self.terminal_nodes_count = 0

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None: # Se o nó atual não tem pai (é o nó raiz)
            return [node.state] # Retorna uma lista contendo apenas o estado do nó atual
        path = self.get_path(node.parent)  # Chamada recursiva para obter o caminho do pai
        path += [node.state]  # Adiciona o estado do nó atual à lista do caminho
        return(path) # Retorna a lista completa de estados

    # procurar a solucao
    def search(self):
        while self.open_nodes != []:    # Enquanto houver nós abertos
            node = self.open_nodes.pop(0)   # Remove o primeiro nó da lista de nós abertos

            if self.problem.goal_test(node.state): # Verifica se o estado do nó é o estado objetivo
                self.solution = node # Armazena a solução encontrada
                self.terminal_nodes_count += 1
                return self.get_path(node), node.depth, self.length, self.terminal_nodes_count, self.non_terminal_nodes_count, self.avg_branching   # Retorna o caminho e a profundidade do nó

            if self.limit is None or node.depth < self.limit: # Se não houver limite de profundidade ou se a profundidade do nó atual for menor que o limite
                self.non_terminal_nodes_count += 1  # Incrementa o contador de nós não terminais,

                lnewnodes = []  # Lista para armazenar novos nós gerados pela expansão do nó atual

                for a in self.problem.domain.actions(node.state): # Para cada ação possível a partir do estado do nó atual
                    newstate = self.problem.domain.result(node.state,a) # Calcula o novo estado resultante da ação
                    if newstate not in self.get_path(node): # Verifica se o novo estado não faz parte do caminho já percorrido (para evitar ciclos)
                        newnode = SearchNode(newstate,node) # Cria um novo nó com o estado gerado e o nó atual como pai
                        lnewnodes.append(newnode) # Adiciona o novo nó à lista de novos nós

                if lnewnodes:  # Se houver novos nós, adiciona à lista de nós abertos
                    self.add_to_open(lnewnodes)
                else:  # Caso contrário, incrementa o contador de nós terminais
                    print("3")
                    self.terminal_nodes_count += 1
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            pass

    @property   # quando chamas a função nao precisas dos parentises (length() -> length)
    def length(self):
        """Retorna o comprimento da solução, que é o número de transições."""
        if self.solution is None:
            return 0
        return len(self.get_path(self.solution))-1

    @property
    def avg_branching(self):
        if self.non_terminal_nodes_count == 0:
            return 0  # Evita divisão por zero
            # Calcula o fator de ramificação médio
        return self.non_terminal_nodes_count / (self.length + 1)  # +1 para incluir a raiz no cálculo
