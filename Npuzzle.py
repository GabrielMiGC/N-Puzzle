import manhattan as am
import auxiliares as aux
import Wrong_position as wp

    
def main():
    puzzle_size = int(input("Defina o tamanho do puzzle:"))
    aux.grid(puzzle_size)

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
        #CODE3
        #
        return 0 #provisório
    elif(option == 3):
        # A* (peças erradas)
        wp.A_wrong()
    elif(option == 4):
        # A*(Manhattan)
        am.A_manhattan()
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
