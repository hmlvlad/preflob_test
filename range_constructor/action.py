import flet as ft


class Action(ft.CupertinoSegmentedButton):
    def __init__(self, matrix):
        self.matrix = matrix
        controls = [
            ft.Container(
                content=ft.Text("FOLD"),
                width=100,
                height=50,
                alignment=ft.alignment.center,
                data='blue',
            ),
            ft.Container(
                content=ft.Text("CALL"),
                width=100,
                height=50,
                alignment=ft.alignment.center,
                data='#136930'
            ),
            ft.Container(
                content=ft.Text("RAISE"),
                width=100,
                height=50,
                alignment=ft.alignment.center,
                data='#8f2e2e'
            ),
            ft.Container(
                content=ft.Text("ALLIN"),
                width=100,
                height=50,
                alignment=ft.alignment.center,
                data='#f700ff'
            ),
        ]
        super().__init__(controls=controls)
        self.padding = 0
        self.unselected_color = '#555657'
        self.selected_color = 'black'
        self.border_color = 'black'
        self.on_change = self.change_cube_color

    def change_cube_color(self, e):
        """Изменить цвет куба при выборе действия"""
        selected_segment = self.controls[e.control.selected_index]
        self.matrix.change_active_color(selected_segment.data)
        # print(e.control.selected_index)


class Clear(ft.CupertinoButton):
    def __init__(self, matrix):
        super().__init__()
        self.matrix = matrix
        self.width = 120
        self.height = 50
        self.on_click = self.clear
        self.text = 'Очистить'

    def clear(self, e):
        for x in self.matrix.controls:
            for zap in x.controls:
                zap.content.bgcolor = '#555657'
        self.matrix.update()


