import tkinter as tk

def calcular_imc():
    altura = float(entry_altura.get()) / 100
    peso = float(entry_peso.get())

    imc = peso / (altura * altura)

    label_resultado.config(text=f"IMC: {imc:.2f}")

    canvas.delete("all")

    cor = "blue"
    if imc < 18.5:
        cor = "red"
    elif imc < 25:
        cor = "green"
    elif imc < 30:
        cor = "yellow"
    elif imc < 35:
        cor = "orange"
    else:
        cor = "red"

    canvas.create_line(0, 0, 500, 0, fill=cor)
    canvas.create_line(0, 18.5, 500, 18.5, fill=cor)
    canvas.create_line(0, 25, 500, 25, fill=cor)
    canvas.create_line(0, 30, 500, 30, fill=cor)
    canvas.create_line(0, 35, 500, 35, fill=cor)
    canvas.create_line(0, 40, 500, 40, fill=cor)

    canvas.create_oval(50, 0, 100, 185, fill=cor)

def reiniciar():
    entry_nome.delete(0, "end")
    entry_endereco.delete(0, "end")
    entry_altura.delete(0, "end")
    entry_peso.delete(0, "end")
    label_resultado.config(text="Resultado")
    canvas.delete("all")

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title("Cálculo do IMC")

label_titulo = tk.Label(janela, text="Cálculo do IMC")

label_nome = tk.Label(janela, text="Nome completo:")
entry_nome = tk.Entry(janela)

label_endereco = tk.Label(janela, text="Endereço completo:")
entry_endereco = tk.Entry(janela)

label_altura = tk.Label(janela, text="Altura (cm):")
entry_altura = tk.Entry(janela)

label_peso = tk.Label(janela, text="Peso (kg):")
entry_peso = tk.Entry(janela)

label_resultado = tk.Label(janela, text="Resultado")

canvas = tk.Canvas(janela, width=500, height=200)
canvas.pack()

botao_calcular = tk.Button(janela, text="Calcular")
botao_reiniciar = tk.Button(janela, text="Reiniciar")
botao_sair = tk.Button(janela, text="Sair")

label_titulo.pack()
label_nome.pack()
entry_nome.pack()
label_endereco.pack()
entry_endereco.pack()
label_altura.pack()
entry_altura.pack()
label_peso.pack()
entry_peso.pack()
label_resultado.pack()
botao_calcular.pack()
botao_reiniciar.pack()
botao_sair.pack()

botao_calcular.config(command=calcular_imc)
botao_reiniciar.config(command=reiniciar)
botao_sair.config(command=sair)
janela.mainloop()