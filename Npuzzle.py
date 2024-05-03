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
        "g": 0, #Custo do movimento até agora
        "h": 0, #Quão proximo do objetivo está
        "f": 0  #Soma de h e g
    }
    return node
#Retornar caminho 
def caminho(no_atual):
    caminho = []
    caminho.append(no_atual["no_pai"])
    return caminho[::-1]

#Função que compara cada elemento/posição do estado atual com as do estado objetivo e retorna um valor h de acordo com o quao parecida estão
def custo_estimado(estado_atual:list, goal_state:list):
    """Para que a função funcionasse corretamente as listas de listas foram transformadas em
      uma única lista, facilitando a iteração e comparação dos elementos"""
    atual_state = []
    objetivo = []
    for face in estado_atual:
        atual_state += face
    for face in goal_state:
        objetivo += face
    """print(atual_state, "\n", objetivo)"""

    """O resto da divisão entre a posição dos elementos em cada lista é subtraido da sua
    posição e esse resultado é seu valor heurístico"""
    h = 0
    for i in range(len(atual_state)):
        quociente, resto = divmod(objetivo.index(atual_state[i]), len(atual_state))
        h += abs(i - resto)
    """print(range(len(atual_state)), resto)
    print(h)"""
    return h


#Função que move o X dentro do grid
def move_X(no_atual,direcao):
    for i in range(len(no_atual)):
        for j in range(len(no_atual[i])):
            if no_atual[i][j] == "X":
                return i, j
    if direcao == "up" and i > 0:
        no_atual[i][j], no_atual[i-1][j] = no_atual[i-1][j], no_atual[i][j]
    if direcao == "down" and i < len(no_atual["posicao"]) - 1:
        no_atual[i][j], no_atual[i+1][j] == no_atual[i+1][j], no_atual[i][j]
    if direcao == "left" and j > 0:
        no_atual[i][j], no_atual[i][j-1] = no_atual[i][j-1], no_atual[i][j]
    if direcao == "right" and j < len(no_atual["posicao"]) -1:
        no_atual[i][j], no_atual[i][j+1] = no_atual[i][j+1], no_atual[i][j]



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
    print("Estado objetivo:\n" + str(goal_state), "\n")

def A_manhattan():
     #Start timer
    timer_starter = time.perf_counter()

    #Algoritmo
    lista_aberta = []   #Lista de nós que ainda podem gerar nós_filho
    lista_fechada = []  #Lista de nós que não podem mais gerar filhos

    no_inicial = create_node(None, initial_state)

    no_inicial["h"] = custo_estimado(no_inicial["posicao"], goal_state)
    no_inicial["f"] = no_inicial["h"] + no_inicial["g"]

    no_final = create_node(None, goal_state)
    no_final["h"] = custo_estimado(no_final["posicao"], goal_state)
    no_final["f"] = no_final["g"] + no_final["h"]

    no_atual =create_node(None, initial_state)


    lista_aberta.append(no_inicial)


    #for debug purpose
    print("\n","#"*10, "\n")
    print(lista_aberta)
    print("#"*10, "\n")


    while len(lista_aberta) > 0:
        print("Entrou no laço while")

        no_atual = lista_aberta[0]
        lista_fechada.append(no_atual)
    
        if no_atual == no_final:
            return caminho(no_atual)

        no_filho = []
        for filho in no_filho:
            if filho["posicao"] in lista_fechada:
                continue
            filho["g"] = no_atual["g"] + 1
            filho["h"] = custo_estimado(filho["posicao"], goal_state)
            filho["f"] = filho["g"] + filho["h"]

            #heapq.heappush(lista_aberta, filho)

        #Toma decisão de qual direção escoher baseado na heurística, quanto menor o valor de h, mais próximo do estado objetivo
        for direcao in ["up", "down", "left", "right"]:
            prox_passo = create_node(None, None)
            prox_passo["posicao"], prox_passo["g"] = no_atual["posicao"], no_atual["g"]
            move_X(prox_passo["posicao"], direcao)
            prox_passo["g"] += 1 #Aumenta numero de passos dados
            prox_passo["h"] = custo_estimado(prox_passo["posicao"], goal_state)
            no_atual["h"] = custo_estimado(no_atual["posicao"], goal_state)
            prox_passo["f"] = prox_passo["g"] + prox_passo["h"]
            no_atual["f"] = no_atual["g"] + no_atual["h"]
            if prox_passo["f"] < no_atual["f"]:
                prox_passo["no_pai"] = no_atual
                no_atual = prox_passo
                print(no_atual["posicao"])

    #for debug purpose
    print("\n","#"*10, "\n")
    print(no_inicial)
    print("#"*10, "\n")
    print(no_atual)
    print("#"*10, "\n")
    print(no_final)
    print("#"*10, "\n")
    
    #Contar nós expandidos

    #Contar média de nós

    #Finish timer
    timer_finisher = time.perf_counter()
    print(caminho)
    print("Quantidade de passos: ", no_atual["g"])
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
