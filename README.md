<h1 align="center">Meditation Tracker API</h1>

<p align="justify">
A Django REST Framework project for recording meditation sessions.  
Users can log, edit, view, and delete their sessions, track consistency, and receive notifications when they reach the top of the leaderboard.
</p>

---

## About the Project

<p align="justify">
Capstone project to satisfy the requirements of the Back-end Web Development Program.  
This project was inspired by the <strong>ALX Tiny Habits Challenge</strong>, which emphasizes small, consistent daily actions.  
Meditation supports the focus, patience, and emotional balance that every ALX learner needs to stay grounded and productive throughout the program.  
The Meditation Tracker helps build that habit by making progress measurable and rewarding.
</p>

---

## Features

- Secure JWT-based authentication  
- Full CRUD functionality for meditation sessions  
- Automatic leaderboard ranking based on total meditation minutes  
- Notifications for top users  
- Pagination for long activity histories  

---

## Tech Stack

- **Framework:** Django 5+  
- **API Toolkit:** Django REST Framework  
- **Database:** SQLite (default)  
- **Authentication:** JWT (JSON Web Tokens)  

---

## API Endpoints with Examples

### Authentication

| Method | Endpoint | Description | Postman Example |
|--------|----------|-------------|----------------|
| POST | `/api/accounts/register/` | Register a new user | Body (raw JSON):<br>```{"username":"testuser","email":"testuser@example.com","password":"StrongPassword123"}``` |
| POST | `/api/accounts/login/` | Login with email and password | Body (raw JSON):<br>```{"email":"testuser@example.com","password":"StrongPassword123"}```<br>Response:<br>```json{"message":"Login was successful.","refresh":"<refresh_token>","access":"<access_token>","user":{"id":5,"username":"testuser","email":"testuser@example.com"}}``` |
| POST | `/api/accounts/logout/` | Logout user (if implemented) | Header: `Authorization: Bearer <access_token>` |

---

### Meditation Sessions

| Method | Endpoint | Description | Postman Example |
|--------|----------|-------------|----------------|
| GET | `/api/meditations/sessions/` | List all logged sessions | Header: `Authorization: Bearer <access_token>` |
| POST | `/api/meditations/sessions/` | Add a new meditation session | Header: `Authorization: Bearer <access_token>`<br>Body (raw JSON):<br>```{"meditation_type":"mindfulness","duration":25,"notes":"Morning calm session"}``` |
| GET | `/api/meditations/sessions/<id>/` | Retrieve one session | Header: `Authorization: Bearer <access_token>` |
| PUT / PATCH | `/api/meditations/sessions/<id>/` | Update a session | Header: `Authorization: Bearer <access_token>`<br>Body (raw JSON):<br>```{"duration":30,"notes":"Extended session"}``` |
| DELETE | `/api/meditations/sessions/<id>/` | Delete a session | Header: `Authorization: Bearer <access_token>` |

---

### Notifications

| Method | Endpoint | Description | Postman Example |
|--------|----------|-------------|----------------|
| GET | `/api/notifications/` | List notifications for current user | Header: `Authorization: Bearer <access_token>` |

---

## Example Postman Workflow

1. **Register User**  
   - POST `http://127.0.0.1:8000/api/accounts/register/`  
   - Body (raw JSON):  
   ```json
   {
     "username": "testuser",
     "email": "testuser@example.com",
     "password": "StrongPassword123"
   }
2. **Login** 
   - POST `http://127.0.0.1:8000/api/accounts/login/`  
   - Body (raw JSON): 
   ```json 
   {
     "email": "testuser@example.com",
     "password": "StrongPassword123"
   }
3. **Add a Meditation Session** 
   - POST `http://127.0.0.1:8000/api/meditations/sessions/`  
   - Header: Authorization: Bearer <access_token>
   - Body (raw JSON):  
   ```json
   {
    "meditation_type": "gratitude",
    "duration": 25,
    "notes": "Morning calm session"
   }

4. **Get All Meditation Sessions** 
   - POST `http://127.0.0.1:8000/api/meditations/sessions/` 
   - Header: Authorization: Bearer <access_token> 
   
5. **Update a Meditation Session** 
   - PATCH `http://127.0.0.1:8000/api/meditations/sessions/<id>/`  
   - Header: Authorization: Bearer <access_token>
   - Body (raw JSON):  
   ```json
   {
    "duration": 23,
   }

6. **DELETE All Meditation Sessions** 
   - DELETE `http://127.0.0.1:8000/api/meditations/sessions/` 
   - Header: Authorization: Bearer <access_token> 
   