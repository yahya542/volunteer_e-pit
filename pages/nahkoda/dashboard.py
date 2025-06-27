
import flet as ft

def db_nahkoda(page: ft.Page, go_to):
    return ft.Column([
        ft.Text("Ini menu dashboard untuk nahkoda", size=30, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("Kembali", on_click=lambda e: go_to("home"))
    ], alignment=ft.MainAxisAlignment.CENTER)

#test