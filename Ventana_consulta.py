import tkinter as tk
import bd_conexion
from Ventana_ingreso import VentanaIngreso

class VentanaConsulta(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500")
        self.title("Consulta de productos")
        

     #Parte de los Frames
        self.frame_buscar = tk.Frame(self)
        self.frame_buscar.pack(fill="both",expand=True)
        
        self.frame_tabla = tk.Frame(self)
        self.frame_tabla.pack(fill="both",expand=True)

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(fill="both",expand=True)


    # Parte de los botones (frame_buscar)
        self.entry_buscar = tk.Entry(self.frame_buscar, width=30)
        self.entry_buscar.grid(row=0,column=1 ,padx=20,pady=20)
        self.btn_buscar = tk.Button(self.frame_buscar,text="Buscar", width=10,height=1,command=self.buscar)
        self.btn_buscar.grid(row=0,column=2 ,padx=15,pady=20)

    #parte tablas (frame_tabla)

        self.scrol_y = tk.Scrollbar(self.frame_tabla,orient=tk.VERTICAL)
        self.scrol_y.pack(side=tk.RIGHT,fill=tk.Y)

        self.scrol_x = tk.Scrollbar(self.frame_tabla,orient=tk.HORIZONTAL)
        self.scrol_x.pack(side=tk.BOTTOM,fill=tk.X)

        self.tabla = tk.Treeview(self.frame_tabla,columns=("ID","Nombre","Cantidad","Categoría","proveedor"),show="headings",height=15, yscrollcommand=self.scrol_y.set, xscrollcommand=self.scrol_x.set)
        self.scrol_y.config(command=self.tabla.yview)
        self.scrol_x.config(command=self.tabla.xview)
        for col in self.tabla["columns"]:
            self.tabla.heading(col,text=col)
            self.tabla.column("#0",width=50,  anchor="center")
            self.tabla.column("#1",width=120,  anchor="center")
            self.tabla.column("#2",width=120,  anchor="center")
            self.tabla.column("#3",width=120,  anchor="center")
            self.tabla.column("#4",width=120,  anchor="center")
        self.tabla.pack(padx=5)

    #parte botones de la tabla (frame_botones)
        self.btn_anadir = tk.Button(self.frame_botones,text="Añadir",width=20,height=1, command=self.anadir_nuevo).pack(side=tk.LEFT, pady=10, padx=100)
        self.btn_actualizar = tk.Button(self.frame_botones,text="Actualizar",command=self.actualizar_producto, width=20,height=1).pack(side=tk.LEFT, pady=10, padx=0)
        self.btn_eliminar = tk.Button(self.frame_botones,text="Eliminar",command=self.eliminar_producto, width=20,height=1).pack(side=tk.LEFT, pady=10, padx=100)
        self.cargar_datos()

    def cargar_datos(self, filtro=None):
        for row in self.tabla.get_children(): #obtiene las filas de la tabla
            self.tabla.delete(row)
        productos = bd_conexion.mostrar_datos(filtro) or []
        for prod in productos:
            self.tabla.insert("",tk.END,values=prod)


    def anadir_nuevo(self):
        form = VentanaIngreso(self)
        form.grab_set()
        self.wait_window(form)
        self.cargar_datos()

    def actualizar_producto(self):
        item = self.tabla.selection()
        if not item:
              tk.messagebox.showwarning("Seleccione un producto")
              return
        producto = self.tabla.item(item[0],"values")
        form = VentanaIngreso(self,producto)
        form.grab_set()
        self.wait_window(form)
        self.cargar_datos()

    def eliminar_producto(self):
        item = self.tabla.selection()
        if not item:
            tk.messagebox.showwarning("Selecciona un producto para eliminar")
            return
        producto = self.tabla.item(item[0],"values")
        confirmar = tk.messagebox.askyesno("Confirmar", f"¿Eliminar producto'{producto[1]}'?")
        if confirmar:
            bd_conexion.eliminar_datos(int(producto[0]))
            self.cargar_datos()
         

    def buscar(self):
        filtro = self.entry_buscar.get()
        self.cargar_datos(filtro)
    


        
    
