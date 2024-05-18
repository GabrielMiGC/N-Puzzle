import bfs  # Importa o módulo bfs contendo as funções de busca

def main():
    puzzle_size = int(input('Defina o tamanho do puzzle: '))  # Solicita ao usuário o tamanho do puzzle
    puzzle = bfs.generate_grid(puzzle_size)  # Gera um puzzle embaralhado com o tamanho especificado
    
    print('Escolha um algoritmo para solucionar o problema:\n' +
          'Busca em largura = 1\nBusca em profundidade = 2\n' +
          'Busca A* com heurística de quantidade de peças erradas = 3\n' +
          'Busca A* com heurística de distância de Manhattan = 4\n' +
          'Busca Bidirecional com A* = 5\n')  # Imprime as opções de algoritmos de busca
    option = int(input('Algoritmo desejado: '))  # Solicita ao usuário a escolha do algoritmo

    if option == 1:
        initial_state = tuple(map(tuple, puzzle))  # Converte o puzzle inicial em uma tupla de tuplas
        goal = bfs.create_goal(puzzle_size)  # Cria o estado objetivo
        graph = bfs.build_graph(initial_state)  # Constrói o grafo a partir do estado inicial
        
        path, execution_time, mem_usage = bfs.bfs(graph, initial_state, goal)  # Executa a busca em largura (BFS) e obtém os resultados
        
        if path:
            print('\nSolução encontrada!')  # Imprime se a solução foi encontrada
            print(f'Caminho: {path}\n')  # Imprime o caminho da solução
        else:
            print('\nSolução não encontrada.\n')  # Imprime se a solução não foi encontrada

        print(f'Tempo de execução: {execution_time:.4f} segundos')  # Imprime o tempo de execução
        print(f'Uso de memória: {mem_usage:.2f} KB')  # Imprime o uso de memória

        total_nodes_explored = len(graph) + sum([len(neighbors) for neighbors in graph.values()])  # Calcula o total de nós explorados
        average_nodes_explored = total_nodes_explored / len(graph)  # Calcula a média de nós explorados
        print(f'Média de nós explorados: {average_nodes_explored:.2f}')  # Imprime a média de nós explorados

if __name__ == '__main__':
    main()  # Chama a função main para executar o programa