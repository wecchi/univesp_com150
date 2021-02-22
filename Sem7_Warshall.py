"""
    Algoritmo de Warshall
    Para um grafo G com n nós, o algoritmo de Warshall calcula uma sequência de n + 1 matrizes M0, M1, M2, …, Mn.
    Para cada k, 0 ≤ k ≤ n, Mk[i, j] = 1 se e somente se existir um caminho em G de ni para nj cujos nós interiores
    (ou seja, nós que não são extremidades do caminho) pertencem apenas ao conjunto de nós {n1, n2, …, nk}:
    1.Todos os nós interiores pertencem a {n1, n2, …, nk}, e, nesse caso, Mk[i, j] = 1.
    Portanto, devemos repetir, em Mk+1, todos os elementos que são iguais a 1 em Mk.
    2.O nó nk+1 é um nó interior. Podemos supor que o nó nk+1 aparece apenas uma vez como nó interior, já que os
    ciclos podem ser eliminados do caminho. Então, tem que existir um caminho de ni para nk+1 cujos nós interiores
    pertencem a {n1, n2, …, nk} e um caminho de nk+1 para nj cujos nós interiores pertencem a {n1, n2, …, nk}.
    Isso significa que Mk[i, k + 1] = 1 e Mk[k + 1, j] = 1, ou seja, Mk[i, k + 1] Mk[k + 1, j] = 1

    GERSTING. Fundamentos Matemáticos para a Ciência da Computação. São Paulo: Grupo GEN, 2016. 9788521633303.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521633303/. Acesso em: 22 Nov 2020
"""
## Versão 1.0 Algoritmo de Warshall
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


def warshall(matrix):
    """
    Retorna a Matriz de acessibiliade, usando algoritmo de Warshall
    :param matrix: Matriz booleana de adjacência A
    :return: matriz de acessibilidade R
    """
    # Obtem a quantidade de nós do grafo:
    n = len(matrix)
    if type(matrix) == list and len(matrix[0]) == n:
        # Cria uma matriz vazia de n elementos
        m = matrix  # [[i * 0 for i in range(n)] for j in range(n)]
        for k in range(-1, n - 1):
            for i in range(0, n):
                for j in range(0, n):
                    m[i][j] = (m[i][j] or (m[i][k + 1] and m[k + 1][j]))
        return m
    else:
        return n


print('\n', str('>>> Início do programa warshall: Matriz informada <<<').center(80, '-'))
m1 = [[0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [1, 0, 0, 1, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0]]
print('Matriz de adjacência: ', m1)
print('Matriz de acessibilidade:\n', warshall(m1))

# m2 = [[0, 1, 1, 0],
#       [0, 0, 0, 0],
#       [0, 0, 1, 0],
#       [1, 1, 1, 0]]
# print('Matriz de adjacência: ', m2)
# print('Matriz de acessibilidade:\n', warshall(m2))
#
# m3 = gera_matriz(randint(3, 20))
# print('\nMatriz de adjacência: ', m3)
# print('Matriz de acessibilidade:\n', warshall(m3))
# print('\n', str('>>> Fim do programa warshall <<<').center(80, '-'))
