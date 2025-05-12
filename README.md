# Remind-me-later API

This is a simple REST API built with Flask that allows users to schedule reminders with a message, time, date, and a reminder type (SMS or Email). The focus of this project is to persist reminder data in a database — actual delivery of reminders is out of scope.

---

## Features

- ✅ Create and save reminders
- ✅ Input validation (required fields, valid reminder type)
- ✅ SQLite database using SQLAlchemy
- ✅ RESTful endpoint
- ✅ JSON-based response
- ✅ Marshmallow-based serialization

---

## API Usage

POST /api/reminders

Request JSON Body:
{
"date": "2025-05-20",
"time": "14:30:00",
"message": "Doctor appointment",
"reminder_type": "Email"
}

Success Response:
201 Created
{
"id": 1,
"date": "2025-05-20",
"time": "14:30:00",
"message": "Doctor appointment",
"reminder_type": "Email"
}

    400 Bad Request
        {
        "error": "Missing required fields"
        }
