# Clase usuario

from models.libro import Libro

class Usuario:
    
    def __init__(self, id, nombre, matricula, carrera, correo, activo=True):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.activo = activo

    def activar(self):
        self.activo = True
        print(f"El usuario {self.nombre} ha sido activdado")

    def desactivar(self):
        self.activo = False
        print(f"El usuario {self.nombre} ha sido desactivdado")

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo" 
        return f"{self.nombre} - {self.carrera} : {estado}" 