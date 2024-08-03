import flet as ft
from models import Folders, Files, app, find_range_by_name


class Ranges(ft.Column):
    def __init__(self, matrix, range_data):
        super().__init__()
        self.width = 400
        self.spacing = 0
        self.create_folder_view(self)
        self.matrix = matrix
        self.range_data = range_data

    def get_hands(self, e):
        ranges = find_range_by_name(e)
        preflop_raise = ranges.preflop_raise.split() if ranges.preflop_raise is not None else []
        call = ranges.call.split() if ranges.call is not None else []
        all_in = ranges.all_in.split() if ranges.all_in is not None else []
        fold = ranges.fold.split() if ranges.fold is not None else []
        for x in self.matrix.controls:
            for zap in x.controls:
                if zap.content.content.value in preflop_raise:
                    zap.content.bgcolor = '#8f2e2e'
                elif zap.content.content.value in all_in:
                    zap.content.bgcolor = '#f700ff'
                elif zap.content.content.value in fold:
                    zap.content.bgcolor = 'blue'
                elif zap.content.content.value in call:
                    zap.content.bgcolor = '#136930'
                else:
                    zap.content.bgcolor = '#555657'
        # self.range_data.value = 'qqqqqqq'
        # print(e)
        self.range_data.controls[0].value = e
        self.matrix.update()
        self.range_data.update()

    def create_folder_view(self, parent_control: object, folder_id: object = None) -> None:
        with app.app_context():
            folders = Folders.query.filter_by(parent_folder_id=folder_id).all()
            for folder in folders:
                folder_tile = ft.ExpansionTile(title=ft.Text(folder.folder_name))
                parent_control.controls.append(folder_tile)

                self.create_folder_view(folder_tile, folder.id)
            files = Files.query.filter_by(folder_id=folder_id).all()
            for file in files:
                file_tile = ft.ListTile(
                    title=ft.Text(file.file_name),
                    on_click=lambda e, file_name=file.file_name: self.get_hands(file_name)
                )
                parent_control.controls.append(file_tile)
            parent_control.controls.append(ft.Container(content=ft.Text('+', size=30,),
                                                        alignment=ft.alignment.center, on_click=self.puk))

    def puk(self, e):
        print("puk")