import tkinter as tk
from tkinter import messagebox
import manhattan as am
import Wrong_position as wp
import bidirecional as bi
import ProfundidadeIterativa as pi
import bfs
import auxiliares as aux
import time

class NPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Puzzle Solver")
        self.size = tk.IntVar(value=3)
        self.algoritmo = tk.StringVar(value="A*_Manhattan")
        self.historico = []
        self.index_atual = 0
        self.start_time = 0

        self.tela_inicial()

    def tela_inicial(self):
        self.clear_window()

        frame = tk.Frame(self.root)
        frame.pack(pady=30)

        tk.Label(frame, text="Escolha o tamanho do puzzle:").pack()
        tk.Spinbox(frame, from_=3, to=5, textvariable=self.size, width=5).pack(pady=5)

        tk.Label(frame, text="Escolha o algoritmo:").pack()
        algoritmos = [
            ("A* (Manhattan)", "A*_Manhattan"),
            ("A* (Peças Erradas)", "A*_Errado"),
            ("A* Bidirecional", "A*_Bidi"),
            ("Profundidade Iterativa", "Prof_Iter"),
            ("Busca em Largura", "BFS")
        ]
        for text, value in algoritmos:
            tk.Radiobutton(frame, text=text, variable=self.algoritmo, value=value).pack(anchor="w")

        tk.Button(self.root, text="Iniciar", command=self.inicializar_interface).pack(pady=20)

    def inicializar_interface(self):
        self.clear_window()
        n = self.size.get()
        aux.grid(n)

        self.buttons = []
        self.historico = []
        self.index_atual = 0

        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=10)
        for i in range(n):
            row = []
            for j in range(n):
                btn = tk.Button(grid_frame, text="", width=4, height=2, font=('Arial', 18))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
        self.update_grid(aux.initial_state)

        tk.Button(self.root, text="Resolver", command=self.executar_algoritmo).pack(pady=10)

        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=10)

        self.prev_btn = tk.Button(nav_frame, text="◀ Anterior", command=self.mostrar_anterior, state=tk.DISABLED)
        self.prev_btn.grid(row=0, column=0, padx=10)

        self.label_passo = tk.Label(nav_frame, text="Passo 0 de 0")
        self.label_passo.grid(row=0, column=1)

        self.next_btn = tk.Button(nav_frame, text="Próximo ▶", command=self.mostrar_proximo, state=tk.DISABLED)
        self.next_btn.grid(row=0, column=2, padx=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def update_grid(self, state):
        for i in range(self.size.get()):
            for j in range(self.size.get()):
                val = state[i][j]
                self.buttons[i][j]['text'] = "" if val == 'X' else str(val)

    def executar_algoritmo(self):
        escolha = self.algoritmo.get()
        caminho = []
        self.start_time = time.perf_counter()

        if escolha == "A*_Manhattan":
            caminho = am.A_manhattan()
        elif escolha == "A*_Errado":
            caminho = wp.A_wrong()
        elif escolha == "A*_Bidi":
            caminho = bi.bidirecional()
        elif escolha == "Prof_Iter":
            caminho = pi.Profundidade_Iterativa(0)
        elif escolha == "BFS":
            estado_inicial = tuple(map(tuple, aux.initial_state))
            grafo = bfs.build_graph(estado_inicial)
            caminho, _ = bfs.bfs(grafo, estado_inicial, aux.goal_state)

        tempo_execucao = time.perf_counter() - self.start_time

        if caminho:
            self.historico = caminho[::-1]
            self.index_atual = len(self.historico) - 1
            self.update_grid(self.historico[self.index_atual])
            self.atualizar_navegacao()
            messagebox.showinfo("Solução encontrada", f"Tempo: {tempo_execucao:.4f} segundos\nPassos: {len(self.historico)}")
        else:
            messagebox.showwarning("Falha", "Nenhuma solução encontrada.")

    def atualizar_navegacao(self):
        total = len(self.historico)
        self.label_passo.config(text=f"Passo {self.index_atual + 1} de {total}")
        self.prev_btn.config(state=tk.NORMAL if self.index_atual > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if self.index_atual < total - 1 else tk.DISABLED)

    def mostrar_proximo(self):
        if self.index_atual < len(self.historico) - 1:
            self.index_atual += 1
            self.update_grid(self.historico[self.index_atual])
            self.atualizar_navegacao()

    def mostrar_anterior(self):
        if self.index_atual > 0:
            self.index_atual -= 1
            self.update_grid(self.historico[self.index_atual])
            self.atualizar_navegacao()


if __name__ == "__main__":
    root = tk.Tk()
    app = NPuzzleGUI(root)
    root.mainloop()
