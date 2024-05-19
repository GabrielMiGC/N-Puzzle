import auxiliares as aux
import heapq 
import time
import pprint
from manhattan import custo_estimado

def intersec(lista_A_init, lista_A_final):
    for no_i in lista_A_init:
        for no_f in lista_A_final:
            if no_i.position == no_f.position:
                return True
            else:
                return False

def caminho(no_a_init, no_a_final):
    caminho_init = []
    caminho_final = []
    inicial = no_a_init
    final = no_a_final
    while inicial is not None:
        caminho_init.append(inicial.position)
        inicial =  inicial.no_pai
    while final is not None:
        caminho_final.append(final.position)
        final = final.no_pai
    caminho_final.reverse()

    path = caminho_init + caminho_final[1:]

    return path     
def bidirecional():
    #Iniciar timer
    time_starter =  time.perf_counter()

    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.g = 0
    no_inicial.h = custo_estimado(aux.initial_state, aux.goal_state)
    no_inicial.f = no_inicial.g + no_inicial.h

    no_final = aux.Node(None, aux.goal_state)
    no_final.h = 0
    no_final.f = no_final.g + no_final.h

    lista_aberta_init = []
    lista_fechada_init = []
    
    heapq.heapify(lista_aberta_init)
    heapq.heappush(lista_aberta_init, no_inicial)

    lista_aberta_final = []
    lista_fechada_final = []
    heapq.heappush(lista_aberta_final, no_final)

    iteracoes = 0
    nos_expandidos = 0
    sucessores_i = []
    sucessores_f = []
    qtd = len(lista_aberta_init) + len(lista_aberta_final)
    while qtd > 0:
        iteracoes += 1
        
        if len(lista_aberta_init) > 0:
            no_at_inicial = heapq.heappop(lista_aberta_init)
            for direcao in ["up", "down", "left", "right"]:
                move = aux.move_X(no_at_inicial.position, direcao)
                novo_no_i = aux.Node(no_at_inicial, move)
                sucessores_i.append(novo_no_i)

            for passo_i in sucessores_i:
                if len([p_f_i for p_f_i in lista_fechada_init if p_f_i==passo_i]) > 0:
                    continue

                passo_i.g = no_at_inicial.g + 1
                passo_i.h = custo_estimado(passo_i.position, aux.goal_state)
                passo_i.f = passo_i.g + passo_i.h
                if len([passo_aberto for passo_aberto in lista_aberta_init if passo_i.position == passo_aberto.position and passo_i.g > passo_aberto.g]) > 0:
                    continue
                print("\nNo da ponta inicial\n")
                pprint.pprint(no_at_inicial)
                heapq.heappush(lista_aberta_init, passo_i)
                
        print("RESTAM NA LISTA ABERTA inicial:", len(lista_aberta_init))
        print("RESTAM NA LISTA ABERTA final:", len(lista_aberta_final))

        print("NA LISTA FECHADA:",len(lista_fechada_init))
        nos_expandidos += 1
        lista_fechada_init.append(no_at_inicial)

        if len(lista_aberta_final) > 0:
            no_at_final = heapq.heappop(lista_aberta_final)


            for direcao in ["up", "down", "left", "right"]:

                move_f = aux.move_X(no_at_final.position, direcao)
                novo_no_f = aux.Node(no_at_final, move_f)
                sucessores_f.append(novo_no_f)
            for passo_f in sucessores_f:
                if len([p_f_f for p_f_f in lista_fechada_init if p_f_f==passo_i]) > 0:
                    continue
                passo_f.g = no_at_final.g + 1
                passo_f.h = custo_estimado(passo_f.position, aux.goal_state)
                passo_f.f = passo_f.g + passo_f.f

                if len([passo_abertof for passo_abertof in lista_aberta_final if passo_f.position == passo_abertof.position and passo_f.g > passo_abertof.g]) > 0:
                    continue
                print("\nNo da ponta final\n")
                pprint.pprint(no_at_final)
                heapq.heappush(lista_aberta_final, passo_f)
        
        lista_fechada_final.append(no_at_final)

        if intersec(lista_aberta_init, lista_aberta_final) == True:
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("Media de nos: ", nos_expandidos//iteracoes)
            timer_finisher = time.perf_counter()
            print("\n\n\n\n\n\\nQuantidade de passos: ", len(lista_fechada_init)+ len(lista_fechada_final))
            print(f"Tempo de execução do algoritmo: {timer_finisher - time_starter:0.4f} segundos")
            
            return caminho(no_at_inicial, no_at_final)
    

            
                
            
    print("\nResposta nao encontrada")
    print("Quantidade de nos expandidos: ", nos_expandidos)
    print("\nMedia de nos: ", nos_expandidos+iteracoes//2)
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", nos_expandidos+iteracoes//2)
    print(f"Tempo de execução do algoritmo: {timer_finisher - time_starter:0.4f} segundos")
    #pprint.pprint(caminho(no_at_inicial, no_at_final))
