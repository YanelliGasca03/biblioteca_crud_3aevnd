class Prestamo:
    #constructor 
    def __init__(self,id,id_libro,fecha_prestamo,fecha_devolucion):
        self.id = id
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def registrar_devolucion(self):
        self.devuelto = True
        print(f"El prestamo con ID {self.id} ha sido mascado como devuelto")
