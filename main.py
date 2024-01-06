#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:34:07 2023

@author: davinky
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()

# configure the root window
        self.title('Gestion de Inventario')
        self.geometry("1251x800")
        self.resizable(False,False)
        
        # Conectar a la base de datos SQLite
        database_path = "/home/davinky/Documents/Tareas/Gestion-de-Inventario/databases/database-producto"
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()
                
    # label
        self.label = ttk.Label(self,border=20,relief="ridge",text="Sistema De Inventario!",font=("liberation-sans", 15 ,"bold"),foreground="blue")
        self.label.pack(fill="x")
    
 # ####################  DATA FRAME #############################
        
        DataFrame_1= tk.Frame(self,bd=15,relief="ridge")
        DataFrame_1.place(x=0,y=80,width=1251,height=300)
        
        DataFrame_2 = tk.LabelFrame(DataFrame_1,border=10,relief="ridge",text="Informacion De Medicamentos",font=("liberation-sans",14,"bold"))
        DataFrame_2.place(x=0,y=5,width=871,height=250)
        
        DataFrame_3 = tk.LabelFrame(DataFrame_1,border=10,relief="ridge",padx=10,text="Informacion Delegados",font=("liberation-sans",14,"bold"))
        DataFrame_3.place(x=800,y=5,width=406,height=250)

###################### Button frame ################################
        ButtonFrame = tk.Frame(self,bd=20,relief="ridge")
        ButtonFrame.place(x=0,y=385,width=1251,height=70)
        
