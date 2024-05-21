import random as rdm
#Variaveis globais
initial_state = []  #Lista para armazenar a matriz inicial
goal_state = [] #Lista para armazenar o estado objetivo

#Funções Auxiliares
    #Criação de nós
class Node:
    def __init__(self, no_pai, position):
        self.no_pai =  no_pai
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, prox):
        return self.position == prox.position
    
    def __repr__(self):
        return f"{self.position}\ng: {self.g}\nh: {self.h}\nf: {self.f}"

    def __lt__(self, prox):
        return self.f < prox.f
    
    def __gt__(self, prox):
        return self.f > prox.f
    

#Função que move o X dentro do grid
def move_X(position,direcao):
    n = len(position)
    nova_posicao = [row[:] for row in position]
    x, y = [(ix, iy) for ix, row in enumerate(position) for iy, i in enumerate(row) if i == 'X'][0]

    if direcao == "up" and x > 0:
        nova_posicao[x][y], nova_posicao[x - 1][y] = nova_posicao[x - 1][y],  nova_posicao[x][y]
    elif direcao == "down" and x < n - 1:
        nova_posicao[x][y], nova_posicao[x + 1][y] = nova_posicao[x + 1][y],  nova_posicao[x][y]
    elif direcao == "left" and y > 0:
        nova_posicao[x][y], nova_posicao[x][y - 1] = nova_posicao[x][y - 1],  nova_posicao[x][y]
    elif direcao == "right" and y < n - 1:
        nova_posicao[x][y], nova_posicao[x][y + 1] = nova_posicao[x][y + 1],  nova_posicao[x][y]
    else:
        return None

    return  nova_posicao

#função que vai calcular número de inversões para saber se o estado inicial consegue chegar no objetivo
def soluvel(grid, n):
    vetor = [num for row in grid for num in row if num != 'X']
    inversoes = 0

    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] > vetor[j]:
                inversoes += 1

    if n % 2 == 1:  #caso tamanho do grid seja ímpar
        return inversoes % 2 == 0
    else:
        x_linha = n - [linha.index("X") for linha in grid if "X" in linha][0]
        return (inversoes + x_linha) % 2 == 0

def grid(n): #Gera grid inicial e objetivo (grid organizado propiamente), um dos elementos é X
    number_list = list(range(1, n*n))
    number_list.append("X")

    global initial_state, goal_state
    #Se o estado inicial gerado não for solucionável, tenta gerar outro que seja
    while True:
        lista_temp = number_list.copy()
        rdm.shuffle(lista_temp)
        initial_state = []
        for i in range(n):
            linha = lista_temp[i * n:(i + 1) * n]
            initial_state.append(linha)

        if soluvel(initial_state, n):
            break

    goal_state = [number_list[i * n:(i + 1) * n] for i in range(n)]

    print("Estado inicial:\n" + str(initial_state))
    print("Estado objetivo:\n" + str(goal_state), "\n")
    return initial_state, goal_state