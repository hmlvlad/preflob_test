import flet as ft


def NavBar(page):
    NavBar = ft.AppBar(
            leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
            leading_width=40,
            title=ft.Text("Flet Router"),
            center_title=False,
            bgcolor=ft.colors.ON_SECONDARY,
            actions=[
                ft.IconButton(ft.icons.HOME,),
                ft.IconButton(ft.icons.PERSON_ROUNDED,),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED)
            ]
        )

    return NavBar