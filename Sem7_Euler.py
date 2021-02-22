## Versão Univesp
"""
    Caminho de Euler
"""
from random import randint


def gera_matriz(n):
    """
    Gera uma matriz booleana aleatória nₓn
    :param n: Tamanho do grafo (quantidade de vértices ou nós)
    :return: Matriz de tamanho n
    """
    geralLista = lambda x: [randint(0, 1) for i in range(x)]
    matriz = []
    for l in range(n):
        matriz.append(geralLista(n))
    return matriz


def iseuler(matrix):
    """
    Verifica se o grafo apresensenta caminho de Euler
    :param matrix: Matriz de adjacência do grafo
    :return: True/False para existência ou não de caminho de Euler
    """
    # Obtem a quantidade de nós do grafo:
    n = len(matrix)
    # Verifica se a matriz é válida
    qtdeNosImpares = 0
    if type(matrix) == list and len(matrix[0]) == n:
        for i in matrix:
            qtdeNosImpares += sum(i) % 2
            if qtdeNosImpares == 3:
                break
    else:
        return False
    return (qtdeNosImpares <= 2)

print('\n', str('>>> Matriz Aleatória <<<').center(80, '-'))
m = gera_matriz(randint(3, 20))
print('\nMatriz de adjacência: ', m)
print('Existe um caminho de Euler? ', iseuler(m))
print('\n', str('>>> Fim do programa iseuler <<<').center(80, '-'))

print('\n', str('>>> Matriz 5x5 conexa e SEM arcos paralelos com solução <<<').center(80, '-'))
m = [[0, 1, 1, 0, 1],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1],
     [1, 0, 0, 1, 0]]
print('\nMatriz de adjacência: ', m)
print('Existe um caminho de Euler? ', iseuler(m))

print('\n', str('>>> Matriz 5x5 conexa e COM arcos paralelos SEM solução <<<').center(80, '-'))
m = [[0, 2, 1, 0, 0],
     [2, 0, 1, 0, 0],
     [1, 1, 0, 1, 1],
     [0, 0, 1, 0, 2],
     [0, 0, 1, 2, 0]]
print('\nMatriz de adjacência: ', m)
print('Existe um caminho de Euler? ', iseuler(m))
print('\n', str('>>> Fim do programa iseuler <<<').center(80, '-'))


## Versão: https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
# Python program print Eulerian Trail in a given Eulerian or Semi-Eulerian Graph

from collections import defaultdict


# This class represents an undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # This function removes edge u-v from graph
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

            # A DFS based function to count reachable vertices from v

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:

        # 1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            ''' 
            2) If there are multiple adjacents, then u-v is not a bridge 
                Do following steps to check if u-v is a bridge 

            2.a) count of vertices reachable from u'''
            visited = [False] * (self.V)
            count1 = self.DFSCount(u, visited)

            '''2.b) Remove edge (u, v) and after removing the edge, count 
                vertices reachable from u'''
            self.rmvEdge(u, v)
            visited = [False] * (self.V)
            count2 = self.DFSCount(u, visited)

            # 2.c) Add the edge back to the graph
            self.addEdge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u):
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%d-%d " % (u, v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)

    '''The main function that print Eulerian Trail. It first finds an odd 
degree vertex (if there is any) and then calls printEulerUtil() 
to print the path '''

    def printEulerTour(self):
        # Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print("\n")
        self.printEulerUtil(u)

    # Create a graph given in the above diagram


g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour()

g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.printEulerTour()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(3, 2)
g3.addEdge(3, 1)
g3.addEdge(2, 4)
g3.printEulerTour()

# This code is contributed by Neelam Yadav
print('\nExercício 20: ')
g4 = Graph(4)
g4.addEdge(0, 1)
g4.addEdge(0, 2)
g4.addEdge(2, 0)
g4.addEdge(2, 1)
g4.addEdge(1, 2)
g4.addEdge(1, 3)
g4.addEdge(2, 3)
g4.addEdge(3, 1)

g4.printEulerTour()
