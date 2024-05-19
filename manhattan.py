import time
import pprint
import heapq
import auxiliares as aux

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
    h = 0
    for i in range(len(atual_state)):
        if i != "X":
            quociente_atual, resto_atual = divmod(atual_state.index(objetivo[i]), len(estado_atual[0]))
            quociente_obj, resto_obj = divmod(i, len(estado_atual[0]))
            h += abs(quociente_atual - quociente_obj) + abs(resto_atual - resto_obj)
    """O resto da divisão entre a posição dos elementos em cada lista é subtraido da sua
    posição e esse resultado é seu valor heurístico"""
    
    for i in range(len(atual_state)):
        resto = atual_state.index(atual_state[i]) - objetivo.index(atual_state[i])
        h += resto
    return h

def caminho(no_atual):
    caminhof = []
    atual = no_atual
    while atual is not None:
        caminhof.append(no_atual.position)
        atual = no_atual.no_pai
    return caminhof[::-1]

def A_manhattan():
    #iniciar timer
    timer_starter = time.perf_counter()


    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.h = custo_estimado(no_inicial.position, aux.goal_state)
    no_inicial.f = no_inicial.g + no_inicial.h

    lista_aberta = []
    lista_fechada = []
    sucessores = []

    heapq.heapify(lista_aberta)
    heapq.heappush(lista_aberta, no_inicial)

    #Nao rodar infinitamente
    iterations = 0
    nos_expandidos = 0
    max_iteracoes = (len(aux.initial_state) ** len(aux.initial_state) ** len(aux.initial_state)*1.5)

    while len(lista_aberta) > 0:
        iterations += 1

        if iterations > max_iteracoes:
            print("Iteracoes demais, cancelando busca!\n")
            timer_finisher = time.perf_counter()
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("\nMedia de nos: ", nos_expandidos+iterations//2)
            print("Quantidade de passos: ", len(lista_fechada))
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            return print(caminho(no_atual))
        
        no_atual = heapq.heappop(lista_aberta)
        print("RESTAM NA LISTA ABERTA:", len(lista_aberta))
        print("NA LISTA FECHADA:",len(lista_fechada))
        nos_expandidos += 1
        lista_fechada.append(no_atual)
        
        if no_atual.position == aux.goal_state:
            caminho_completo = caminho(no_atual)
            timer_finisher = time.perf_counter()
            print("Quantidade de nos expandidos: ", nos_expandidos)
            print("Quantidade de passos: ", len(caminho_completo) - 1)
            print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
            for estado in caminho_completo:
                pprint.pprint(estado)
                print()
            return caminho_completo

        
        for direcao in ["up", "down", "left", "right"]:
            
            move = aux.move_X(no_atual.position, direcao)
            pprint.pprint(no_atual)
            novo_no = aux.Node(no_atual.position, move)
            sucessores.append(novo_no)
            

        for passo in sucessores:
            #checar se o proximo passo esta na lista fechada
            if len([passo_fechado for passo_fechado in lista_fechada if passo_fechado==passo]) > 0:
                continue
        
            passo.g = no_atual.g + 1
            passo.h = custo_estimado(passo.position, aux.goal_state)
            passo.f = passo.g + passo.h

            #checar se o proximo passo já ta na lista aberta
            if len([passo_aberto for passo_aberto in lista_aberta if passo.position == passo_aberto.position and passo.g > passo_aberto.g]) > 0:
                continue
            
            
            heapq.heappush(lista_aberta, passo)

    print("\nAlgoritmo não encontrou resposta")
    #Contar nós expandidos
    print("Quantidade de nos expandidos: ", nos_expandidos)
    #Contar média de nós
    print("\nMedia de nos: ", nos_expandidos+iterations//2)
    #Finish timer
    timer_finisher = time.perf_counter()
    print("Quantidade de passos: ", len(lista_fechada))
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
