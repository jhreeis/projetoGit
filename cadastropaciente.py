from pacientemulher import PacienteM
from pacientehomem import PacienteH
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Criação da Lista de pacientes
lista = []

#Função de cadastro de pacientes
def cadastroPessoa():
    nome = entryNome.get()
    idade = entryIdade.get()
    temperatura = entryTemperatura.get()
    pressao = entryPressao.get()
    peso = entryPeso.get()
    sexo = varSexo.get()

    if sexo == "Homem":
        if nome == "":
            messagebox.showinfo("Erro", "Nome do paciente deve ser preenchido.")
        elif not nome.isalpha():
            messagebox.showinfo("Erro", "Nome inválido.")
        elif idade == "":
            messagebox.showinfo("Erro", "Idade do paciente deve ser preenchida.")
        elif not idade.isdigit():
            messagebox.showinfo("Erro", "Idade inválida.")
        elif temperatura == "":
            messagebox.showinfo("Erro", "Temperatura do paciente deve ser preenchida.")
        elif not temperatura.isdigit():
            messagebox.showinfo("Erro", "Temperatura inválida.")
        elif pressao == "":
            messagebox.showinfo("Erro", "Pressão do paciente deve ser preenchida.")
        elif peso == "":
            messagebox.showinfo("Erro", "Peso do paciente deve ser preenchido.")
        elif not peso.isdigit():
            messagebox.showinfo("Erro", "Peso inválido.")
        else:
          h = PacienteH(nome, idade, temperatura, pressao, peso)
          salvar(h)
          messagebox.showinfo("Cadastro", f"Paciente {nome} cadastrado com sucesso!")

    else:
         if nome == "":
            messagebox.showinfo("Erro", "Nome do paciente deve ser preenchido.")
         elif not nome.isalpha():
            messagebox.showinfo("Erro", "Nome inválido.")
         elif idade == "":
            messagebox.showinfo("Erro", "Idade deve ser preenchida.")
         elif not idade.isdigit():
            messagebox.showinfo("Erro", "Idade inválida.")
         elif temperatura == "":
            messagebox.showinfo("Erro", "Temperatura do paciente deve ser preenchida.")
         elif not temperatura.isdigit():
            messagebox.showinfo("Erro", "Temperatura inválida.")
         elif pressao == "":
            messagebox.showinfo("Erro", "Pressão do paciente deve ser preenchida.")
         elif peso == "":
            messagebox.showinfo("Erro", "Peso do paciente deve ser preenchido.")
         elif not peso.isdigit():
            messagebox.showinfo("Erro", "Peso inválido.")
         else:
          m = PacienteM(nome, idade, temperatura, pressao, peso)
          salvar(m)
          messagebox.showinfo("Cadastro", f"Paciente {nome} cadastrada com sucesso!") 

#Função que salva os pacientes e seus dados na lista
def salvar(obj):
    lista.append(obj)

#Função que atualiza a lista de pacientes
def atualizarListbox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

#Criação das janelas, tabs, entradas, labels e botões
janela =  tk.Tk()
janela.title("Cadastro de pacientes do Hospital")
janela.geometry("500x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)

for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Pacientes Cadastrados")

label1 = tk.Label(tab1, text="Nome:", font=("",15))
label1.grid(row=0, column=0, sticky="w", padx=10)

entryNome = tk.Entry(tab1, font=("", 15))
entryNome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label2 = tk.Label(tab1, text="Idade:", font=("",15))
label2.grid(row=1, column=0, sticky="w", padx=10)

entryIdade = tk.Entry(tab1, font=("", 15))
entryIdade.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label3 = tk.Label(tab1, text="Temperatura:", font=("",15))
label3.grid(row=2, column=0, sticky="w", padx=10)

entryTemperatura = tk.Entry(tab1, font=("", 15))
entryTemperatura.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

label4 = tk.Label(tab1, text="Pressão:", font=("",15))
label4.grid(row=3, column=0, sticky="w", padx=10)

entryPressao = tk.Entry(tab1, font=("", 15))
entryPressao.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

label5 = tk.Label(tab1, text="Peso:", font=("",15))
label5.grid(row=4, column=0, sticky="w", padx=10)

entryPeso = tk.Entry(tab1, font=("", 15))
entryPeso.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Sexo", font=("", 15)).grid(row=5, column=0, sticky="w", padx=10)
varSexo = tk.StringVar(value="Homem")

tk.Radiobutton(tab1, text="Feminino", font=("", 10), variable=varSexo, value="Mulher").grid(row=5, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Masculino", font=("", 10), variable=varSexo, value="Homem").grid(row=5, column=1, sticky="e", padx=10)
tk.Button(tab1, text="Cadastrar", font=("", 10), command=cadastroPessoa).grid(row=6, columnspan=2, sticky="nsew")

listbox = tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar",font=("", 15), command=atualizarListbox).grid(row=1, column=0, sticky="nsew")

#Função que impede que a janela abra e feche imediatamente
janela.mainloop()