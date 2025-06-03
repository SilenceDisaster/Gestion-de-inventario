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
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Gestion de Inventario')
        self.geometry("1270x830")
        self.resizable(False,False)

        # Configurar estilo global
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.configurar_estilos()

        # Colores para la interfaz (puedes personalizarlos)
        COLOR_FONDO = "#f5f5f5"  # Gris claro
        COLOR_TEXTO = "#333333"  # Gris oscuro
        COLOR_PRIMARIO = "#4a6fa5"  # Azul principal
        COLOR_BORDE = "#cccccc"  # Gris para bordes
        COLOR_FONDO_ENTRY = "#ffffff"  # Blanco
        
        # Conectar a la base de datos SQLite
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_dir = os.path.join(script_dir, "databases")
        os.makedirs(db_dir, exist_ok=True)  # Crear directorio si no existe
        database_path = os.path.join(db_dir, "database")  # Cambiado a .db
        print(database_path)
        try:
            self.connection = sqlite3.connect(database_path)
            self.cursor = self.connection.cursor()
            print(f"Conexión exitosa a {database_path}")
        except sqlite3.Error as e:
            messagebox.showerror("Error de BD", f"No se pudo conectar a la BD:\n{e}")
            self.destroy()
                
        # label
        self.label = ttk.Label(self,border=20,relief="ridge",text="Sistema De Inventario!",font=("liberation-sans", 15 ,"bold"),foreground="blue")
        self.label.pack(fill="x")
    
        # ####################  DATA FRAME #############################
        
        DataFrame_1= tk.Frame(self,bd=15,relief="ridge")
        DataFrame_1.place(x=0,y=67,width=1270,height=320)
        
        DataFrame_2 = tk.LabelFrame(DataFrame_1,border=10,relief="ridge",text="Informacion De Medicamentos",font=("liberation-sans",14,"bold"))
        DataFrame_2.place(x=2,y=5,width=890,height=280)
        
        DataFrame_3 = tk.LabelFrame(DataFrame_1,border=10,relief="ridge",padx=10,text="Informacion Delegados",font=("liberation-sans",14,"bold"))
        DataFrame_3.place(x=806,y=5,width=430,height=280)

        ###################### Button frame ################################
        ButtonFrame = tk.Frame(self,bd=20,relief="ridge")
        ButtonFrame.place(x=0,y=388,width=1270,height=70)
        
        ###################### Detalles frame 2 ################################

        DetallesFrame = tk.Frame(self,bd=20,relief="ridge")
        DetallesFrame.place(x=0,y=460,width=1270,height=360)
        
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
        self.txt_Distribuidor = ttk.Entry(DataFrame_2,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Distribuidor.grid(row=7,column=1)
        
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
        self.txt_Centro = ttk.Entry(DataFrame_3, font=("Helvetica", 11, "bold"), width=33)
        self.txt_Centro.grid(row=1, column=1)

        
        Lbl_Cedula = ttk.Label(DataFrame_3,text='Cedula',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_Cedula.grid(row=2,column=0)
        self.txt_Cedula = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_Cedula.grid(row=2,column=1)
        
        Lbl_requisa = ttk.Label(DataFrame_3,text='Requisa',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_requisa.grid(row=3,column=0)
        self.txt_requisa = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_requisa.grid(row=3,column=1)
        
        Lbl_requisa_fecha = ttk.Label(DataFrame_3,text='Fecha',font=("Helvetica",11 ,"bold"),padding=5)
        Lbl_requisa_fecha.grid(row=4,column=0)
        self.txt_requisa_fecha = ttk.Entry(DataFrame_3,font=("Helvetica",11 ,"bold"),width=33)
        self.txt_requisa_fecha.grid(row=4,column=1)

        ###################### Buttons ################################
        
        Boton_Insertar = tk.Button(ButtonFrame,background="#169086", text='Insertar',font=("Helvetica",11 ,"bold"),width=21,command=self.insertar_producto)
        Boton_Insertar.grid(row=0,column=1)
        
        Boton_Actualizar = tk.Button(ButtonFrame,background="#169086" ,text='Actualizar',font=("Helvetica",11 ,"bold"),width=22)
        Boton_Actualizar.grid(row=0,column=2)
        
        Boton_Borrar = tk.Button(ButtonFrame,background="#169086", text='Borrar',font=("Helvetica",11 ,"bold"),width=22,command=self.Borrar)
        Boton_Borrar.grid(row=0,column=3)
        
        Boton_Limpiar = tk.Button(ButtonFrame,background="#169086", text='Limpiar',font=("Helvetica",11 ,"bold"),width=22,command=self.Limpiar_Campos)
        Boton_Limpiar.grid(row=0,column=4)
        
        Boton_Buscar = tk.Button(ButtonFrame,background="#169086", text='Buscar',font=("Helvetica",11 ,"bold"),width=22,command=self.Buscar_Producto_Actual)
        Boton_Buscar.grid(row=0,column=5)
        
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
        for index, col in enumerate(self.tabla_producto["columns"], start=1):
            self.tabla_producto.heading(col, text=col)
            self.tabla_producto.column(col, width=1)  # Ajusta el ancho según sea necesario
        
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
        self.tabla_producto.configure(height=13)  
        
    def Add_Treeview(self):
        # Limpiar el Treeview primero
        for item in self.tabla_producto.get_children():
            self.tabla_producto.delete(item)
    
        try:
            self.cursor.execute("SELECT * FROM productos")
            productos = self.cursor.fetchall()
            
            # Insertar datos manteniendo el orden de columnas
            columnas = ["codigo", "nombre", "cantidad", "lote", 
                       "fecha_vencimiento", "destino", "procedencia",
                       "distribuidor", "producto_disponible"]
            
            for producto in productos:
                # Mapear los valores según el orden de las columnas
                valores = [producto[1], producto[2], producto[3], producto[4],
                          producto[5], producto[6], producto[7], producto[8], producto[9]]
                self.tabla_producto.insert("", tk.END, values=valores)
                
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudieron cargar los productos:\n{e}")

    #########################  Funciones  ########################################
    def configurar_estilos(self):
    # Definición de colores
        self.COLOR_PRIMARIO = "#2c3e50"  # Azul oscuro
        self.COLOR_SECUNDARIO = "#3498db"  # Azul
        self.COLOR_FONDO = "#ecf0f1"  # Gris claro
        self.COLOR_TEXTO = "#2c3e50"  # Azul oscuro
        self.COLOR_BOTONES = "#2980b9"  # Azul medio
        self.COLOR_HOVER = "#1abc9c"  # Verde turquesa
        
        # Configurar estilo general
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurar frames
        self.style.configure('TFrame', background=self.COLOR_FONDO)
        self.style.configure('Custom.TFrame', background='white', borderwidth=2, relief='solid')
        
        # Configurar LabelFrame
        self.style.configure('TLabelframe', background=self.COLOR_FONDO, font=('Helvetica', 12, 'bold'))
        self.style.configure('TLabelframe.Label', background=self.COLOR_FONDO, foreground=self.COLOR_PRIMARIO)
        
        # Configurar labels
        self.style.configure('TLabel', 
                        background=self.COLOR_FONDO,
                        foreground=self.COLOR_TEXTO,
                        font=('Helvetica', 10))
    
        self.style.configure('Bold.TLabel',
                        font=('Helvetica', 10, 'bold'),
                        padding=5)
    
    # Configurar entries
        self.style.configure('TEntry',
                        fieldbackground='white',
                        foreground=self.COLOR_TEXTO,
                        bordercolor='#bdc3c7',
                        insertcolor=self.COLOR_SECUNDARIO,
                        padding=5)
    
        self.style.map('TEntry',
                  bordercolor=[('focus', self.COLOR_SECUNDARIO)],
                  lightcolor=[('focus', self.COLOR_SECUNDARIO)])
    
    # Configurar botones
        self.style.configure('TButton',
                        font=('Helvetica', 10, 'bold'),
                        background=self.COLOR_BOTONES,
                        foreground='white',
                        borderwidth=1,
                        padding=8)
    
        self.style.map('TButton',
                  background=[('active', self.COLOR_HOVER)],
                  relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    def Buscar_Producto(self, criterio):
        try:
            self.cursor.execute("""
                SELECT * FROM productos 
                WHERE codigo LIKE ? OR nombre LIKE ?
            """, (f"%{criterio}%", f"%{criterio}%"))
            
            resultados = self.cursor.fetchall()
            self.mostrar_resultados_busqueda(resultados)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en búsqueda:\n{e}")

    def mostrar_resultados_busqueda(self, resultados):
        self.Add_Treeview()  # Limpiar y mostrar solo resultados
        for producto in resultados:
            valores = producto[1:]  # Excluir el ID
            self.tabla_producto.insert("", tk.END, values=valores)
            
    def Borrar(self):
        seleccion = self.tabla_producto.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para borrar")
            return
    
        if not messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este producto?"):
            return
    
        try:
            item = self.tabla_producto.item(seleccion[0])
            codigo = item['values'][0]  # Asumiendo que código es la primera columna
            
            self.cursor.execute("DELETE FROM productos WHERE codigo=?", (codigo,))
            self.connection.commit()
            
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.Add_Treeview()  # Actualizar la vista
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el producto:\n{e}")
            self.connection.rollback()
            
    def insertar_producto(self):
        try:
            datos = (
                self.txt_Codigo.get(),
                self.txt_Nombre.get(),
                int(self.txt_Cantidad.get()),
                self.txt_Lote.get(),
                self.txt_Fecha_vencimiento.get(),
                self.txt_Destino.get(),
                self.txt_Procedencia.get(),
                self.txt_Distribuidor.get(),
                self.txt_Producto_Disponible.get() or 0  # Valor por defecto si está vacío
            )
            
            self.cursor.execute("""
                INSERT INTO productos 
                (codigo, nombre, cantidad, lote, fecha_vencimiento, 
                 destino, procedencia, distribuidor, producto_disponible)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, datos)
            
            self.connection.commit()
            messagebox.showinfo("Éxito", "Producto insertado correctamente")
            self.Add_Treeview()  # Actualizar la vista
            self.Limpiar_Campos()
            
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número válido")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El código ya existe en la base de datos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al insertar producto:\n{e}")

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
        self.txt_Fecha_vencimiento.delete(0, tk.END)
        self.txt_Fecha_vencimiento.insert(0, producto_info[4])

        self.txt_Destino.delete(0, tk.END)
        self.txt_Destino.insert(0, producto_info[5])

        self.txt_Procedencia.delete(0, tk.END)
        self.txt_Procedencia.insert(0, producto_info[6])

        self.txt_Distribuidor.delete(0, tk.END)
        self.txt_Distribuidor.insert(0, producto_info[7])

        self.txt_Producto_Disponible.delete(0, tk.END)
        self.txt_Producto_Disponible.insert(0, producto_info[8])
        
    def Limpiar_Campos(self):
        campos = [
            self.txt_Codigo, self.txt_Nombre, self.txt_Cantidad,
            self.txt_Lote, self.txt_Fecha_vencimiento, self.txt_Destino,
            self.txt_Procedencia, self.txt_Distribuidor, self.txt_Producto_Disponible,
            self.txt_Delegado, self.txt_Cedula, self.txt_Centro, self.txt_requisa, 
            self.txt_requisa_fecha
        ]
        
        for campo in campos:
            campo.delete(0, tk.END)
    
    def Buscar_Producto_Actual(self):
        try:
            # Obtener el código actual del Entry
            codigo_actual = self.txt_Codigo.get()
            # Llamar a buscar_producto con el código actual
            self.Buscar_Producto(codigo_actual)
        except Exception as e:
            print(f"Error al buscar producto actual: {e}")

if __name__ == "__main__": 
    app = App()
    app.mainloop()
