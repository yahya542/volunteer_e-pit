import flet as ft


def db_pemilik(page: ft.Page):
    def create_menu(icon, label):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Icon(icon, size=30, color=ft.Colors.BLUE_800),
                    padding=15,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=10,
                ),
                ft.Text(label, size=12, text_align="center"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    

    header = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="https://i.imgur.com/FH0ZhG8.png", width=120),  # Ganti dengan logo e-PIT jika ada
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

    menu_grid = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=150,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10,
        controls=[
            create_menu(ft.Icons.DIRECTIONS_BOAT, "Profil\nKapal"),
            create_menu(ft.Icons.DATA_USAGE, "Kuota"),
            create_menu(ft.Icons.SYNC, "Operasi"),
            create_menu(ft.Icons.HISTORY, "History"),
            create_menu(ft.Icons.RECEIPT_LONG, "Invoice"),
            create_menu(ft.Icons.DESCRIPTION, "Dokumen\nKapal"),
            create_menu(ft.Icons.LINK, "Link\nLayanan"),
            create_menu(ft.Icons.HELP_OUTLINE, "Bantuan"),
            create_menu(ft.Icons.LOGOUT, "Logout"),
            create_menu(ft.Icons.NOTE_ADD_OUTLINED, "LPM\nTambahan"),
        ]
    )

    footer = ft.Container(
        content=ft.Text("PEMILIK KAPAL", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_500,
        padding=15,
        alignment=ft.alignment.center,
        border_radius=20,
        margin=ft.margin.only(top=20, left=30, right=30),
    )

    return ft.View(
        route="/dashboard",
        controls=[
            header,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            menu_grid,
            footer
        ],
        scroll=ft.ScrollMode.AUTO
    )
