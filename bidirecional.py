import auxiliares as aux
import heapq 
import time
import pprint 

def custo_estimado(estado_atual:list, goal_state:list):
    h = 0
    n = len(estado_atual)
    for i in range(n):
        for j in range(n):
            if estado_atual[i][j] != 'X' and estado_atual[i][j] != goal_state[i][j]:
                h += 1
    return h


def intersec(lista_A_init, lista_A_final):
    for no in lista_A_init:
        for no_final in lista_A_final:
            if no.position == no_final.position:
                return no
    return None

def caminho(no_a_init, no_a_final):
    caminho_init = []
    caminho_final = []
    inicial = no_a_init
    final = no_a_final
    
    while inicial is not None:
        caminho_init.append(inicial.position)
        inicial = inicial.no_pai
        
    while final is not None:
        caminho_final.append(final.position)
        final = final.no_pai
    
    caminho_final.append(aux.goal_state)

    path = caminho_init + caminho_final[1:]
    pprint.pprint(caminho_final[::-1])
    pprint.pprint(caminho_init)
    
    return path


def bidirecional():
    #iniciar timer
    time_starter = time.perf_counter()

    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.g = 0
    no_inicial.h = custo_estimado(no_inicial.position, aux.goal_state)
    no_inicial.f = no_inicial.g + no_inicial.h

    no_final = aux.Node(None, aux.goal_state)
    no_final.g = 0
    no_final.h = custo_estimado(no_final.position, aux.initial_state)
    no_final.f = no_final.g + no_final.h

    lista_aberta_inicial = []
    lista_fechada_inicial = []

    heapq.heappush(lista_aberta_inicial, no_inicial)

    lista_aberta_final = []
    lista_fechada_final = []

    heapq.heappush(lista_aberta_final, no_final)
    iteracoes = 0
    nos_expandidos = 0 

    while lista_aberta_inicial and lista_aberta_final:
        iteracoes += 1

        common_node = intersec(lista_fechada_inicial, lista_fechada_final)
        if common_node:
            timer_finisher = time.perf_counter()
            print("SOLUÇÃO ENCONTRADA!")
            print("Quantidade de nós expandidos: ", nos_expandidos)
            print("Média de nós: ", nos_expandidos // iteracoes)
            print("Quantidade de passos: ", len(lista_fechada_inicial) + len(lista_fechada_final))
            print(f"Tempo de execução do algoritmo: {timer_finisher - time_starter:0.4f} segundos")
            return caminho(no_atual_inicial, common_node)
        
        if lista_aberta_inicial:
            no_atual_inicial = heapq.heappop(lista_aberta_inicial)
            lista_fechada_inicial.append(no_atual_inicial)
            print("RESTAM NA LISTA ABERTA INICIAL:", len(lista_aberta_inicial))
            print("Na lista fechada inicial: ", len(lista_fechada_inicial))
            sucessores_i = []

            for direcao in ["up", "down", "left", "right"]:
                    move = aux.move_X(no_atual_inicial.position, direcao)
                    if move:
                        pai = aux.Node(no_atual_inicial.no_pai, no_atual_inicial.position)
                        novo_no_i = aux.Node(pai, move)
                        sucessores_i.append(novo_no_i)
            for passo_i in sucessores_i:
                    if any(passo_i.position == fechado.position for fechado in lista_fechada_inicial):
                        continue

                    passo_i.g = no_atual_inicial.g + 1
                    passo_i.h = custo_estimado(passo_i.position, aux.goal_state)
                    passo_i.f = passo_i.g + passo_i.h

                    if any(passo_i.position == aberto.position and passo_i.g > aberto.g for aberto in lista_aberta_inicial):
                        continue
                    heapq.heappush(lista_aberta_inicial, passo_i)
                    nos_expandidos += 1

        if lista_aberta_final:
            no_atual_final = heapq.heappop(lista_aberta_final)
            lista_fechada_final.append(no_atual_final)
            nos_expandidos += 1
            print("RESTAM NA LISTA ABERTA FINAL:", len(lista_aberta_final))
            print("Na lista fechada final: ", len(lista_fechada_final))
            sucessores_f = []

            for direcao in ["up", "down", "left", "right"]:
                    move = aux.move_X(no_atual_final.position, direcao)
                    if move:
                        paif = aux.Node(no_atual_final.position, direcao)
                        novo_no_f = aux.Node(paif, move)
                        sucessores_f.append(novo_no_f)

            for passo_f in sucessores_f:
                    if any(passo_f.position == fechado.position for fechado in lista_fechada_final):
                        continue

                    passo_f.g = no_atual_final.g + 1
                    passo_f.h = custo_estimado(passo_f.position, aux.initial_state)
                    passo_f.f = passo_f.g + passo_f.h

                    if any(passo_f.position == aberto.position and passo_f.g > aberto.g for aberto in lista_aberta_final):
                        continue
                    heapq.heappush(lista_aberta_final, passo_f)
                    nos_expandidos += 1


    print("\nResposta nao encontrada")
    print("Quantidade de nos expandidos: ", nos_expandidos)
    print("\nMedia de nos: ", nos_expandidos+iteracoes//2)
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", nos_expandidos+iteracoes//2)
    print(f"Tempo de execução do algoritmo: {timer_finisher - time_starter:0.4f} segundos")

