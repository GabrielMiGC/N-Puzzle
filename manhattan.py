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
        caminhof.append(atual.position)
        atual = atual.no_pai
    return caminhof[::-1]

def A_manhattan():
    #iniciar timer
    timer_starter = time.perf_counter()


    no_inicial = aux.Node(None, aux.initial_state)
    no_inicial.g = no_inicial.h = no_inicial.f = 0
    no_final = aux.Node(None, aux.goal_state)
    no_final.g = no_final.h = no_final.f = 0

    lista_aberta = []
    lista_fechada = []

    heapq.heapify(lista_aberta)
    heapq.heappush(lista_aberta, no_inicial)

    #Nao rodar infinitamente
    iterations = 0
    nos_expandidos = 0
    max_iteracoes = (len(aux.initial_state) ** len(aux.initial_state)//2)

    while len(lista_aberta) > 0:
        iterations += 1

        """if iterations > max_iteracoes:
            print("Iteracoes demais, cancelando busca!\n")
            timer_finisher = time.perf_counter()
            return print(caminho(no_atual))"""
        
        no_atual = heapq.heappop(lista_aberta)
        nos_expandidos += 1
        lista_fechada.append(no_atual)

        if no_atual == no_final:
            return caminho(no_atual)

        sucessores = []
        for direcao in ["up", "down", "left", "right"]:
            
            move = aux.move_X(no_atual.position, direcao)
            novo_no = aux.Node(no_atual, move)
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
            pprint.pp(no_atual)
            heapq.heappush(lista_aberta, passo)

    
    #Contar nós expandidos
    print("Quantidade de nos expandidos: ", nos_expandidos)
    #Contar média de nós
    print("\nMedia de nos: ", nos_expandidos//iterations)
    #Finish timer
    timer_finisher = time.perf_counter()
    print("\n\n\n\n\n\\nQuantidade de passos: ", len(lista_fechada))
    print(f"Tempo de execução do algoritmo: {timer_finisher - timer_starter:0.4f} segundos")
