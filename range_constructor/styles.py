import flet as ft


class Styles:
    """Класс для хранения стилей приложения"""
    TEXT_STYLE = ft.TextStyle(
        font_family='Open_sans',
        shadow=ft.BoxShadow(
            spread_radius=0,
            color=ft.colors.BLACK,
            offset=ft.Offset(1, 1),
            blur_style=ft.ShadowBlurStyle.SOLID,
        )
    )

    CONTAINER_SHADOW = ft.BoxShadow(
        spread_radius=0,
        color=ft.colors.BLACK,
        offset=ft.Offset(1, 1),
        blur_style=ft.ShadowBlurStyle.SOLID,
    )

    CONTAINER_BG_COLOR = '#555657'
    ACTION_COLOR = 'blue'
    TEXT_SIZE = 12
    CONTAINER_SIZE = 35
    BORDER_RADIUS = 2
