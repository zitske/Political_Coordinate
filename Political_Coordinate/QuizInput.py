import tkinter as tk
import pandas as pd 
import numpy as np 

filee = pd.read_excel(r"C:\Users\Eduardo Zitske\Documents\perguntaspoli.xlsx")


nperg = 0

xar = 0
yar = 0


    
    
    

    



def write_concordo_totalmente():
    vl = 10
    if (filee['tipo'] [nperg] == 'xa' ):
        xar += 10
    elif (filee['tipo'] [nperg] == 'ya' ):
        yar += 10
    elif (filee['tipo'] [nperg] == 'xa+ya'):
        yar += 10
        xar += 10
    nperg += 1
    print('pergunta atualizada')
    print("user concordou totalmente")
    print (xar)
    print (yar)

def write_concordo():
    vl = 5
    if (filee['tipo'] [nperg] == 'xa' ):
        xar += vl
    elif (filee['tipo'] [nperg] == 'ya' ):
        yar += vl
    print("user concordou")
    print (xar)
    print (yar)

def write_discordo():
    vl = -5
    if (filee['tipo'] [nperg] == 'xa' ):
        xar += vl
    elif (filee['tipo'] [nperg] == 'ya' ):
        yar += vl
    print("user discordou")
    print (xar)
    print (yar)

def write_discordo_totalmente():
    vl = -10
    if (filee['tipo'] [nperg] == 'xa' ):
        xar += vl
    elif (filee['tipo'] [nperg] == 'ya' ):
        yar += vl
    print("user discordou totalmente")
    print (xar)
    print (yar)
    root.update







##pergunta.config(text=filee['pergunta'] [1])

root = tk.Tk()
root.geometry("450x300")  
frame = tk.Frame(root)
frame.pack()
pergunta = tk.Label.setup(frame,text=filee['pergunta'] [nperg])
pergunta.pack(side=tk.TOP)
button = tk.Button(frame, 
                   text="DISCORDO TOTALMENTE", 
                   fg="red",
                   command=write_discordo_totalmente)
button.pack(side=tk.LEFT)
button = tk.Button(frame, 
                   text="DISCORDO", 
                   fg="red",
                   command=write_discordo)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="CONCORDO",
                   fg="green",
                   command=write_concordo)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="CONCORDO TOTALMENTE",
                   fg="green",
                   command=write_concordo_totalmente)
slogan.pack(side=tk.LEFT)

root.mainloop()