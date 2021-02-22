def caminho_hamiltoniano(grafo, size, ponto, path=[]):
    # print(f'Caminho hamiltoniano ligado ao ponto={ponto}, caminho={path}')
    if ponto not in set(path):
        path.append(ponto)
        if len(path) == size:
            return path
        # inicio do backtracking
        todos_candidatos = []
        for prox_ponto in grafo.get(ponto, []):
            res_path = [i for i in path]
            # print(res_path)
            candidatos = caminho_hamiltoniano(grafo, size, prox_ponto, res_path)
            if candidatos is not None:  # sai do loop ou termina caminho
                todos_candidatos.extend(candidatos)
                # print(todos_candidatos)
            else:
                # print(f'Caminho {path} termina')
                pass
        return todos_candidatos
    else:
        # print(f'Ponto {ponto} já está no caminho {path}')
        return None


if __name__ == '__main__':
    ponto = 1
    size = 7
    grafo = {1: [2, 6],
             2: [1, 3, 7],
             3: [2, 4, 7],
             4: [5],
             6: [1, 5, 7],
             7: [2, 3, 5, 6]}
    path = caminho_hamiltoniano(grafo, size, ponto)
    # print(path)  # retorna uma única lista com todos os pontos que formam os caminhos
    # Abaixo separo path em sublistas, cada uma é um caminho diferente gerado por caminho_hamiltoniano()
    lista_candidados = []
    for j in range(size):
        while j*size < len(path):
            start = int(j*size)
            end = int((j+1)*size)
            lista_candidados.append(path[start:end])
            break
    print(f'Os candidatos a ciclos hamiltonianos são: {lista_candidados}')

    # verificação se o caminho é um ciclo hamiltoniano
    if len(lista_candidados) == 0:
        print('Nesse grafo não há caminho hamiltoniano, logo, não há ciclo hamiltoniano')
    else:
        for candidato in lista_candidados:
            if ponto in grafo[candidato[0]]:
                print(f'O caminho {candidato} é um ciclo hamiltoniano')
            else:
                print(f'O caminho {candidato} não é um ciclo hamiltoniano')