# DBD API Project

ระบบเรียก API กรมพัฒนาธุรกิจการค้า (DBD) สำหรับดึงข้อมูลผู้ถือหุ้น (Shareholder) และบันทึกไฟล์ PDF

- **Backend**: Python + FastAPI
- **Frontend**: Vue 3 + Vite
- **Database**: Microsoft SQL Server (LocalDB)

---

## Requirements

| Tool | Version |
|------|---------|
| Python | >= 3.11 |
| Node.js | ^20.19.0 หรือ >= 22.12.0 |
| SQL Server / LocalDB | - |
| ODBC Driver 17 for SQL Server | - |

---

## การติดตั้งและรันโปรเจกต์

### 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

---

### 2. ตั้งค่า Backend (FastAPI)

#### 2.1 สร้าง Virtual Environment

```bash
cd BackEnd
python -m venv venv
```

#### 2.2 Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

#### 2.3 ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

#### 2.4 สร้างไฟล์ Config

สร้างไฟล์ `app/config.py` (ไฟล์นี้ถูก ignore ใน git):

```python
BDEX_CONSUMER_KEY    = "your_consumer_key"
BDEX_CONSUMER_SECRET = "your_consumer_secret"
BDEX_TOKEN_URL       = "https://api-sandbox.dbd.go.th/auth/oauth/v2/token"
CREATE_JOB_URL       = "https://api-sandbox.dbd.go.th/image/ShareHolder/v1/CreateJobSHLimage"
```

#### 2.5 ตั้งค่า Database

แก้ไข `app/database.py` ให้ตรงกับ SQL Server ของคุณ:

```python
SERVER   = "(localdb)\\TestTB"   # เปลี่ยนตามเครื่องของคุณ
DATABASE = "DBDAPI"
```

> ตรวจสอบว่าติดตั้ง **ODBC Driver 17 for SQL Server** แล้ว  
> ดาวน์โหลดได้ที่: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

#### 2.6 รัน Backend

```bash
uvicorn app.main:app --reload
```

Backend จะรันที่ `http://127.0.0.1:8000`

ตรวจสอบ API docs ได้ที่ `http://127.0.0.1:8000/docs`

---

### 3. ตั้งค่า Frontend (Vue 3)

#### 3.1 ติดตั้ง Dependencies

```bash
cd FrontEnd
npm install
```

#### 3.2 รัน Frontend

```bash
npm run dev
```

Frontend จะรันที่ `http://localhost:5173`

---

## โครงสร้างโปรเจกต์

```
project/
├── BackEnd/
│   ├── app/
│   │   ├── main.py                  # FastAPI app + CORS
│   │   ├── config.py                # API keys (ไม่อยู่ใน git)
│   │   ├── database.py              # SQLAlchemy connection
│   │   ├── logging_config.py        # Logger (บันทึก log รายวัน)
│   │   ├── models/
│   │   │   ├── InquirySHL_model.py  # Pydantic model สำหรับ BDEX response
│   │   │   └── profile_req_log.py   # SQLAlchemy model
│   │   ├── routers/
│   │   │   ├── bdex_router.py       # /bdex/*
│   │   │   ├── InquirySHL_router.py # /InquirySHL/*
│   │   │   ├── profile_req_log.py   # /profile-log/*
│   │   │   └── book.py              # /book/* (ตัวอย่าง)
│   │   ├── services/
│   │   │   ├── bdex_service.py      # เรียก BDEX Token + CreateJob API
│   │   │   ├── InquirySHL_service.py# ดึงข้อมูล + บันทึก PDF
│   │   │   ├── pdf_service.py       # decode base64 → บันทึกไฟล์ PDF
│   │   │   ├── hash_service.py      # ตรวจสอบ SHA-256
│   │   │   └── profile_req_log_service.py
│   │   └── mock_data/               # ข้อมูล mock สำหรับทดสอบ
│   ├── logs/                        # log รายวัน (ไม่อยู่ใน git)
│   ├── venv/                        # virtual environment (ไม่อยู่ใน git)
│   └── requirements.txt
│
└── FrontEnd/
    ├── src/
    │   ├── App.vue                  # หน้าหลัก (เรียก SavePDF API)
    │   ├── main.js
    │   ├── router/
    │   └── stores/
    ├── package.json
    └── vite.config.js
```

---

## API Endpoints

| Method | Endpoint | คำอธิบาย |
|--------|----------|-----------|
| `GET` | `/bdex/token` | ขอ Access Token จาก BDEX |
| `POST` | `/bdex/shareholder-image?org_id=xxx` | สร้าง Job ดึงรูปผู้ถือหุ้น |
| `POST` | `/InquirySHL/SavePDF` | บันทึกไฟล์ PDF จาก mock data |
| `GET` | `/profile-log/` | ดู log การเรียก API |
| `GET` | `/book/` | ตัวอย่าง CRUD |

---

## การแก้ไขปัญหาเบื้องต้น

**Backend ไม่ start — `ModuleNotFoundError`**
```bash
# ตรวจสอบว่า activate venv แล้ว
venv\Scripts\activate
pip install -r requirements.txt
```

**เชื่อม Database ไม่ได้**
- ตรวจสอบชื่อ `SERVER` และ `DATABASE` ใน `database.py`
- ตรวจสอบว่าติดตั้ง ODBC Driver 17 แล้ว
- ตรวจสอบว่า SQL Server / LocalDB กำลังรันอยู่

**Frontend เรียก API แล้ว CORS error**
- ตรวจสอบว่า Backend รันที่ `http://127.0.0.1:8000`
- ตรวจสอบ `origins` ใน `main.py` ว่ามี `http://localhost:5173`