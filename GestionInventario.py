import tkinter as tk
from tkinter import Tk,Button,Entry,Label,ttk,PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
#conectando con la bd
from conexion_sqlite import ConexionBd
#strftime para tener el tiempo actual para dar el nombre al archivo excel y panda para exportar 
from time import strftime
import pandas as pd

ventana1 = tk.Tk() #crear una ventana
ventana1.title ("Ventana Principal")
ventana1.geometry("900x500") #tamaño
ventana1.resizable(False,False)

lblTitulo = Label(ventana1,text="SISTEMA DE GESTIÓN DE INVENTARIO")
lblTitulo.pack()

frame1 = Frame(ventana1,bg="light grey")
frame1.place(x=0,y=25,width=900, height=30)

btnInicio = Button(frame1,text="Inicio", width=10)
btnInicio.pack(side=tk.LEFT)

btnConsulta = Button(frame1,text="Consulta",width=10)
btnConsulta.pack(side=tk.LEFT, padx=2)

btnReportes = Button(frame1,text="Reportes",width=10)
btnReportes.pack(side=tk.LEFT)

RegistroFrame = tk.LabelFrame(ventana1, text= "Registro",width=300, height=400)
RegistroFrame.place(x=10, y=70)

frameA= Frame (RegistroFrame, pady=20)
frameA.place(x=0,y=20,width=280, height=280)

lblnombre = Label(frameA, text="Nombre")
lblnombre.grid(row=0, column=0,padx=10, pady=3)

entryNombre = Entry(frameA, width=30, )
entryNombre.grid(row=0,column=1 ,padx=10, pady=6)

lblCantidad = Label(frameA, text="Cantidad",justify='left')
lblCantidad.grid(row=1, column=0,padx=10, pady=3)

entryCantidad = Entry(frameA, width=30, justify='center')
entryCantidad.grid(row=1,column=1 ,padx=10, pady=6)


lblCategoria = Label(frameA, text="Categoria", justify='left')
lblCategoria.grid(row=2, column=0,padx=10, pady=3)

entryCategoria = Entry(frameA, width=30, justify='center')
entryCategoria.grid(row=2,column=1 ,padx=10, pady=6)

lblProveedor = Label(frameA, text="Proveedor", justify='left')
lblProveedor.grid(row=3, column=0,padx=10, pady=3)

entryProveedor = Entry(frameA, width=30, justify='center')
entryProveedor.grid(row=3,column=1 ,padx=10, pady=6)

frameB = Frame (RegistroFrame, pady=20)
frameB.place(x=0,y=250,width=280, height=100)

btnNuevo = Button(frameB,text="Nuevo", width=10,height=1)
btnNuevo.pack(side=tk.LEFT,padx=7)

btnGuardar = Button(frameB,text="Guardar", width=10,height=1)
btnGuardar.pack(side=tk.LEFT, padx=9)

btnBorrar = Button(frameB,text="Borrar", width=10,height=1)
btnBorrar.pack(side=tk.LEFT, padx=5)


frame4 = Frame(ventana1)
frame4.place(x=320, y=70,width=570, height=300)

scrol_y = ttk.Scrollbar(frame4,orient=tk.VERTICAL)
scrol_y.pack(side=tk.RIGHT,fill=tk.Y)

scrol_x = ttk.Scrollbar(frame4,orient=tk.HORIZONTAL)
scrol_x.pack(side=tk.BOTTOM,fill=tk.X)

tabla = ttk.Treeview(frame4,columns=("ID","Nombre","Cantidad","Categoría","Proveedor"), show="headings",height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
scrol_y.config(command=tabla.yview)
scrol_y.config(command=tabla.xview)

tabla.heading("#1", text="ID")
tabla.heading("#2", text="Nombre")
tabla.heading("#3", text="Cantidad")
tabla.heading("#4", text="Categoría")
tabla.heading("#5", text="Proveedor")

tabla.column("ID", anchor="center")
tabla.column("Nombre", anchor="center")
tabla.column("Cantidad", anchor="center")
tabla.column("Categoría", anchor="center")
tabla.column("Proveedor", anchor="center")

tabla.pack(expand=True)


OpcionesFrame = tk.LabelFrame(ventana1, text= "Opciones",width=570, height=100)
OpcionesFrame.place(x=450, y=385)


btnActualizar = Button(OpcionesFrame,text="Actualizar", width=10,height=2)
btnActualizar.pack(side=tk.LEFT, pady=5, padx=20)

btnEliminar = Button(OpcionesFrame,text="Eliminar", width=10,height=2)
btnEliminar.pack(side=tk.LEFT, pady=5, padx=20)


ventana1.mainloop()
