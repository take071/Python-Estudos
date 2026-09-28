import tkinter as tk

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")

login_frame = tk.Frame(janela)
login_frame.pack()

tk.Label(login_frame, text="Bem vindo ao Sistema de Login").pack()
tk.Label(login_frame, text="Login").pack()
userlogin = tk.Entry(login_frame)
userlogin.pack()

tk.Label(login_frame, text="Senha").pack()
userkey = tk.Entry(login_frame)
userkey.pack()

login = [
    ("Arthur", "1223"),
    ("Felipe", "2223")
]

incorrectLogin = tk.Label(login_frame)
incorrectLogin.pack()

logado = tk.Frame()
tk.Label(logado,text="Logado").pack()

def botao():
    usuario = userlogin.get()
    senha = userkey.get()
    if(usuario, senha) in login:
        login_frame.forget()
        logado.pack()
    else:
        incorrectLogin['text']="Login Incorreto"
tk.Button(login_frame, text="Confirmar", command=botao).pack()

janela.mainloop()