# Blog API (FastAPI Backend)

A RESTful Blog API built with **FastAPI**, **SQLAlchemy**, and **Pydantic**.  
This project demonstrates backend development using CRUD operations, routing, database integration, and API design principles.

---

## Features

- Create, read, update, and delete users
- Create, read, update, and delete blog posts
- User–post relationship handling
- Input validation using Pydantic schemas
- Proper error handling with HTTP responses
- Modular router-based architecture
- SQLAlchemy ORM database integration

---

## Tech Stack

- **Python**
- **FastAPI** — High-performance Python web framework
- **SQLAlchemy** — ORM for database design and queries
- **Pydantic** — Request validation and serialization
- **SQLite** — Lightweight relational database
- **Uvicorn** — ASGI server

---

## Project Structure

```
fastapi_blog/
├── routers/
│   ├── users.py
│   └── posts.py
├── models.py
├── schemas.py
├── database.py
├── main.py
└── requirements.txt
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/OgbeweOsawaru/blog-api.git
cd blog-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

> Interactive docs available at `http://127.0.0.1:8000/docs`

---

## API Endpoints

### Users

| Method   | Endpoint                | Description             |
| -------- | ----------------------- | ----------------------- |
| `POST`   | `/api/users`            | Create a new user       |
| `GET`    | `/api/users/{id}`       | Get a user by ID        |
| `PATCH`  | `/api/users/{id}`       | Partially update a user |
| `DELETE` | `/api/users/{id}`       | Delete a user           |
| `GET`    | `/api/users/{id}/posts` | Get all posts by a user |

### Posts

| Method   | Endpoint          | Description             |
| -------- | ----------------- | ----------------------- |
| `POST`   | `/api/posts`      | Create a new post       |
| `GET`    | `/api/posts`      | Get all posts           |
| `GET`    | `/api/posts/{id}` | Get a post by ID        |
| `PUT`    | `/api/posts/{id}` | Fully update a post     |
| `PATCH`  | `/api/posts/{id}` | Partially update a post |
| `DELETE` | `/api/posts/{id}` | Delete a post           |

---

## What I Learned

- Building REST APIs with **FastAPI**
- Database design using **SQLAlchemy ORM**
- Request validation using **Pydantic**
- Modular router-based architecture
- Error handling in production APIs

---

## Future Improvements

- [ ] Add JWT authentication
- [ ] Add pagination & filtering
- [ ] Deploy to cloud (Render / Railway)
- [ ] Add automated tests

---

## Author

**Ogbewe Osawaru Favour**

- GitHub: [github.com/OgbeweOsawaru](https://github.com/OgbeweOsawaru)
- LinkedIn: [linkedin.com/in/osawaru-ogbewe](https://www.linkedin.com/in/osawaru-ogbewe)

---

## License

This project is for educational purposes.
