from database import conexion
from database.conexion import Conexion
from models.libro import Libro


class LibroDAO:
    def obtener_libros(self):


        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
            SELECT 
                libro.id_libro,
                libro.titulo,
                autor.nombre as autor,
                libro.isbn,
                libro.disponible
            FROM libro
            INNER JOIN autor
            ON libro.autor = autor.id 
            '''

        cursor.execute(sql)
        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro(id=registro[0], titulo=registro[1], autor=registro[2], isbn=registro[3], disponible=registro[4])
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros
        

    def insertar(self,libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """"
        INSER INTO libro (titulo, autor, isb, disponible)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self,libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """"
        UPDATE libro
        SET titulo = %s, autor = %s, 
        isbn = %s, disponible = %s
        WHERE id = %s
        """
        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible,
            libro.id
        ))
    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s",
            (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
#UPDATE
    def actualizar(self,libro):
         conexion = conexion.obtener_conexion()
         cursor = conexion.cursor()
         sql = """"
         UPDATE libro
         SET titulo=%s, autor=%s, isbn=%s, disponible=%s
         
         """


