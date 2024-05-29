import manhattan as am
import auxiliares as aux
import Wrong_position as wp
import bidirecional as bi
import ProfundidadeIterativa as pi
import bfs 
import tracemalloc as trace
import pprint as pr

    
def main():
    puzzle_size = int(input("Defina o tamanho do puzzle:"))
    aux.grid(puzzle_size)
    solv = aux.soluvel(aux.initial_state, puzzle_size)
    print("Solucionavel? ", solv)

    print("Escolha um algoritmo para solucionar o problema:\nBusca em profundidade = 1\nBusca em Profundidade Iterativa = 2\nBusca A* com heurística de quantidade de peças erradas\n"+
          "Busca A* com heurística de distância de Manhattan = 4\nBusca Bidirecional com A* = 5\n")
    option = int(input("Algoritmo desejado:"))

    if(option == 1):
        #Busca em largura
        trace.start()
        puzzle = bfs.generate_grid(puzzle_size)
        initial_state = tuple(map(tuple, puzzle))
        graph = bfs.build_graph(initial_state)
        path, execution_time= bfs.bfs(graph, initial_state, aux.goal_state)  # Executa a busca em largura (BFS) e obtém os resultados
        if path:
            print('\nSolução encontrada!')  # Imprime se a solução foi encontrada
            print(f'Caminho: {path}\n')  # Imprime o caminho da solução
        else:
            print('\nSolução não encontrada.\n')  # Imprime se a solução não foi encontrada
        print(f'Tempo de execução: {execution_time:.4f} segundos')  # Imprime o tempo de execução
        total_nodes_explored = len(graph) + sum([len(neighbors) for neighbors in graph.values()])  # Calcula o total de nós explorados
        average_nodes_explored = total_nodes_explored / len(graph)  # Calcula a média de nós explorados
        print(f'Média de nós explorados: {average_nodes_explored:.2f}')

        snapshot = trace.take_snapshot()
        stats = snapshot.statistics('lineno')
        for stat in stats[:1]: #Exibe o pico de memória (linha que usou mais memória)
            pr.pprint(stat)
    elif(option == 2):
        #Busca em Profundidade Iterativa
        
        pi.Profundidade_Iterativa(0)
        snapshot = trace.take_snapshot()
        stats = snapshot.statistics('lineno')
        for stat in stats[:1]:#Exibe o pico de memória (linha que usou mais memória)
            pr.pprint(stat)
    elif(option == 3):
        # A* (peças erradas)
        trace.start()
        wp.A_wrong()
        snapshot = trace.take_snapshot()
        stats = snapshot.statistics('lineno')
        for stat in stats[:1]:#Exibe o pico de memória (linha que usou mais memória)
            pr.pprint(stat)
    elif(option == 4):
        # A*(Manhattan)
        trace.start()
        am.A_manhattan()
        snapshot = trace.take_snapshot()
        stats = snapshot.statistics('lineno')
        for stat in stats[:1]:#Exibe o pico de memória (linha que usou mais memória)
            pr.pprint(stat)
    elif(option == 5):
        # Bidirecional A*
        trace.start()
        bi.bidirecional()
        snapshot = trace.take_snapshot()
        stats = snapshot.statistics('lineno')
        for stat in stats[:1]: #Exibe o pico de memória (linha que usou mais memória)
            pr.pprint(stat)
    else:
        print("Comando invalido")
        return main()

if __name__ == "__main__":
    main()
