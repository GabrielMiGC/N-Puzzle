import random as rdm
import time

def grid(n): #Gera grid inicial e objetivo (grid organizado propiamente), um dos elementos é X
    number_list = list(range(1, n*n))
    number_list.append("X")
    goal_list = number_list.copy()

    global initial_state, goal_state
    initial_state = []  # Lista para armazenar a matriz inicial
    goal_state = [] #Lista para armazenar o estado objetivo
    
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
    #Contar passos

    #Contar nós expandidos

    #Contar média de nós

    #Start timer
    timer_starter = time.perf_counter()
    print("code")

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
