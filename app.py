 from DAO import usuario_dao
from DAO.libro_dao import LibroDAO 
from models.libro import Libro
from models.usuario import Usuario, UsuarioDAO
def ver_todo(libro_dao):
    try:
        libros = libro_dao.obtener_libros()

        print("Libros en la biblioteca")
        if len(libros) == 0:
            print("No hay libros en la biblioteca")
        else:
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor} - {libro.disponible}")
        
        print ("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:

        print ("*************************")
        print("Inserccion a un nuevo libro")
        titulo = input("Escribe el título del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        nuevoLibro =Libro(8,titulo,autor,isbn,disponible)
        libro_dao.insertar(nuevoLibro)

    except Exception as e:
      
         print(f"Error al conectar a la base de datos: {e}")

def actualizar_libro(libro_dao):

    ver_todo(libro_dao)
    id =int(input("Escribe el id del libro a editar: "))
    print("Actualiza los datos de este libro")
    titulo = input("Escribe el titulo del libro: ")
    autor = int(input("Escribe el nuevo id del autor: "))
    isbn = input("Escribe el nuevo isbn del libro: ")
    disponible = bool(input("Escribe si el libro esta disponible o no: "))
    libro = Libro(id,titulo,autor,isbn,disponible)
    libro_dao.actualizar(libro)

def eliminar_libro(libro_dao):
    ver_todo(libro_dao)
    id =int(input("Escribe el id del libro a eliminar: "))
    libro_dao.eliminar(id)
    print("Libros disponibles")
    ver_todo(libro_dao)

def main():
    print("Biblioteca universitaria")
    libro_dao = LibroDAO()

    #Imprime menu de opciones
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion =int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1: ver_todo(libro_dao)            
        case 2: insertar_libro(libro_dao)
        case 3: actualizar_libro(libro_dao)
        case 4: eliminar_libro(libro_dao)

    main()
def ver_usuarios(usuario_dao):

    try:
        usuarios = usuario_dao.obtener_usuarios()

        print("\n===== USUARIOS =====")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print(f"{usuario.id} - {usuario.matricula} - {usuario.nombre} - {usuario.carrera}")

    except Exception as e:
        print(f"Error: {e}")
    
def insertar_usuario(usuario_dao):

    print("\n NUEVO USUARIO ")

    matricula = input("Matrícula: ")
    nombre = input("Nombre: ")
    carrera = input("Carrera: ")

    usuario = Usuario(0, matricula, nombre, carrera)

    usuario_dao.insertar(usuario)

print("Usuario agregado correctamente.")


def actualizar_usuario(usuario_dao):

    ver_usuarios(usuario_dao)

    id = int(input("\nId del usuario: "))
    matricula = input("Nueva matrícula: ")
    nombre = input("Nuevo nombre: ")
    carrera = input("Nueva carrera: ")

    usuario = Usuario(id, matricula, nombre, carrera)
    usuario_dao.actualizar(usuario)

    print("Usuario actualizado.")


def eliminar_usuario(usuario_dao):

    ver_usuarios(usuario_dao)

    id = int(input("\nId del usuario a eliminar: "))

    usuario_dao.eliminar(id)

    print("Usuario eliminado.")


