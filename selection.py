from InquirerPy import inquirer
from InquirerPy.base.control import Choice

# กำหนดรายการตัวเลือก
choices_list = [
    Choice(value="frontend", name="สร้างเว็บไซต์ (Front-end)"),
    Choice(value="backend", name="สร้าง API/เซิร์ฟเวอร์ (Back-end)"),
    Choice(value="database", name="จัดการฐานข้อมูล"),
    Choice(value=None, name="ยกเลิกการตั้งค่า"),
]

# ใช้ inquirer.select เพื่อสร้างเมนูแบบเลื่อนขึ้นลง
result = inquirer.select(
    message="กรุณาเลือกประเภทของโปรเจกต์:",
    choices=choices_list,
    default=None, # ตัวเลือกที่ถูกเลือกไว้ล่วงหน้า
    # "list" คือรูปแบบที่ทำให้เลื่อนขึ้นลงได้
).execute() 

if result:
    print(f"คุณเลือก: {result.upper()}")
else:
    print("ยกเลิกการตั้งค่า")