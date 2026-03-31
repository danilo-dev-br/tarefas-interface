import tkinter as tk

def adicionar():
    tarefa = entrada.get()
    if tarefa:
        lista.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)

def remover():
    selecionado = lista.curselection()
    if selecionado:
        lista.delete(selecionado)

janela = tk.Tk()
janela.title("Lista de Tarefas")

entrada = tk.Entry(janela, width=30)
entrada.pack()

btn_add = tk.Button(janela, text="Adicionar", command=adicionar)
btn_add.pack()

btn_remove = tk.Button(janela, text="Remover", command=remover)
btn_remove.pack()

lista = tk.Listbox(janela, width=40)
lista.pack()

janela.mainloop()
