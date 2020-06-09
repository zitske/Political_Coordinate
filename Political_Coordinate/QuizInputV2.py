import tkinter as tk
import pandas as pd 
import numpy as np 


## IMPORTA PLANILHA COM PERGUNTAS 

arquivoP = pd.read_excel(r"C:\Users\Eduardo Zitske\Documents\Political_Coordinate\perguntaspoli.xlsx") 

## NUMERO DA PERGUNTA ATUAL

npergunta = 0

## VALOR DO EIXO X E Y DO USUÁRIO 

x = 0
y = 0

##

def pergType(peso):
    global nperg
    if (arquivoP['tipo'] [arquivoP] == 'xa' ):
        x + peso
    elif (arquivoP['tipo'] [arquivoP] == 'ya' ):
        y + peso
    elif (arquivoP['tipo'] [arquivoP] == 'xa+ya'):
        y + peso
        x + peso
        tk.update()
        arquivoP += 1
        print(arquivoP)
        print ("pergType CALLED")