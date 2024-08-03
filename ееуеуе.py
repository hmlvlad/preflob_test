import flet as ft

def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.CupertinoSegmentedButton(
            selected_index=1,
            selected_color=ft.colors.RED_400,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Text("One"),
                ft.Container(
                    padding=ft.padding.symmetric(0, 30),
                    content=ft.Text("Two"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(0, 10),
                    content=ft.Text("Three"),
                ),
            ],
        ),
    )

ft.app(main)