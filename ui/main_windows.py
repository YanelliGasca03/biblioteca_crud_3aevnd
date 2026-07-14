import flet as ft

from ui.libro_form import libro_form 

def main_window(page: ft.Page):
    #configuracion de la pagina principal
    page.title = "Sistema de Gestión de Biblioteca"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #Widget etiqueta o Text
    titulo = ft.Text(
        "Sistema de Gestion de Biblioteca",
        size = 24,
        weight = ft.FontWeight.BOLD,
        color = ft.Colors.BLUE_GREY_800
    )

    subtitulo = ft.Text (
        "Seleccione una opción del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )


    #CONTENEDOR CENTRAL 
    contenido = ft.Container(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10
        ),
        padding = 30,
        expand = True
    )

    def insertar_libro(e):
        contenido.content = libro_form()
        page.update()
    #menu lateral
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding=20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                    
                ),
                ft.Text(
                    "Sistema de Gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                #BOTONES
                ft.ElevatedButton(
                    "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180,
                    on_click = insertar_libro
                ),
                ft.ElevatedButton(
                     "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180
                ),
                 ft.ElevatedButton(
                     "Préstamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180
                ), 
                ft.ElevatedButton(
                    "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),          
            ],
            spacing = 15
        )
    )

    #Definicion del layout de la página
    layout = ft.Row(
        controls = [
            menu_lateral,
            contenido
        ],
        expand = True
    )

    #agregar el layout a la pagina
    page.add(layout)