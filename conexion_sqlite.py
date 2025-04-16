import sqlite3



#conexion bd

#cursor.execute('''CREATE TABLE IF NOT EXISTS productos ( 
 #          id INTEGER PRIMARY KEY AUTOINCREMENT, 
  #           nombre TEXT,
   #        cantidad INTEGER, 
    #       categoría TEXT)''')

#c= conn.cursor()
#c.execute("ALTER TABLE productos ADD COLUMN proveedor TEXT")

class ConexionBd():
    def __init__(self):
        self.conn = sqlite3.connect('bd_inventario')

    def insertar_datos(self,nombre,cantidad,categoria,proveedor):
        cursor =self.conn.cursor()
        bd = '''INSERT INTO productos (nombre,cantidad,categoria)
        VALUES('{}','{}','{}')'''.format(nombre,cantidad,categoria,proveedor)
        cursor.execute(bd)
        self.conn.commit()
        cursor.close

    def mostrar_datos(self):
        cursor = self.conn.cursor()
        bd = "SELECT*FROM productos"
        cursor.execute(bd)
        productos = cursor.fetchall()
        return productos 

    def eliminar_datos(self,nombre):
        cursor  =self.conn.cursor()
        bd ='''DELETE FROM productos WHERE nombre = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conn.commit()
        cursor .close()

    def actualizar_datos(self,id,nombre,cantidad,categoria,proveedor):
        cursor = self.conn.cursor()
        bd = '''UPDATE productos SET NOMBRE= '{}', CANTIDAD = '{}', CATEGORIA = '{}' 
        WHERE ID= '{}' '''.format(nombre,cantidad,categoria,proveedor, id)
        producto = cursor.rowcount
        self.conn.commit()

        
        cursor.close()
        return producto