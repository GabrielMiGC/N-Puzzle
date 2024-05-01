import random as rdm
import time
import heapq
#Variaveis globais
initial_state = []  # Lista para armazenar a matriz inicial
goal_state = [] #Lista para armazenar o estado objetivo

#Funções Auxiliares
    #Criação de nós
def create_node(no_pai = None, posicao = None):
    node = {
        "no_pai": no_pai,
        "posicao": posicao, #Posição se refere ao grid com posição do X modificado
        "g": 0,
        "h": 0,
        "f": 0
    }
    #Retornar caminho 
def caminho(no_atual):
    caminho = []
    atual = no_atual
    while atual != None:
        caminho.append(atual["posicao"])
        caminho = caminho["no_pai"]
    return caminho[::-1]

def no_maior_que(no_1, no_2):
    return no_1["f"] > no_2["f"]
def no_menor_que(no_1, no_2):
    return no_1["f"] > no_2["f"]

                        #TODO
#Função que move o X dentro do grid
"""
    Essa função deve primeiramente encontrar o X dentro do grid.
    Deve então checar os possiveis movimentos e comparar de acordo com a heuristica final ["f"]
    Deve escolher aquele que possui ["f"] maior
    Atualizar "posicao" do nó atual
"""
def grid(n): #Gera grid inicial e objetivo (grid organizado propiamente), um dos elementos é X
    number_list = list(range(1, n*n))
    number_list.append("X")
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
    print("Estado objetivo:\n" + str(goal_state))

def A_manhattan():
    #Algoritmo
    lista_aberta = []   #Lista de nós que ainda podem gerar nós_filho
    lista_fechada = []  #Lista de nós que não podem mais gerar filhos
    
    no_inicial = create_node(None, initial_state)
    no_inicial["g"] = no_inicial["h"] = no_inicial["f"] = 0
    no_final = create_node(None, goal_state)
    no_final["g"] = no_final["h"] = no_final["f"] = 0

    heapq.heapify(lista_aberta) #Organizar a lista aberta como um heap
    heapq.heappush(lista_aberta,no_inicial) #Insere no_inicial na lista aberta


    while len(lista_aberta) > 0:
        no_atual = heapq.heappop(lista_aberta)
        lista_fechada.append(no_atual)
        #Contar passos
        contador_passos = 0

        if no_atual == no_final:
            return caminho(no_atual)

        no_filho = []
    for filho in no_filho:
        if no_filho[filho] in lista_fechada:
            continue

    #Contar nós expandidos

    #Contar média de nós

    #Start timer
    timer_starter = time.perf_counter()


    #Finish timer
    timer_finisher = time.perf_counter()
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")

    
def main():
    puzzle_size = int(input("Defina o tamanho do puzzle:"))
    grid(puzzle_size)

    print("Escolha um algoritmo para solucionar o problema:\nBusca em profundidade = 1\nBusca em Profundidade Iterativa = 2\nBusca A* com heurística de quantidade de peças erradas\n"+
          "Busca A* com heurística de distância de Manhattan = 4\nBusca Bidirecional com A* = 5\n")
    option = int(input("Algoritmo desejado:"))

    if(option == 1):
        #Busca em largura
        # 
        #CODE
        #
        return 0 #provisório
    elif(option == 2):
        #Busca em Profundidade Iterativa
        # 
        #CODE
        #
        return 0 #provisório
    elif(option == 3):
        # A* (peças erradas)
        # 
        #CODE
        #
        return 0 #provisório
    elif(option == 4):
        # A*(Manhattan)
        A_manhattan()
    elif(option == 5):
        # Bidirecional A*
        # 
        #CODE
        #
        return 0 #provisório
    else:
        print("Comando invalido")
        return main()

if __name__ == "__main__":
    main()
