# Journal API

## Description

Journal API is a secure RESTful backend built with Flask that allows users to register, authenticate using JSON Web Tokens (JWT), and manage their personal journal entries. Each journal entry belongs to a specific user, ensuring that authenticated users can only access, update, or delete their own records.

The API follows RESTful principles and demonstrates secure authentication, authorization, CRUD operations, pagination, and database migrations.

---

## Features

* User registration
* User login using JWT authentication
* Secure password hashing with Flask-Bcrypt
* Protected routes using JWT
* Create journal entries
* View journal entries with pagination
* Update journal entries
* Delete journal entries
* Users can only access their own journal entries
* Database migrations using Flask-Migrate
* Database seeding with Faker

---

## Technologies Used

* Python
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* Flask-Bcrypt
* Marshmallow
* Faker
* SQLite

---

## Project Structure

```
journal-api/
│
├── app.py
├── config.py
├── extensions.py
├── seed.py
├── Pipfile
├── README.md
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── journal_entry.py
│
├── resources/
│   ├── auth.py
│   └── journal.py
│
├── schemas/
│   ├── __init__.py
│   ├── user_schema.py
│   └── journal_schema.py
│
└── migrations/
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate into the project directory.

```bash
cd <repository-name>
```

Install the project dependencies.

```bash
pipenv install
```

Activate the virtual environment.

```bash
pipenv shell
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DATABASE_URI=sqlite:///instance/app.db

FLASK_APP=app.py
FLASK_ENV=development
```

---

## Database Setup

Initialize the migrations (only once).

```bash
flask db init
```

Create a migration.

```bash
flask db migrate -m "Initial migration"
```

Apply the migration.

```bash
flask db upgrade
```

Seed the database.

```bash
python seed.py
```

---

## Running the Application

Start the Flask development server.

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## Authentication

The API uses JSON Web Tokens (JWT).

After logging in, copy the returned access token and include it in the Authorization header of protected requests.

```
Authorization: Bearer <your_access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint    | Description                               |
| ------ | ----------- | ----------------------------------------- |
| POST   | `/register` | Register a new user                       |
| POST   | `/login`    | Authenticate a user and return a JWT      |
| GET    | `/loggedin` | Return the currently authenticated user   |
| DELETE | `/logout`   | Log out the current user (if implemented) |

### Journal Entries

| Method | Endpoint        | Description                                                                            |
| ------ | --------------- | -------------------------------------------------------------------------------------- |
| GET    | `/journal`      | Retrieve all journal entries belonging to the authenticated user (supports pagination) |
| POST   | `/journal`      | Create a new journal entry                                                             |
| GET    | `/journal/<id>` | Retrieve a specific journal entry *(if implemented)*                                   |
| PATCH  | `/journal/<id>` | Update a journal entry                                                                 |
| DELETE | `/journal/<id>` | Delete a journal entry                                                                 |

---

## Sample Register Request

```json
{
    "username": "iann",
    "email": "iann@example.com",
    "password": "Password123!"
}
```

---

## Sample Login Response

```json
{
    "access_token": "your_jwt_token",
    "user": {
        "id": 1,
        "username": "iann",
        "email": "iann@example.com"
    }
}
```

---

## Pagination

The journal endpoint supports pagination using query parameters.

Example:

```
GET /journal?page=1&per_page=5
```

---

## Future Improvements

* Search journal entries by title
* Filter entries by creation date
* Upload images or attachments
* Soft delete and restore journal entries
* Refresh token authentication
* API documentation with Swagger/OpenAPI

---

## Author

Developed as part of a Flask Authentication and Authorization lab assignment.
