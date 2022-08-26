from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

# cores

preto = "#3d3d3d"
branco = "#fafcff"
verde = "#21c25c"
vermelho = "#eb463b"
cinza = "#dedcdc"
azul = "#3080f0"

# criando janela com tamanho sem ajuste

janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=False, height=False)
janela.config(bg=preto)

# chamando classe tempo

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    if dia_semana == "Sunday":
        dia_port = "Domingo"
    elif dia_semana == "Monday":
        dia_port = "Segunda-Feira"
    elif dia_semana == "Tuesday":
        dia_port = "Terca-Feira"
    elif dia_semana == "Wednesday":
        dia_port = "Quarta-feira"
    elif dia_semana == "Thursday":
        dia_port = "Quinta-Feira"
    elif dia_semana == "Friday":
        dia_port = "Sexta-Feira"
    elif dia_semana == "Saturday":
        dia_port = "Sabado"
    else:
        dia_port = "Dia nao reconhecido."
    
        
    label_relogio.config(text=hora)
    label_relogio.after(200, relogio)
    label_calendario.config(text= "  " + dia_port + "    " + str(dia) + "/" + str(mes) + "/" + str(ano))
    
#criado os label

label_relogio = Label(janela, bg=preto, fg=branco, text="", font="digital-7 80", justify=CENTER, padx=70)
label_relogio.grid(row=0, column=0, sticky=NW, padx=5)

label_calendario = Label(janela, bg=preto, fg=branco, text="", font="digital-7 25")
label_calendario.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()