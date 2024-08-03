import flet as ft
from models import update_preflop_raise


class RangeData(ft.Column):
    def __init__(self, matrix):
        super().__init__(alignment=ft.alignment.top_center)
        self.matrix = matrix
        self.text = ft.Text('', size=40)
        self.position = self.create_radio_group(["EP", "MP", "HJ", "CO", "BTN", "SB", "BB"])
        self.vs_position = self.create_radio_group(["EP", "MP", "HJ", "CO", "BTN", "SB"])
        self.controls.extend([self.text, self.position, self.vs_position, ChangePositionButton(self),
                              SaveButton(self)
                              ])

    @staticmethod
    def create_radio_group(values):
        return ft.RadioGroup(
            content=ft.Row([ft.Radio(value=value, label=value) for value in values], spacing=0)
        )

    def change_position(self):
        self.position.value = "HJ"
        self.update()

    def save_range(self):
        preflop_raise = []
        call = []
        fold = []
        all_in = []
        for x in self.matrix.controls:
            for zap in x.controls:
                if zap.content.bgcolor == '#8f2e2e':
                    preflop_raise.append(zap.content.content.value)
                if zap.content.bgcolor == '#136930':
                    call.append(zap.content.content.value)
                if zap.content.bgcolor == 'blue':
                    fold.append(zap.content.content.value)
                if zap.content.bgcolor == '#f700ff':
                    all_in.append(zap.content.content.value)

        update_preflop_raise(range_name=self.text.value,
                             preflop_raise=preflop_raise,
                             all_in=all_in,
                             fold=fold, call=call)






class SaveButton(ft.ElevatedButton):
    def __init__(self, parent):
        super().__init__(text="Сохранить", on_click=self.save)
        self.parent = parent

    def save(self, e):
        self.parent.save_range()



class ChangePositionButton(ft.ElevatedButton):
    def __init__(self, parent):
        super().__init__(text="Change Position to HJ", on_click=self.change_position)
        self.parent = parent

    def change_position(self, e):
        self.parent.change_position()


