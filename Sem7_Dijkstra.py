"""
    Código original: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
    Author: Maria Boldyreva 10 de jul. de 2018

    O algoritmo
        1- Marque todos os nós não visitados e armazene-os.
        2- Defina a distância como zero para nosso nó inicial e infinito para outros nós.
        3- Selecione o nó não visitado com a menor distância, é o nó atual agora.
        4- Encontre vizinhos não visitados para o nó atual e calcule suas distâncias através do nó atual. Compare a
        distância recém-calculada com a atribuída e salve a menor. Por exemplo, se o nó A tem uma distância de 6, e a
        aresta AB tem comprimento 2, então a distância de B a A será 6 + 2 = 8. Se B foi previamente marcado com uma
        distância maior que 8, altere a 8.
        5-Marque o nó atual como visitado e remova-o do conjunto não visitado.
        6-Pare, se o nó de destino foi visitado (ao planejar uma rota entre dois nós específicos) ou se a menor
        distância entre os nós não visitados é infinita. Caso contrário, repita as etapas 3-6.
"""


from collections import deque, namedtuple

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)

        distance_between_nodes = 0
        for index in range(1, len(path)):
            for thing in self.edges:
                if thing.start == path[index - 1] and thing.end == path[index]:
                    distance_between_nodes += thing.cost
        path = list(path)
        info = {"D({}→{}) = {}".format(source, dest, distance_between_nodes): path}
        return info, distance_between_nodes, path

graph = Graph([
    ("a", "c", 2), ("a", "e", 5), ("b", "a", 8), ("b", "c", 10), ("b", "d", 15),
    ("c", "d", 9), ("c", "e", 6), ("d", "b", 7), ("e", "b", 4)])

print(graph.dijkstra("d", "e"))
