# COM150 - Fundamentos matemáticos para computação

Conceitos de matemática discreta e de lógica para computação (lógica formal e lógica de predicados). Noção de complexidade. Técnicas de demonstração direta, demonstração por contraposição e demonstração por absurdo. Relaçaõ de recorrência, provas, indução matemática.
Uso da lógica formal em programação declarativa e na demonstração de correção de um algoritmo.
Relações e conceitos de teoria de grafos. Modelagem de problemas usando grafos. 

## Exercícios práticos:

Relacionei os exercícios realizados no 4º bimestre/2020 durante as aulas da disciplina COM150 do Curso de Bacharel de Ciência de Dados da Univesp. Abaixo segue uma breve descrição do problema de negócios e da solução em Python (o link direciona para o código):

1. [Relação de recorrência 1](Sem4_Recorrencia.py): Judith L Gersting (Seção 3.1). Exercícios diversos para estabelecer definições e obter soluções para relações recorrentes com uso de algoritmos recursivos.
2. [Relação de recorrência 2](Sem4_formula_fechada_2_ordem.py): Judith L Gersting (Seção 3.2). Criando uma seguência com 4 casos básicos. Fórmula fechada de segunda ordem.
3. [Relação binária com matrizes](Sem5_Matriz.py): criação da classe Matrix e implementação de operadores lógicos e aritméticos, diagonal principal e secundária, características (ordem, identidade, triangular superior, triangular inferior). Cálculo da matriz de acessibilidade para grafos a partir da matriz boolena  de adjacência.
4. [Conversor polonês ou "pré-ordem"](Sem6_infix_to_postfix.py): dada uma equação algébrica "em ordem" transformá-la em ordem polonesa ou "pré-ordem".
5. [Conversor polonês inverso ou "pós-ordem"](Sem6_toRpn.py): dada uma equação algébrica "em ordem" transformá-la em ordem polonesa inversa ou "pós-ordem".
6. [Conversor de expressão](Sem6_preprocessExpression.py): conversor gráfico de expressão para operadores booleandos entre "pré-ordem" e "pós-ordem" - infixToPostfix.
7. [Circuitos e caminhos em grafos](Sem7_Circuitos_e_caminhos.py): obter a mínima distância entre a origem e destino em um grafo direcionado com pesos em seus vértices.  
8. [Algoritmo de Dijkstra](Sem7_Dijkstra.py): obter o menor caminho entre dois vértices ponderados de um grafo, usando o algoritmo de Dijkstra.
9. [Caminho Hamiltonioano](Sem7_Hamiltoniano.py): obter todos os possíveis caminhos Hamiltonianos para um grafo a partir de um determinado vértice. Checar se existe um ciclo. Num caminho Hamiltoniano todos os vértices de um grafo devem ser visitados apenas uma única vez.
10. [Caminho de Euler](Sem7_Euler.py): verificar se um grafo possui um caminho de Euler. Obter o caminho de Euler. Num caminho de Euler todas as arestas de um grafo devem ser visitados apenas uma única vez.
11. [Algoritmo de Warshall](Sem7_Warshall.py): dado um grafo _G_ com _n_ nós, o algoritmo de _Warshall_ deve calcular uma sequência de _n + 1_ matrizes de acessibilidades M<sub>0</sub>, M<sub>1</sub>, M<sub>2</sub>, …, M<sub>n</sub>.
