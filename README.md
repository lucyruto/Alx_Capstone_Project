
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

- Secure user authentication (session or token based)  
- Full CRUD functionality for meditation sessions  
- Automatic leaderboard ranking based on total meditation minutes  
- Notifications for top users  
- Pagination for long activity histories  
- Default Django REST security settings enabled  

---

## Tech Stack

- **Framework:** Django 5+  
- **API Toolkit:** Django REST Framework  
- **Database:** SQLite (default)  
- **Authentication:** Session / Token  

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api-auth/login/` | Log in with username and password |
| POST | `/api-auth/logout/` | Log out |

### Meditation Sessions

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/sessions/` | View all logged sessions (paginated) |
| POST | `/api/sessions/` | Add a new meditation session |
| GET | `/api/sessions/<id>/` | Retrieve details of one session |
| PUT/PATCH | `/api/sessions/<id>/` | Update a session |
| DELETE | `/api/sessions/<id>/` | Delete a session |

**Example Request**
```json
POST /api/sessions/
{
  "meditation_type": "mindfulness",
  "duration": 25,
  "notes": "Morning calm session"
}
