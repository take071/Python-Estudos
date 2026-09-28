import tkinter as tk

janela = tk.Tk()
janela.title("Olá mundo")
janela.geometry("400x300")

texto = tk.Label(janela, text="Olá user, seja Bem-Vindo")
texto.pack()

def botao():
 nome = entrada.get()
 texto['text'] = f"Olá,{nome}"

entrada = tk.Entry(janela)
entrada.pack()
    
tk.Button(janela, text="Botão da Felicidade", command=botao).pack()

janela.mainloop()