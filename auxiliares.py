import random as rdm
#Variaveis globais
initial_state = []  #Lista para armazenar a matriz inicial
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
        print("se moveu pra cima")
        atual_state[x], atual_state[x-colunas] = atual_state[x-colunas], atual_state[x]
    if direcao == "down" and x < len(atual_state) - colunas:
        print("se moveu pra baixo")
        atual_state[x], atual_state[x+colunas] = atual_state[x+colunas], atual_state[x]
    if direcao == "se moveu pra esquerda" and x % colunas != 0:
        print("left")
        atual_state[x], atual_state[x-1] = atual_state[x-1], atual_state[x]
    if direcao == "right" and (x + 1) % colunas != 0:
        print("se moveu pra direita")
        atual_state[x], atual_state[x+1] = atual_state[x+1], atual_state[x]
    
    """Esse trecho irá ajudar a transformar a lista unica de volta na lista de listas"""
    matriz = []
    matriz = [atual_state[i:i+len(no_atual[0])] for i in range(0, len(atual_state), len(no_atual[0]))]
    
    return matriz

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
    

def grid(n): #Gera grid inicial e objetivo (grid organizado propiamente), um dos elementos é X
    number_list = list(range(1, n*n))
    number_list.append("X") # type: ignore
    goal_list = number_list.copy()

    global initial_state, goal_state

    for index in range(n):
        row_goal = goal_list[index*n:(index+1)*n]
        goal_state.append(row_goal)
    
    #Se o estado inicial gerado não for solucionável, tenta gerar outro que seja
    while True:
        lista_temp = number_list.copy()
        initial_state = []
        for i in range(n):
            linha = []
            for j in range(n):
                numero_ins = rdm.choice(lista_temp)
                linha.append(numero_ins)
                lista_temp.remove(numero_ins)
            initial_state.append(linha)
        if soluvel(initial_state, n):
            break
        

    print("Estado inicial:\n" + str(initial_state))
    print("Estado objetivo:\n" + str(goal_state), "\n")