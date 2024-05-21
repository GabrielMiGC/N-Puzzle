import time
import heapq
import auxiliares as aux

#Função que compara cada elemento/posição do estado atual com as do estado objetivo e retorna um valor h de acordo com o quao parecida estão
def custo_estimado(estado_atual:list, goal_state:list):
    h = 0
    n = len(estado_atual)
    goal_map = {value: (i, j) for i, row in enumerate(goal_state) for j, value in enumerate(row)}
    for i in range(n):
        for j in range(n):
            if estado_atual[i][j] != 'X':
                goal_x, goal_y = goal_map[estado_atual[i][j]]
                h += abs(i - goal_x) + abs(j - goal_y)
    return h

def caminho(no_atual):
    caminhof = []
    atual = no_atual
    
    while atual is not None:
        
        caminhof.append(no_atual.position)
        print(atual.position)
        atual = atual.no_pai
    return caminhof

def A_manhattan():
    #iniciar timer
    timer_starter = time.perf_counter()


    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.h = custo_estimado(no_inicial.position, aux.goal_state)
    no_inicial.f = no_inicial.g + no_inicial.h

    lista_aberta = []
    lista_fechada = []
    
    heapq.heappush(lista_aberta, no_inicial)

    #Nao rodar infinitamente
    iterations = 0
    nos_expandidos = 0
    max_iteracoes = (len(aux.initial_state) ** len(aux.initial_state) ** len(aux.initial_state)*1.5)

    while lista_aberta:
        iterations += 1
 
        if iterations > max_iteracoes:
            print("Iteracoes demais, cancelando busca!\n")
            timer_finisher = time.perf_counter()
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("\nMedia de nos: ", nos_expandidos+iterations//2)
            print("Quantidade de passos: ", len(lista_fechada))
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            break
        
        no_atual = heapq.heappop(lista_aberta)
        print(no_atual)
        nos_expandidos += 1
        lista_fechada.append(no_atual)
        print("RESTAM NA LISTA ABERTA:", len(lista_aberta))
        print("NA LISTA FECHADA:",len(lista_fechada))
        
        if no_atual.position == aux.goal_state:
            print("Solução encontrada")
            timer_finisher = time.perf_counter()
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("Quantidade de passos: ", len(lista_fechada))
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            return caminho(no_atual)

        
        sucessores = []
        for direcao in ["up", "down", "left", "right"]:
            move = aux.move_X(no_atual.position, direcao)
            if move:
                pai = aux.Node(no_atual.no_pai,no_atual.position)
                novo_no = aux.Node(pai, move)

                sucessores.append(novo_no)

        for passo in sucessores:
            if any(passo == fechado for fechado in lista_fechada):
                continue

            passo.g = no_atual.g + 1
            passo.h = custo_estimado(passo.position, aux.goal_state)
            passo.f = passo.g + passo.h


            if any(passo.position == aberto.position and passo.g > aberto.g for aberto in lista_aberta):
                continue

            heapq.heappush(lista_aberta, passo)

    print("Algoritmo não encontrou resposta")
    print("Quantidade de nos expandidos: ", nos_expandidos)
    print("Media de nos: ", nos_expandidos+iterations//2)
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", len(lista_fechada))
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
