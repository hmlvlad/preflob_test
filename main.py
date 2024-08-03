import flet as ft
from range_constructor.range_matrix import Matrix
from range_constructor.ranges import Ranges
from range_constructor.range_data import RangeData
from range_constructor.action import Action, Clear
from appbar import NavBar


class App:
    def __init__(self):
        self.matrix = Matrix()
        self.clear_btn = Clear(self.matrix)
        self.settings = RangeData(self.matrix)
        self.folder_view = Ranges(self.matrix, self.settings)

    def main(self, page: ft.Page) -> None:
        app_layout = ft.Row(
            controls=[
                ft.Container(content=self.folder_view, alignment=ft.alignment.center),
                ft.Column(
                    controls=[
                        self.matrix,
                        ft.Container(content=Action(self.matrix.color_changer), alignment=ft.alignment.center),
                        self.clear_btn
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(content=self.settings, alignment=ft.alignment.center),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        page.add(app_layout)


def main(page: ft.Page) -> None:
    page.appbar = NavBar(page)
    app = App()
    app.main(page)


if __name__ == "__main__":
    ft.app(target=main)