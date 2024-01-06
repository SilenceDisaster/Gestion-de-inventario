#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:28:05 2024

@author: davinky
"""
import tkinter as tk
from tkinter import ttk

class Welcome:
    def __init__(self):
        # configure the root window
        self.root = tk.Tk()
        self.root.title("Bienvenido")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        DataFrame_1= tk.Frame(self.root,bd=15,relief="ridge")
        DataFrame_1.place(x=0,y=0,width=400,height=250)
        
        self.label = ttk.Label(DataFrame_1,border=20,text="Bienvenido!",font=("liberation-sans", 30 ,"bold"),foreground="blue")
        self.label.grid(row=0,column=1,columnspan=8)
        
        Lbl_Usuario = ttk.Label(DataFrame_1,text='User',font=("liberation-sans",15 ,"bold"),padding=15)
        Lbl_Usuario.grid(row=10,column=1)
        
        Lbl_Password = ttk.Label(DataFrame_1,text='Password',font=("liberation-sans",15 ,"bold"),padding=15)
        Lbl_Password.grid(row=11,column=1)
        
        self.txt_User = ttk.Entry(DataFrame_1,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_User.grid(row=10,column=2)
        
        self.txt_Password = ttk.Entry(DataFrame_1,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Password.grid(row=11,column=2)
        
        Boton_Inicio = tk.Button(DataFrame_1,background="#169086" ,text='Inico',font=("Helvetica",11 ,"bold"),width=21)
        Boton_Inicio.grid(row=13,column=1)
        
        Boton_Salir = tk.Button(DataFrame_1,background="#169086" ,text='Salir',font=("Helvetica",11 ,"bold"),width=22)
        Boton_Salir.grid(row=13,column=2)
        
        
        self.root.mainloop()


app = Welcome()
