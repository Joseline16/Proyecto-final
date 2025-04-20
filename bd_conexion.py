import sqlite3
import unittest
def conectar():
    conn =sqlite3.connect('bd_inventario')
    return conn
#conexion bd

#cursor.execute('''CREATE TABLE IF NOT EXISTS productos ( 
 #          id INTEGER PRIMARY KEY AUTOINCREMENT, 
  #           nombre TEXT,
   #        cantidad INTEGER, 
    #       categoría TEXT)''')

#c= conexion.cursor()
#c.execute("ALTER TABLE productos RENAME COLUMN 'categoría' TO 'categoria'")
#c.close()


def insertar_datos(nombre,cantidad,categoria,proveedor):
        conn = conectar()
        cursor =conn.cursor()
        bd = '''INSERT INTO productos (nombre,cantidad,categoria,proveedor)
        VALUES('{}','{}','{}','{}')'''.format(nombre,cantidad,categoria,proveedor)
        cursor.execute(bd)
        conn.commit()
        cursor.close()

def mostrar_datos(filtro=None):
        conn = conectar()
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR  id=?", (f"%{filtro}%",filtro))
        else:
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            cursor.close()
            return resultados 

def eliminar_datos(nombre):
        try:
            conn = conectar()
            cursor  =conn.cursor()
            bd ="DELETE FROM productos WHERE nombre = ?"
            cursor.execute(bd,(nombre,))
            conn.commit()
        except Exception as e:
            print(f"Error al eliminar el dato: {e}")
        finally:
            cursor.close()

def actualizar_datos(id,nombre,cantidad,categoria,proveedor):
        try:
            conn = conectar()
            cursor =conn.cursor()
            bd = '''UPDATE productos 
            SET NOMBRE= ?, CANTIDAD = ?, CATEGORIA = ?,  PROVEEDOR = ?
            WHERE ID = ? 
            '''
            cursor.execute(bd,(nombre,cantidad,categoria,proveedor,id))
            conn.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"error al actualizar el producto{e}")
            return 0
        finally:
            cursor.close()

    


#prueba1.actualizar_datos(
#    id=2,
#    nombre="camisetos",
#    cantidad=10,
#   categoria="ropa",
#    proveedor="josi")

#datos = prueba1.mostrar_datos()
#for fila in datos:
#   print(fila)