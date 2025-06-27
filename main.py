import flet as ft
from pages.auth.login import login as lp

def main(page: ft.Page):
    page.title = "e-PIT"
    page.theme_mode = ft.ThemeMode.LIGHT

    
    
    def login(e):
        page.views.append(lp(page))
        page.go("/login")
    
    

    page.views.clear()
    page.views.append(
        ft.View(
            route="/",
            controls=[
                ft.Text("Selamat Datang di e-PIT", size=20),
                ft.ElevatedButton("login", on_click=login),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.go(page.route)

ft.app(target=main)
