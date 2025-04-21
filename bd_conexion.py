import sqlite3
def conectar():
    conn =sqlite3.connect('bd_inventario')
    return conn

def insertar_datos(nombre,cantidad,categoria,proveedor):
        conn = conectar()
        cursor =conn.cursor()
        bd = '''INSERT INTO productos (nombre,cantidad,categoria,proveedor)
        VALUES('{}','{}','{}','{}')'''.format(nombre,cantidad,categoria,proveedor)
        cursor.execute(bd)
        conn.commit()
        cursor.close()

def mostrar_datos(filtro):
        conn = conectar()
        cursor = conn.cursor()
        if filtro:
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR  id=?", (f"%{filtro}%",filtro))
        else:
            cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return productos 

def eliminar_datos(id):
        try:
            conn = conectar()
            cursor  =conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id=?", (id,))
            conn.commit()
        except Exception as error:
            print(f'Error al eliminar el dato: {error}')
        finally:
            cursor.close()
            conn.close()

def actualizar_datos(id,nombre,cantidad,categoria,proveedor):
        try:
            conn = conectar()
            cursor =conn.cursor()
            bd = '''UPDATE productos 
            SET NOMBRE= ?, CANTIDAD = ?, CATEGORIA = ?,  PROVEEDOR = ? WHERE ID = ? '''

            cursor.execute(bd,(nombre,cantidad,categoria,proveedor,id))
            conn.commit()
            return cursor.rowcount
        except Exception as error:
            print(f"error al actualizar el producto{error}")
            return 0
        finally:
            cursor.close()
            conn.close()

    

