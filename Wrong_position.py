import auxiliares as aux
import heapq
import time
import pprint

def calculo_heuristica(estado_atual, estado_obj):
    h = 0
    atual_state = []
    objetivo = []
    for face in estado_atual:
        atual_state += face
    for face in estado_obj:
        objetivo += face

    for i in range(len(atual_state)):
        if atual_state[i] != objetivo[i]:
            h += 1
    return h

def caminho(no_atual):
    caminhof = []
    atual = no_atual
    while atual is not None:
        caminhof.append(atual.position)
        atual = atual.no_pai
    return caminhof[::-1]


def A_wrong():
    #iniciar timer
    timer_starter = time.perf_counter()

    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.g = no_inicial.h = no_inicial.f = 0
    no_final = aux.Node(None, aux.goal_state)
    no_final.g = no_final.h = no_final.f = 0

    lista_aberta = []
    lista_fechada = []
    sucessores = []

    heapq.heapify(lista_aberta)
    heapq.heappush(lista_aberta, no_inicial)

    #Nao rodar infinitamente
    iterations = 0
    nos_expandidos = 0
    max_iteracoes = (len(aux.initial_state) ** len(aux.initial_state) ** len(aux.initial_state) * 1.5)

    while len(lista_aberta) > 0:
        iterations += 1

        if iterations > max_iteracoes:
            print("Iteracoes demais, cancelando busca!\n")
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("Media de nos: ", nos_expandidos//iterations)
            timer_finisher = time.perf_counter()
            print("Quantidade de passos: ", len(lista_fechada))
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            return caminho(no_atual)
        
        no_atual = heapq.heappop(lista_aberta)
        print("RESTAM NA LISTA ABERTA:", len(lista_aberta))
        print("NA LISTA FECHADA:",len(lista_fechada))
        nos_expandidos += 1
        lista_fechada.append(no_atual)

        if no_atual.position == aux.goal_state:
            #Contar nós expandidos
            print("Quantidade de nos expandidos: ", nos_expandidos)
            #Contar média de nós
            print("\nMedia de nos: ", nos_expandidos+iterations//2)
            #Finish timer
            timer_finisher = time.perf_counter()
            print("Quantidade de passos: ", iterations)
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            return caminho(no_atual)

        
        for direcao in ["up", "down", "left", "right"]:
            
            move = aux.move_X(no_atual.position, direcao)
            pprint.pprint(no_atual)
            novo_no = aux.Node(no_atual, move)
            sucessores.append(novo_no)

        for passo in sucessores:
            #checar se o proximo passo esta na lista fechada
            if len([passo_fechado for passo_fechado in lista_fechada if passo_fechado==passo]) > 0:
                continue
        
            passo.g = no_atual.g + 1
            passo.h = calculo_heuristica(passo.position, aux.goal_state)
            passo.f = passo.g + passo.h

            #checar se o proximo passo já ta na lista aberta
            if len([passo_aberto for passo_aberto in lista_aberta if passo.position == passo_aberto.position and passo.g > passo_aberto.g]) > 0:
                continue
            
            heapq.heappush(lista_aberta, passo)

    print("Resposta não encontrada")
    #Contar nós expandidos
    print("Quantidade de nos expandidos: ", nos_expandidos)
    #Contar média de nós
    print("\nMedia de nos: ", nos_expandidos+iterations//2)
    #Finish timer
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", iterations)
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
