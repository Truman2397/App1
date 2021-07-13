from tkinter import *
import tkinter as tk
from tkinter import ttk
import os 
import pandas as pd
import sqlite3


root = Tk()
root.geometry("460x290")
root.config(bg="dark cyan")

#####---Generador de CSV---#####
def Datos1():     
      Combo3_info = Combo3.get()
      conn = sqlite3.connect('DB1.db')
      cur = conn.cursor()
      query = cur.execute("SELECT * FROM Usuario where ID="+Combo3_info)
      data = []
      # print(cur.fetchall())
      
      resultado= cur.fetchall()
      ID = resultado[0][0]
      Nombre = resultado[0][1]
      Apellido = resultado[0][2]
      Sexo = resultado[0][3]
      Pais = resultado[0][4]
       
      cur.close()
      conn.close()
      print(resultado[0][1])
      data = {"ID":[ID], "Nombre":[Nombre], "Apellido":[Apellido], "Sexo":[Sexo], "Pais":[Pais]} 
      
      archivo = pd.DataFrame(data)
      archivo.to_csv("PRUEBA_Usr.csv", mode="a", header=not os.path.isfile("Data1.csv"))
           
#####---Diseño---#####
Frame1 = Frame(root, bd=2, padx=10, pady=3)
Label(Frame1, text="Seleccione un ID: ", font=('Times', 14)).grid(row=1, column=0, sticky=W, pady=10)
Combo3 = ttk.Combobox(Frame1, font=('Times', 15), width=25)
Combo3.grid(row=1, column=1, pady=10, padx=20, sticky=W)

Boton1 = Button(Frame1, text="Generar CSV", width=10, command = Datos1).grid(row=4, column=1, sticky=W, pady=10)
Frame1.place(x=20, y=40)

#####---Consulta a la DB---#####
def combo_Name():
    conn = sqlite3.connect('DB1.db')
    cur = conn.cursor()
    query = cur.execute('SELECT ID FROM Usuario')
    
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    cur.close()
    conn.close()
    return data    
    
Combo3['values'] = combo_Name() 
   
root.mainloop()
