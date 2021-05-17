# Chava
# 1. เปิด command prompt

# 2. สร้างโฟลเดอร์ใหม่
mkdir project

# 3. เปิดโฟลเดอร์ที่สร้าง
cd project

# 4. ติดตั้ง Django
conda create -n dsi202 python=3.6
conda activate dsi202
conda install django=2.2

# 5. ติดตั้งแพ็คเกจเพิ่มเติม
pip install django-shopping-cart

# 6. ติดตั้งไฟล์ที่ได้ทำการอัพโหลดไว้ โดยติดตั้งในโฟลเดอร์ที่ได้สร้างไว้ในdsi202 ชื่อ myproject
# โดยติดตั้ง models.py , forms.py , admin.py , apps.py , views.py , static , migrations , templates ไว้ในโฟลเดอร์ myapp ใน myproject
# และติดตั้ง settings.py , urls.py , ใน myproject ใน myproject 

# 7. เปิดโฟล์เดอร์ที่ติดตั้ง
cd myproject

# 8. สร้าง superser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 9. runserver
python manage.py runserver

#
#
#
#
#
#
#
#
#
#
#
#
