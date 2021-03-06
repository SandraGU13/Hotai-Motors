from os import error
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('dbhotai.db')
        return con
    except :
        print ('error')

def sql_insert_producto(id_producto, nombre, marca, descripcion, categoria, costo, precio, cantidad):
    try:
        sql = f'insert into Productos(id_producto, nombre, marca, descripcion, categoria, costo, precio, cantidad) values ("{id_producto}","{nombre}",{marca},{descripcion},{categoria},{costo},{precio},{cantidad})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    

def sql_select_productos():
    try:
        strsql = "select * from Productos;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)
	

def sql_edit_productos(id_producto, nombre, marca, descripcion, categoria, costo, precio, cantidad):
    try:
        strsql = "update Productos set id_producto = '"+id_producto+"', nombre = '"+nombre+"', marca = "+marca+", descripcion = "+descripcion+", categoria = "+categoria+", costo = "+costo+", precio = "+precio+", cantidad = "+cantidad+" where id_producto = "+id_producto+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_productos(id):
    try:
        strsql = "delete from Productos where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	
# Proveedores

def sql_insert_proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono):
    try:
        sql = f'insert into Proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono) values ('"{id_proveedores}"',"{nombre}","{categoria}","{ciudad}","{direccion}","{telefono}")'
        #statement = "insert into Proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono) values ('?', ?, ?, ?, ?, ?)"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        #cursorObj.execute(statement, [id_proveedores , nombre, categoria, ciudad, direccion, telefono])
        con.commit()
        con.close()
    except Error as err:
        print(err)
    

def sql_select_proveedores():
    try:
        strsql = "select * from Proveedores;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)
	

def sql_edit_proveedores(id_proveedores, nombre, categoria, ciudad, direccion, telefono):
    try:
        strsql = "update Proveedores set id_proveedores = '"+id_proveedores+"', nombre = '"+nombre+"', categoria = "+categoria+", ciudad = "+ciudad+", direccion = "+direccion+", telefono = "+telefono+" where id = "+id_proveedores+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_proveedores(id_proveedores):
    try:
        strsql = "delete from Proveedores where id = "+id_proveedores+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

# Usuario

def sql_insert_usuarios(id, nombre, mail, perfil, usuario, passw):
    try:
        sql = f'insert into Usuarios(id, nombre, mail, perfil, usuario, passw) values ("{id}","{nombre}",{mail},{perfil},{usuario},{passw})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    

def sql_select_usuarios():
    try:
        strsql = "select * from Usuarios;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)
	

def sql_edit_usuarios(id, nombre, mail, perfil, usuario, passw):
    try:
        strsql = "update Usuarios set id = '"+id+"', nombre = '"+nombre+"', mail = "+mail+", perfil = "+perfil+", usuario = "+usuario+", passw = "+passw+" where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
	

def sql_delete_usuarios(id):
    try:
        strsql = "delete from Usuarios where id = "+id+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)