###################### Detalles frame 2 ################################

        DetallesFrame = tk.Frame(self,bd=20,relief="ridge")
        DetallesFrame.place(x=0,y=460,width=1251,height=340)
        
        Lbl_Codigo = ttk.Label(DataFrame_2,text='Codigo',font=("liberation-sans",11 ,"bold"),padding=5)
        Lbl_Codigo.grid(row=0,column=0)
        
        self.txt_Codigo = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Codigo.grid(row=0,column=1)
        
        Lbl_Nombre = ttk.Label(DataFrame_2,text='Nombre',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Nombre.grid(row=1,column=0)
        self.txt_Nombre = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Nombre.grid(row=1,column=1)
        
        Lbl_Cantida = ttk.Label(DataFrame_2,text='Cantida',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Cantida.grid(row=2,column=0)
        self.txt_Cantidad= ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Cantidad.grid(row=2,column=1)
        
        Lbl_Lote = ttk.Label(DataFrame_2,text='Lote',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Lote.grid(row=3,column=0)
        self.txt_Lote = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Lote.grid(row=3,column=1)
        
        Lbl_Fecha_Vencimiento = ttk.Label(DataFrame_2,text='Vencimiento',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Fecha_Vencimiento.grid(row=4,column=0)
        self.txt_Fecha_vencimiento = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Fecha_vencimiento.grid(row=4,column=1)
        
        Lbl_Destino = ttk.Label(DataFrame_2,text='Destino',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Destino.grid(row=5,column=0)
        self.txt_Destino = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Destino.grid(row=5,column=1)
        
        Lbl_Procedencia = ttk.Label(DataFrame_2,text='Procedencia',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Procedencia.grid(row=6,column=0)
        self.txt_Procedencia = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Procedencia.grid(row=6,column=1)
        
        Lbl_Distribuidor = ttk.Label(DataFrame_2,text='Distribuidor',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Distribuidor.grid(row=7,column=0)
        self. txt_Distribuidor = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self. txt_Distribuidor.grid(row=7,column=1)
        
        Lbl_Producto = ttk.Label(DataFrame_2,text='Producto Disponible',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Producto.grid(row=0,column=2)
        self.txt_Producto_Disponible = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=30)
        self.txt_Producto_Disponible.grid(row=0,column=3)

###################### Detalles frame 3 ################################

        Lbl_Delegado = ttk.Label(DataFrame_3, text='Delegado', font=("Helvetica", 11, "bold"),padding=5)
        Lbl_Delegado.grid(row=0, column=0)
        self.txt_Delegado = ttk.Entry(DataFrame_3, font=("Helvetica", 11, "bold"), width=33)
        self.txt_Delegado.grid(row=0, column=1)

        Lbl_Centro = ttk.Label(DataFrame_3, text='Centro', font=("Helvetica", 11, "bold"),padding=5)
        Lbl_Centro.grid(row=1, column=0)
        txt_Centro = ttk.Entry(DataFrame_3, font=("Helvetica", 11, "bold"), width=33)
        txt_Centro.grid(row=1, column=1)

        
        Lbl_Cedula = ttk.Label(DataFrame_3,text='Cedula',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Cedula.grid(row=2,column=0)
        txt_Cedula = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        txt_Cedula.grid(row=2,column=1)
        
        Lbl_requisa = ttk.Label(DataFrame_3,text='Requisa',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_requisa.grid(row=3,column=0)
        txt_requisa = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        txt_requisa.grid(row=3,column=1)
        
        Lbl_requisa_fecha = ttk.Label(DataFrame_3,text='Fecha',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_requisa_fecha.grid(row=4,column=0)
        txt_requisa_fecha = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        txt_requisa_fecha.grid(row=4,column=1)

###################### Buttons ################################
        
        Boton_Insertar = tk.Button(ButtonFrame,background="#169086", text='Insertar',font=("Helvetica",11 ,"bold"),width=21,command=self.insertar_producto)
        Boton_Insertar.grid(row=0,column=1)
        
        Boton_Actualizar = tk.Button(ButtonFrame,background="#169086" ,text='Actualizar',font=("Helvetica",11 ,"bold"),width=22)
        Boton_Actualizar.grid(row=0,column=2)
        
        Boton_Actualizar = tk.Button(ButtonFrame,background="#169086", text='Borrar',font=("Helvetica",11 ,"bold"),width=22,command=self.Borrar)
        Boton_Actualizar.grid(row=0,column=3)
        
        Boton_Limpiar = tk.Button(ButtonFrame,background="#169086", text='Limpiar',font=("Helvetica",11 ,"bold"),width=22,command=self.Limpiar_Campos)
        Boton_Limpiar.grid(row=0,column=4)
        
        Boton_Salir = tk.Button(ButtonFrame,background="#169086", text='Buscar',font=("Helvetica",11 ,"bold"),width=22,command=self.Buscar_Producto_Actual)
        Boton_Salir.grid(row=0,column=5)
        
        Boton_Salir = tk.Button(ButtonFrame,background="#169086", text='Salir',font=("Helvetica",11 ,"bold"),width=22)
        Boton_Salir.grid(row=0,column=6)

#################################################### Scrollbar ###########################################################
        scrollbar_x = ttk.Scrollbar(DetallesFrame, orient="horizontal")
        scrollbar_y = ttk.Scrollbar(DetallesFrame, orient="vertical")

#################################################### Tabla ###############################################################
# Crear el Treeview con columnas
        self.tabla_producto = ttk.Treeview(DetallesFrame, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        self.tabla_producto["columns"] = ("Codigo", "Nombre", "Cantidad",
                                     "Lote", "Fecha vencimiento", "Destino", "Procedencia","Distribuidor", "Producto Disponible")

# Configurar las columnas con tamaños iniciales
        
        self.tabla_producto.column("#0", width=1, stretch=tk.NO)  # Ancho mínimo para minimizar el espacio en blanco
        self.tabla_producto.column("Codigo", width=100)
        self.tabla_producto.column("Nombre", width=100)
        self.tabla_producto.column("Cantidad", width=80)
        self.tabla_producto.column("Lote", width=80)
        self.tabla_producto.column("Fecha vencimiento", width=80)
        self.tabla_producto.column("Destino", width=100)
        self.tabla_producto.column("Procedencia", width=100)
        self.tabla_producto.column("Distribuidor", width=100)
        self.tabla_producto.column("Producto Disponible", width=120)
        
        self.Add_Treeview()


# Configurar las columnas
        for index, col in enumerate (self.tabla_producto["columns"] ,start=1):
            self.tabla_producto.heading(col, text=col)
            self.tabla_producto.column(col, width=1 )  # Ajusta el ancho según sea necesario
        
# Agregar la barra de desplazamiento utilizando grid
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tabla_producto.grid(row=0, column=0, sticky="nsew")

# Configurar la barra de desplazamiento
        scrollbar_x.config(command=self.tabla_producto.xview) 
        scrollbar_y.config(command=self.tabla_producto.yview)

# Configurar el peso de las filas y columnas para que se expandan
        DetallesFrame.grid_rowconfigure(0, weight=1) 
        DetallesFrame.grid_columnconfigure(0, weight=1)

# Ajustar la altura del Treeview
        self.tabla_producto.configure(height=13)  # Ajusta el valor según tus necesidades
        
    def Add_Treeview(self): 
        # Crear un cursor
        cursor = self.connection.cursor()
    
        # Ejecutar la consulta SQL para obtener datos
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        print(datos)

       # Insertar datos en el Treeview
        for dato in datos:
          self.tabla_producto.insert("", tk.END, values=dato[1:])  # Excluir la primera columna (Codigo)


#########################  Funciones  ########################################
    
    def Buscar_Producto(self, codigo):
     try:
        # Realizar una consulta SQL para obtener la información del producto 
        self.cursor.execute("SELECT * FROM productos WHERE codigo=?", (codigo,))
        producto_info = self.cursor.fetchone()

        if producto_info:
            # Rellenar los Entry boxes con la información del producto
            self.txt_Codigo.delete(0, tk.END)
            self.txt_Codigo.insert(0, producto_info[1])

            self.txt_Nombre.delete(0, tk.END)
            self.txt_Nombre.insert(0, producto_info[2])

            self.txt_Cantidad.delete(0, tk.END)
            self.txt_Cantidad.insert(0, str(producto_info[3]))

            self.txt_Lote.delete(0, tk.END)
            self.txt_Lote.insert(0, producto_info[4])
            
            self.txt_Fecha_vencimiento.delete(0, tk.END)
            self.txt_Fecha_vencimiento.insert(0, producto_info[5]) 
            
            self.txt_Destino.delete(0, tk.END) 
            self.txt_Destino.insert(0, producto_info[6]) 
            
            self.txt_Procedencia.delete(0, tk.END) 
            self.txt_Procedencia.insert(0, producto_info[7]) 
            
            self.txt_Distribuidor.delete(0, tk.END)
            self.txt_Distribuidor.insert(0, producto_info[8])


            # Mostrar cantidad disponible o 0 si no hay cantidad disponible
            cantidad_disponible = producto_info[9] if producto_info[9] is not None else 0
            self.txt_Producto_Disponible.delete(0, tk.END)
            self.txt_Producto_Disponible.insert(0, cantidad_disponible)

        else:
            # Código no encontrado, puedes manejar esto según tus necesidades
            messagebox.showerror(title="ERROR", message="Código no encontrado")
     except Exception as e:
        # Manejar el error según tus necesidades
        print(f"Error al buscar producto: {e}")


    def Buscar_Producto_Actual(self):
     try:
        # Obtener el código actual del Entry
        codigo_actual = self.txt_Codigo.get()

        # Llamar a buscar_producto con el código actual
        self.Buscar_Producto(codigo_actual)
        

     except Exception as e:
        print(f"Error al buscar producto actual: {e}")
        
            
    def Borrar(self):
     try:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM productos WHERE nombre=?", (self.txt_Nombre.get(),))

        messagebox.showinfo("Datos Borrados")

     except Exception as e:
        # Manejar el error según tus necesidades
        self.connection.rollback()
        messagebox.showerror("Error al borrar")
        print(f"Error al borrar: {e}")
     finally:
        # Cerrar la conexión después de realizar la operación
        self.connection.commit()

            
    def insertar_producto(self):
     try:
        # Obtener los valores de los Entry widgets
        codigo = self.txt_Codigo.get()
        nombre = self.txt_Nombre.get()
        cantidad = int(self.txt_Cantidad.get())
        lote = self.txt_Lote.get()
        fecha_vencimiento = self.txt_Fecha_vencimiento.get()
        destino = self.txt_Destino.get()
        procedencia = self.txt_Procedencia.get()
        distribuidor = self.txt_Distribuidor.get()
        

        # Utilizar el bloque with para asegurar la correcta gestión de la conexión
        with self.connection:
            
            cursor = self.connection.cursor()
            
            # Obtener la cantidad disponible actual del producto
            self.cursor.execute("SELECT cantidad_disponible FROM productos WHERE codigo=?", (codigo,))
            cantidad_disponible_actual = self.cursor.fetchone()

            # Calcular la nueva cantidad en base a la cantidad disponible actual
            nueva_cantidad = cantidad_disponible_actual + cantidad if cantidad_disponible_actual is not None else cantidad

            # Insertar los datos en la base de datos
            self.cursor.execute("INSERT INTO productos (codigo, nombre, cantidad, lote, fecha_vencimiento, destino, procedencia, distribuidor, cantidad_disponible) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (codigo, nombre, cantidad, lote, fecha_vencimiento, destino, procedencia, distribuidor, nueva_cantidad))
            
            messagebox.showinfo("Datos Guardados")

            # Limpiar los Entry widgets después de la inserción
            self.Limpiar_Campos()

     except Exception as e:
        # Manejar el error según tus necesidades
        messagebox.showerror("ERROR AL INGRESAR DATOS",message="Error")
        print(f"Error al insertar: {e}")

     finally:
        # Cerrar el cursor en cualquier caso
        if cursor:
            cursor.close()
            


    
    def actualizar_campos(self, producto_info):
    # Campos en DataFrame_2
        self.txt_Codigo.delete(0, tk.END)
        self.txt_Codigo.insert(0, producto_info[0])
        
        self.txt_Nombre.delete(0, tk.END)
        self.txt_Nombre.insert(0, producto_info[1])
        self.txt_Cantidad.delete(0, tk.END)
        self.txt_Cantidad.insert(0, str(producto_info[2]))
        self.txt_Lote.delete(0, tk.END)
        self.txt_Lote.insert(0, producto_info[3])

    # Campos adicionales en DataFrame_2
    # Asegúrate de tener una referencia a estos Entry widgets (txt_Fecha, txt_vencimiento, txt_Destino, etc.)
        self.txt_Fecha.delete(0, tk.END)
        self.txt_Fecha.insert(0, producto_info[4])

        self.txt_vencimiento.delete(0, tk.END)
        self.txt_vencimiento.insert(0, producto_info[5])

        self.txt_Destino.delete(0, tk.END)
        self.txt_Destino.insert(0, producto_info[6])

        self.txt_Distribuidor.delete(0, tk.END)
        self.txt_Distribuidor.insert(0, producto_info[7])

        self.txt_Producto_Disponible.delete(0, tk.END)
        self.txt_Producto_Disponible.insert(0, producto_info[8])
        
        self.connection.close()

        
    def Limpiar_Campos(self):
        self.txt_Lote.delete(0, tk.END)
        self.txt_Codigo.delete(0, tk.END)
        self.txt_Nombre.delete(0, tk.END)
        self.txt_Cantidad.delete(0, tk.END)
        self.txt_Fecha_vencimiento(0,tk.END)
        self.txt_Destino(0,tk.END)
        self.txt_Procedencia(0,tk.END)
        self.txt_Distribuidor(0,tk.END)
        self.txt_Delegado(0,tk.END)
        self.txt_Cedula(0,tk.END)
        self.txt_Centro(0,tk.END)
        self.txt_requisa(0,tk.END) 
    
   
           

if __name__ == "__main__": 
    app = App()
    app.mainloop()
