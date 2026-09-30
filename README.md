# SheShield — Women Safety Alert System

A creative, responsive educational project for 3rd-year students using **React JS + Python Django**. MySQL is listed as a possible future extension, but this version deliberately uses **no database**.

## Project modules
- Dashboard / Safety Command Centre
- One-tap SOS demo workflow
- Emergency / trusted contacts
- Safety resources and safe zones
- Incident reporting form
- Internship & opportunity search hub
- Safety toolkit / awareness tips
- Alert history timeline
- Responsive mobile/tablet/desktop UI
- Django REST-style JSON endpoints
- No migrations and no database setup

## Folder structure
```
SheShield/
├── frontend/       # React + Vite UI
├── backend/        # Django API
├── docs/           # Project documentation placeholders
└── README.md
```

## Run frontend (VS Code Terminal)
1. Open the `frontend` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run:
```bash
npm install
npm run dev
```
4. Open the localhost URL shown by Vite (normally `http://localhost:5173`).

## Run Django API (optional)
Open a second VS Code terminal:
```bash
cd backend
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```
Then check `http://127.0.0.1:8000/api/health/`.

### Important
- **Do NOT run `python manage.py migrate`.** There is intentionally no database configuration.
- The frontend currently contains demo data so it can be run independently.
- The Django API is included to demonstrate the React → Django architecture and can be connected to the frontend later.
- The SOS feature is a simulation. It does not send real emergency messages.
- Sample contact numbers/data are placeholders and must be replaced with verified information in any real deployment.

## Suggested student presentation flow
1. Problem statement: emergency response can be slow or fragmented.
2. Proposed solution: a single student-friendly safety command centre.
3. Frontend: React components, state, routing-style navigation, responsive CSS.
4. Backend: Django JSON APIs.
5. Database decision: intentionally omitted for this version; future scope can use MySQL.
6. Future scope: authentication, real-time location, SMS/WhatsApp integration, map APIs, encrypted reports, admin dashboard, MySQL, audit logs and role-based access.
