import flet as ft
import csv
import os

# ชื่อไฟล์ CSV ที่จะใช้บันทึกข้อมูล
CSV_FILE = "registrations.csv"

def main(page: ft.Page):
    page.title = "แบบฟอร์มการรับสมัคร"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def save_to_csv(data):
        # ตรวจสอบว่าไฟล์ CSV มีอยู่แล้วหรือไม่
        is_file_exist = os.path.isfile(CSV_FILE)
        
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # ถ้าไฟล์ยังไม่มี ให้เขียนหัวข้อคอลัมน์ก่อน
            if not is_file_exist:
                writer.writerow(["ชื่อ-สกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
            
            # เขียนข้อมูลใหม่ลงในไฟล์
            writer.writerow(data)

    def submit_form(e):
        name = name_input.value
        phone = phone_input.value
        team = team_input.value

        # ตรวจสอบว่ามีการกรอกข้อมูลครบถ้วนหรือไม่
        if not name or not phone or not team:
            page.snack_bar = ft.SnackBar(ft.Text("กรุณากรอกข้อมูลให้ครบถ้วน"), open=True)
            page.update()
            return
        
        # เตรียมข้อมูลสำหรับบันทึก
        registration_data = [name, phone, team]
        
        # บันทึกข้อมูลลงในไฟล์ CSV
        try:
            save_to_csv(registration_data)
            
            # แสดงข้อความยืนยันการส่งข้อมูล
            page.snack_bar = ft.SnackBar(ft.Text("ส่งข้อมูลและบันทึกลงไฟล์สำเร็จ!"), open=True)
            
            # ล้างช่องกรอกข้อมูล
            name_input.value = ""
            phone_input.value = ""
            team_input.value = ""
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"เกิดข้อผิดพลาดในการบันทึก: {ex}"), open=True)
        
        page.update()
        
    # สร้างช่องกรอกข้อมูล (TextField)
    name_input = ft.TextField(
        label="ชื่อ-สกุล",
        hint_text="กรุณากรอกชื่อและนามสกุล",
        width=300
    )
    
    phone_input = ft.TextField(
        label="หมายเลขโทรศัพท์",
        hint_text="กรุณากรอกเบอร์โทรศัพท์",
        width=300
    )
    
    team_input = ft.TextField(
        label="ชื่อทีม",
        hint_text="กรุณากรอกชื่อทีม",
        width=300
    )

    # สร้างปุ่มสำหรับส่งข้อมูล
    submit_button = ft.ElevatedButton(
        text="ส่งข้อมูล",
        on_click=submit_form,
        width=300
    )

    # จัดวางองค์ประกอบทั้งหมดในหน้าเพจ
    page.add(
        ft.Column(
            controls=[
                ft.Text("แบบฟอร์มการรับสมัคร", size=24, weight="bold"),
                name_input,
                phone_input,
                team_input,
                submit_button
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)