import flet as ft
from range_constructor.styles import Styles
from matrix import matrix


class ColorChanger:
    def __init__(self):
        self.last_cell_color = ''
        self.is_pan_active = False
        self.action_color = 'blue'

    def change_active_color(self, color):
        self.action_color = color

    def change_color(self, e, color):
        e.control.content.bgcolor = color
        self.last_cell_color = e.control.content.bgcolor
        e.control.update()

    def pan_start(self, e):
        if self.is_pan_active and e.control.content.bgcolor != self.last_cell_color:
            self.toggle_color(e)

    def pan_true(self, e):
        self.is_pan_active = True
        self.toggle_color(e)

    def pan_false(self, e):
        self.is_pan_active = False

    def toggle_color(self, e):
        if e.control.content.bgcolor == self.action_color:
            self.change_color(e, Styles.CONTAINER_BG_COLOR)
        else:
            self.change_color(e, self.action_color)


class Matrix(ft.Column):
    def __init__(self):
        super().__init__(spacing=2)
        self.color_changer = ColorChanger()
        self.create_matrix()

    def create_matrix(self):
        for h in matrix:
            row = ft.Row(spacing=2)
            for z in h:
                hand = ft.GestureDetector(
                    on_enter=self.color_changer.pan_start,
                    on_pan_start=self.color_changer.pan_true,
                    on_pan_end=self.color_changer.pan_false,
                    content=ft.Container(
                        content=ft.Text(value=z, size=Styles.TEXT_SIZE, color='white', style=Styles.TEXT_STYLE),
                        shadow=Styles.CONTAINER_SHADOW,
                        bgcolor=Styles.CONTAINER_BG_COLOR,
                        width=Styles.CONTAINER_SIZE,
                        height=Styles.CONTAINER_SIZE,
                        border_radius=Styles.BORDER_RADIUS,
                        alignment=ft.alignment.center,
                    )
                )
                row.controls.append(hand)
            self.controls.append(row)


