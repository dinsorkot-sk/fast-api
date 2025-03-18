# 🚀 FastAPI + MySQL + Alembic CRUD API

## 📌 รายละเอียดโปรเจค
โปรเจคนี้เป็น API ที่พัฒนาโดยใช้ **FastAPI** และ **SQLAlchemy** เชื่อมต่อกับฐานข้อมูล **MySQL** รองรับ **CRUD (Create, Read, Update, Delete)** สำหรับตาราง `users` และใช้ **Alembic** สำหรับการจัดการ Migration

---
## 🔧 การติดตั้ง

### 1️⃣ **Clone โปรเจค**
```bash
git clone https://github.com/your-repo/fastapi-mysql-crud.git
cd fastapi-mysql-crud
```

### 2️⃣ **สร้าง virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **ติดตั้ง Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **ตั้งค่าไฟล์ .env**
สร้างไฟล์ `.env` และกำหนดค่าต่อไปนี้:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=
DB_NAME=fast_api
```

### 5️⃣ **ตั้งค่า Database และ Alembic**
```bash
alembic upgrade head  # รัน Migration เพื่อสร้างตารางในฐานข้อมูล
```

---
## 🚀 การรันเซิร์ฟเวอร์
```bash
uvicorn app.main:app --reload
```
เซิร์ฟเวอร์จะเริ่มต้นที่ `http://127.0.0.1:8000/`

---
## 🔥 การทดสอบ API
### 📌 1. สร้างผู้ใช้ใหม่ (POST)
```bash
curl -X POST "http://127.0.0.1:8000/api/users" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "age": 30}'
```

### 📌 2. ค้นหาผู้ใช้ทั้งหมด (GET)
```bash
curl -X GET "http://127.0.0.1:8000/api/users"
```

### 📌 3. ค้นหาผู้ใช้ตาม ID (GET)
```bash
curl -X GET "http://127.0.0.1:8000/api/users/1"
```

### 📌 4. อัปเดตข้อมูลผู้ใช้ (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/api/users/1" -H "Content-Type: application/json" -d '{"name": "John Updated", "age": 35}'
```

### 📌 5. ลบผู้ใช้ (DELETE)
```bash
curl -X DELETE "http://127.0.0.1:8000/api/users/1"
```

---
## 🎯 โครงสร้างโปรเจค
```
fastapi_project/
│── app/
│   ├── controllers/
│   │   ├── user_controller.py
│   ├── models/
│   │   ├── database.py
│   │   ├── user_model.py
│   ├── schemas/
│   │   ├── user_schema.py
│   ├── views/
│   │   ├── user_view.py
│   ├── main.py
│── migrations/
│── .env
│── requirements.txt
│── README.md
```

---
## 🎉 สรุป
- ✅ **FastAPI + MySQL + Alembic**
- ✅ **CRUD API สำหรับตาราง `users`**
- ✅ **รองรับการทำ Migration ด้วย Alembic**
- ✅ **API พร้อมใช้งาน และทดสอบได้ง่าย**

🚀 **ขอให้สนุกกับการใช้งาน!** 🎉