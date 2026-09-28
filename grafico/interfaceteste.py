import tkinter as tk

janela = tk.Tk()
janela.title("Olá mundo")
janela.geometry("400x300")

tk.Label(janela, text="Bem-Vindo a essa aplicação").pack()

def botao():
    print("lol")

tk.Button(janela, text="clique em mim", command=botao).pack()

janela.mainloop()