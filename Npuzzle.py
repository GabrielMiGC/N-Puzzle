import random as rdm

def grid(n):
    number_set = set(range(1, n*n + 1))
    number_set.add("X")
    
    generated_grid = []  # Lista para armazenar a matriz gerada
    
    for _ in range(n):
        row = []
        for _ in range(n):
            inside_number = rdm.sample(number_set, 1)[0]
            row.append(inside_number)
            number_set.remove(inside_number)  # Remove o número selecionado do conjunto
        generated_grid.append(row)
        print(' '.join(map(str, row)))
    print("puzzle:\n"+ str(generated_grid))

def A_manhattan():
    print("code")

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
        return main

if __name__ == "__main__":
    main()
