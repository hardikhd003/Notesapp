# Notes App (Full Stack)

## Overview

This is a full-stack Notes Application built using FastAPI for the backend and React for the frontend.
It allows users to register, login, and manage their personal notes securely.

---

## Tech Stack

* **Backend:** FastAPI
* **Frontend:** React
* **Database:** SQLite
* **Authentication:** JWT (JSON Web Token)

---

## Features

* User Registration & Login
* Secure Authentication using JWT
* Create Notes
* View Notes (user-specific)
* Update & Delete Notes

---

## Backend Setup

1. Navigate to project folder
2. Activate virtual environment
3. Run server:

uvicorn main:app --reload

4. Open API docs:
   http://127.0.0.1:8000/docs

---

## Frontend Setup

1. Navigate to frontend folder

cd frontend

2. Install dependencies

npm install

3. Run frontend

npm start

---

## Live Backend Link

(https://notesapp-skyq.onrender.com)

---

## API Endpoints

### Auth

* POST /register
* POST /login

### Notes

* GET /notes
* POST /notes
* PUT /notes/{id}
* DELETE /notes/{id}

---

## Notes

* SQLite is used for quick setup and development
* Can be easily migrated to MySQL/PostgreSQL
* CORS enabled for frontend-backend communication

---

## Author

Developed as part of a full-stack assignment.
