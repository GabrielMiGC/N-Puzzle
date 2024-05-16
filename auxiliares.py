import random as rdm
#Variaveis globais
initial_state = []  # Lista para armazenar a matriz inicial
goal_state = [] #Lista para armazenar o estado objetivo

#Funções Auxiliares
    #Criação de nós
class Node:
    def __init__(self, no_pai= None, position=None):
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

def move_X(no_atual,direcao):
    """Para que a função funcionasse corretamente as listas de listas foram transformadas em
      uma única lista, facilitando a iteração e movimentação do X"""
    atual_state = []
    for face in no_atual:
        atual_state += face
    
    x = atual_state.index("X")
    colunas = len(no_atual[0])
    if direcao == "up" and x >= colunas:
        print("up")
        atual_state[x], atual_state[x-colunas] = atual_state[x-colunas], atual_state[x]
    if direcao == "down" and x < len(atual_state) - colunas:
        print("down")
        atual_state[x], atual_state[x+colunas] = atual_state[x+colunas], atual_state[x]
    if direcao == "left" and x % colunas != 0:
        print("left")
        atual_state[x], atual_state[x-1] = atual_state[x-1], atual_state[x]
    if direcao == "right" and (x + 1) % colunas != 0:
        print("right")
        atual_state[x], atual_state[x+1] = atual_state[x+1], atual_state[x]
    
    """Esse trecho irá ajudar a transformar a lista unica de volta na lista de listas"""
    matriz = []
    matriz = [atual_state[i:i+len(no_atual[0])] for i in range(0, len(atual_state), len(no_atual[0]))]
    
    return matriz


def grid(n): #Gera grid inicial e objetivo (grid organizado propiamente), um dos elementos é X
    number_list = list(range(1, n*n))
    number_list.append("X") # type: ignore
    goal_list = number_list.copy()

    global initial_state, goal_state
    
    
    for i in range(n):
        row = []
        for j in range(n):
            inside_number = rdm.choice(number_list)
            row.append(inside_number)
            number_list.remove(inside_number)  # Remove o número selecionado do conjunto
        initial_state.append(row)
    
    for index in range(n):
        row_goal = goal_list[index*n:(index+1)*n]
        goal_state.append(row_goal)



    print("Estado inicial:\n" + str(initial_state))
    print("Estado objetivo:\n" + str(goal_state), "\n")