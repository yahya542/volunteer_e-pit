import flet as ft
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pages.pemilik.dashboard import db_pemilik as pemilik

def login(page: ft.Page):
    def go_to_dashboard(e):
        page.views.append(pemilik(page))
        page.go("/dashboard")

    # Header atas
    header = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="https://i.imgur.com/FH0ZhG8.png", width=120),
                ft.Text("SAMUDERA-1", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("BAGASKARA", size=14),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.BLUE_400,
        border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30),
        padding=20,
        alignment=ft.alignment.center,
    )

    # Footer / bagian bawah halaman
    footer = ft.Text(
        "Selamat Datang di e-PIT",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK12,
        
        text_align=ft.TextAlign.CENTER,
        width=400,
        height=40,
        
    )
    
    db_pemilik = ft.ElevatedButton(
        "Masuk Dashboard", on_click=go_to_dashboard,
        

                                   
    )


    # Kembalikan satu View
    return ft.View(
        route="/login",
        controls=[
            header,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            footer,
            db_pemilik
        ],
        scroll=ft.ScrollMode.AUTO
    )
