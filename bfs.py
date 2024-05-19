from collections import deque  # Importa deque da coleção para manipulação de filas
from random import shuffle  # Importa shuffle para embaralhar listas
import time  # Importa o módulo time para medir o tempo de execução

#função que vai calcular número de inversões para saber se o estado inicial consegue chegar no objetivo
def soluvel(grid, n):
    vetor = [num for row in grid for num in row if num != 'X']
    inversoes = 0

    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] > vetor[j]:
                inversoes += 1

    if n % 2 == 1: #caso tamanho do grid seja impar
        return inversoes % 2 == 0
    else:
        x_linha =  n - [linha.index("X") for linha in grid if "X" in linha][0]
        return (inversoes + x_linha) % 2 ==0
    
def generate_grid(n):
    while True:
        generated_grid = [[str(i + 1 + j * n) for i in range(n)] for j in range(n)]  # Cria uma grade inicial numerada
        generated_grid[-1][-1] = 'X'  # Substitui o último elemento por 'X' representando o espaço vazio
        
        flat_grid = [item for sublist in generated_grid for item in sublist]  # Achata a grade em uma lista única
        shuffle(flat_grid)  # Embaralha a lista achatada
        
        index = 0
        for row in range(n):
            for col in range(n):
                generated_grid[row][col] = flat_grid[index]  # Preenche a grade com a lista embaralhada
                index += 1
        if soluvel(generated_grid, n):
            break
        
    for row in generated_grid:
        print(' '.join(map(str, row)))  # Imprime a grade embaralhada
    print('Puzzle:\n' + str(generated_grid))  # Imprime a grade como lista de listas
        
    return generated_grid  # Retorna a grade gerada

def create_goal(n):
    goal = [[str(i + 1 + j * n) for i in range(n)] for j in range(n)]  # Cria a grade de objetivo numerada
    goal[-1][-1] = 'X'  # Substitui o último elemento por 'X'
    return tuple(map(tuple, goal))  # Retorna a grade de objetivo como tupla de tuplas

def generate_neighbors(state):
    neighbors = []  # Inicializa a lista de vizinhos
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Lista de movimentos possíveis (direita, esquerda, baixo, cima)
    
    # Encontra a posição do 'X'
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 'X':
                x, y = i, j  # Armazena a posição de 'X'
                break
    
    # Gera novos estados baseados em movimentos válidos
    for move in moves:
        new_position = (x + move[0], y + move[1])  # Calcula a nova posição após o movimento
        if 0 <= new_position[0] < len(state) and 0 <= new_position[1] < len(state[0]):
            new_state = [list(row) for row in state]  # Cria uma cópia do estado atual
            # Troca os valores da posição atual com a nova posição
            new_state[x][y], new_state[new_position[0]][new_position[1]] = new_state[new_position[0]][new_position[1]], new_state[x][y]
            new_state_tuple = tuple(map(tuple, new_state))  # Converte o novo estado em tupla de tuplas
            neighbors.append((new_state_tuple, move))  # Adiciona o novo estado e o movimento à lista de vizinhos
    
    
    
    return neighbors  # Retorna a lista de vizinhos

def build_graph(initial_state):
    graph = {}  # Inicializa o grafo
    queue = deque([initial_state])  # Cria uma fila com o estado inicial
    visited = set()  # Inicializa o conjunto de estados visitados

    while queue:
        current_state = queue.popleft()  # Remove o primeiro estado da fila
        if current_state not in visited:
            visited.add(current_state)  # Marca o estado como visitado
            neighbors = generate_neighbors(current_state)  # Gera os vizinhos do estado atual
            graph[current_state] = neighbors  # Adiciona o estado e seus vizinhos ao grafo
            for neighbor, _ in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)  # Adiciona o vizinho não visitado à fila
                    
    return graph  # Retorna o grafo construído


def bfs(graph, start, goal):
    visited = set()  # Inicializa o conjunto de estados visitados
    queue = deque([(start, [])])  # Cria uma fila com o estado inicial e o caminho vazio
    
    start_time = time.time()  # Registra o tempo de início

    while queue:
        state, path = queue.popleft()  # Remove o primeiro estado da fila
        if state not in visited:
            visited.add(state)  # Marca o estado como visitado
            print('\nPasso:', state)  # Adicionalmente imprime o estado atual
            if state == goal:
                end_time = time.time()  # Registra o tempo de fim
                
                return path, (end_time - start_time),   # Retorna o caminho, tempo de execução e uso de memória
            if state in graph:
                for next_state, action in graph[state]:
                    queue.append((next_state, path + [action]))  # Adiciona o próximo estado e o caminho atualizado à fila
    
    end_time = time.time()  # Registra o tempo de fim
    return None, (end_time - start_time) # Retorna None se a solução não for encontrada, tempo de execução e uso de memória