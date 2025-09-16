import flet as ft
import re

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_button_click(e):
        current_value = result.value
        button_text = e.control.text
        
        if button_text == "=":
            try:
                # แก้ไขการแทนที่เครื่องหมายเพื่อให้ eval() ทำงานได้
                expression = current_value.replace("×", "*").replace("÷", "/")
                expression = expression.replace("^", "**")
                # เปลี่ยน % เป็น /100 (รองรับกรณี 50% หรือ 50+10%)
                expression = re.sub(r"(\d+)%", r"(\1/100)", expression)
                result.value = str(eval(expression))
            except (SyntaxError, ZeroDivisionError, Exception):
                result.value = "Error"
        elif button_text == "C":
            result.value = ""
        else:
            result.value += button_text
        
        page.update()

    result = ft.TextField(
        read_only=True,
        text_align="right",
        value="",
        expand=True,
        border_radius=10,
        text_size=24,
    )

    # สร้างปุ่มสำหรับตัวเลขและเครื่องหมาย
    buttons = [
        ["(", ")", "%", "^"],
        ["7", "8", "9", "÷"],
        ["4", "5", "6", "×"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    # สร้าง UI ของเครื่องคิดเลข
    layout = ft.Column(
        controls=[
            ft.Row(
                controls=[result],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Column(
                spacing=5,
                controls=[
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text=text, on_click=on_button_click, expand=True, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))) 
                            for text in row
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                    for row in buttons
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)