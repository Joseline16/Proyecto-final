import tkinter as tk
from tkinter import ttk
#conectando con la bd
from bd_conexion import insertar_datos,actualizar_datos

class VentanaIngreso(tk.Toplevel):
    def __init__(self,master, productos=None):
        super().__init__(master)
        self.geometry("300x300")
        self.title("Registro")
        self.resizable(False,False)
        self.productos = productos
        
        #Parte de los frame
        self.frame_datos = tk.Frame(self)
        self.frame_datos.pack(pady=10, fill="both",expand=True)
        
        self.frame_boton = tk.Frame(self)
        self.frame_boton.pack(fill="both",expand=True)


        #Ingreso de datos
        self.lbl_nombre=tk.Label(self.frame_datos,text="Nombre",justify=tk.LEFT).grid(row=0, column=0,padx=10, pady=9)
        self.entry_nombre=tk.Entry(self.frame_datos, width=30)
        self.entry_nombre.grid(row=0,column=1 ,padx=10, pady=9)

        self.lbl_categoria=tk.Label(self.frame_datos,text="Categoría",justify=tk.LEFT).grid(row=1, column=0,padx=10,pady=9)
        self.entry_categoria=ttk.Combobox(self.frame_datos, width=30, values=["Electronica","Ropa","Comida","Otros"])
        self.entry_categoria.grid(row=1,column=1 ,padx=10, pady=9)

        self.lbl_cantidad=tk.Label(self.frame_datos,text="Cantidad",justify=tk.LEFT).grid(row=2, column=0,padx=10, pady=9)
        self.entry_cantidad=tk.Entry(self.frame_datos, width=30)
        self.entry_cantidad.grid(row=2,column=1 ,padx=10, pady=9)

    
        self.lbl_proveedor=tk.Label(self.frame_datos,text="Proveedor",justify=tk.LEFT).grid(row=3, column=0,padx=10, pady=9)
        self.entry_proveedor=tk.Entry(self.frame_datos, width=30)
        self.entry_proveedor.grid(row=3,column=1 ,padx=10, pady=9)    

        #Boton Guardar
        if self.productos:
            self.llenar_datos()
            self.btn_actualizar = tk.Button(self.frame_boton, text="Actualizar",command=self.actualizar,width=15)
            self.btn_actualizar.pack( padx=10)
        else:
            self.btn_guardar = tk.Button(self.frame_boton, text="Guardar",command=self.guardar, width=15)
            self.btn_guardar.pack( padx=10)

    def llenar_datos(self):
        self.title("editar productos")
        self.entry_nombre.insert(0,self.productos[1])
        self.entry_cantidad.insert(0,self.productos[2])
        self.entry_categoria.set(self.productos[3])
        self.entry_proveedor.insert(0,self.productos[4])

    def guardar(self):
        nombre = self.entry_nombre.get()
        cantidad= int(self.entry_cantidad.get())
        categoria = self.entry_categoria.get()
        proveedor = self.entry_proveedor.get()

        insertar_datos(nombre,cantidad,categoria,proveedor)
        self.destroy()

    def actualizar(self):
        id=self.productos[0]
        nombre = self.entry_nombre.get()
        cantidad= int(self.entry_cantidad.get())
        categoria = self.entry_categoria.get()
        proveedor = self.entry_proveedor.get()
       
        actualizar_datos(id,nombre,cantidad,categoria,proveedor)
        self.destroy()
        
