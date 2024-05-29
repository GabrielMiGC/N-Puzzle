import time
import pprint
import auxiliares as aux # type: ignore

def caminho(no_atual):
    caminhof = []
    atual = no_atual
    
    while atual is not None:
        
        caminhof.append(no_atual.position)
        print(atual.position)
        atual = atual.no_pai
    return caminhof

def Profundidade_Iterativa(max_Deep):
    #iniciar timer
    timer_starter = time.perf_counter()
    
    #só esta usando g como profundidade do no 
    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.g = no_inicial.h = no_inicial.f = 0
    no_final = aux.Node(None, aux.goal_state)
    no_final.g = no_final.h = no_final.f = 0

    lista_aberta = []
    lista_fechada = []
    

    lista_aberta.append(no_inicial)

    #Nao rodar infinitamente
    iterations = 0
    nos_expandidos = 0
    max_iteracoes = (len(aux.initial_state) ** len(aux.initial_state) ** len(aux.initial_state)//2)
    #sys.setrecursionlimit(max_iteracoes)
    while len(lista_aberta) > 0:
        iterations += 1

        if iterations == max_iteracoes - 1:
            print("Iteracoes demais, cancelando busca!\n")
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("\nMedia de nos: ", nos_expandidos+iterations//2)
            print("Quantidade de passos: ", len(lista_fechada))
            timer_finisher = time.perf_counter()
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            return print(caminho(no_atual))
        
        no_atual = lista_aberta.pop(-1)
        nos_expandidos += 1
        lista_fechada.append(no_atual)
        print("RESTAM NA LISTA ABERTA:", len(lista_aberta))
        print("NA LISTA FECHADA:",len(lista_fechada))

        if no_atual == no_final:
            return caminho(no_atual)

        sucessores = []
        for direcao in ["up", "down", "left", "right"]:
            
            move = aux.move_X(no_atual.position, direcao)
            novo_no = aux.Node(no_atual, move)
            sucessores.append(novo_no)
            

        for passo in sucessores:
            #como só esta usando g preenche os outros valores com 0 
            passo.g = no_atual.g + 1
            passo.h = 0
            passo.f = 0

            #checar se os proximos passos alcançam a profundidade maxima 
            if passo.g >= max_Deep:
                continue

            #checar se o proximo passo esta na lista fechada
            if len([passo_fechado for passo_fechado in lista_fechada if passo_fechado==passo]) > 0:
                continue
            
            lista_aberta.append(passo)              

    #caso a lista aberta fique vazia o objetivo não foi atingido 
    if len(lista_aberta) == 0:
        lista_aberta.clear()
        lista_fechada.clear()
        #aumentando a profundidade iterativamente
        Profundidade_Iterativa(max_Deep+1)
    


    #Contar nós expandidos
    print("Quantidade de nos expandidos: ", nos_expandidos)
    #Contar média de nós
    print("\nMedia de nos: ", nos_expandidos+iterations//2)
    #Finish timer
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", len(lista_fechada))
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")  