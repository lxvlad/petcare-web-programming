# 🐾 PetCare — сервіс для власників тварин

**Ідея:** веб-додаток для реєстрації домашніх улюбленців, ведення щеплень, годування, нотаток і нагадувань про візит до ветеринара.  
Проєкт складається з двох частин:
- **Back-end:** Django + Django REST Framework (API, база даних);
- **Front-end:** React + TypeScript (інтерфейс користувача).

---

## 📦 Структура проєкту

petcare/
├── backend/ # Django + DRF (API, база даних)
│ ├── core/ # моделі, views, urls
│ ├── manage.py
│ └── requirements.txt
└── frontend/ # React + TypeScript (UI)
├── src/
├── package.json
└── vite.config.ts

---

## ⚙️ Технології

| Частина | Технології |
|----------|-------------|
| Back-end | Django 5, Django REST Framework, CORS Headers |
| Front-end | React 18, TypeScript, Vite, Axios, React Router DOM |
| База даних | SQLite (за замовчуванням), можна PostgreSQL |
| Dev tools | Node ≥18, Python ≥3.10 |

---

## 🧠 Робота з віртуальним середовищем (macOS / Windows)

### macOS
```bash
# 1️⃣ Створення середовища (перший раз)
python3 -m venv .venv

# 2️⃣ Активація середовища (кожного разу, коли відкриваєш новий термінал)
source .venv/bin/activate

# 3️⃣ Встановлення бібліотек (перший раз або після змін у requirements.txt)
pip install -r requirements.txt

# 4️⃣ Запуск Django сервера
python manage.py migrate
python manage.py runserver

### Windows

# 1️⃣ Створення середовища
py -3 -m venv .venv

# 2️⃣ Активація
.\.venv\Scripts\Activate.ps1

# 3️⃣ Встановлення бібліотек
pip install -r requirements.txt

# 4️⃣ Запуск Django сервера
python manage.py migrate
python manage.py runserver


## 🚀 Запуск фронтенду

cd frontend
npm install
npm run dev

бекенд — http://localhost:8000/api
фронтенд — http://localhost:5173