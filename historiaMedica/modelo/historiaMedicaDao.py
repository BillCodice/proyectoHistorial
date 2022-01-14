from sqlite3.dbapi2 import Cursor
from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaMedica, p.nombre || " " || p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.motivo, h.examenAuxiliar, h.tratamiento, h.detalle FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)

    return listaHistoria

def guardarHistoria(idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{examenAuxiliar}','{tratamiento}','{detalle}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Medica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Medica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia medica'
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = '{fechaHistoria}', motivo = '{motivo}', examenAuxiliar = '{examenAuxiliar}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia medica'
        messagebox.showerror(title, mensaje)

class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.tratamiento = tratamiento
        self.detalle = detalle
    
    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo}, {self.examenAuxiliar}, {self.tratamiento}, {self.detalle}]'