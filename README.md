📌 Blog API (FastAPI Backend)

A simple RESTful Blog API built with FastAPI, SQLAlchemy, and Pydantic, supporting full CRUD operations for users and blog posts.
This project demonstrates backend development concepts including routing, database integration, validation, and structured API design.

🚀 Features
Create, read, update, and delete users
Create, read, update, and delete blog posts
Relationship between users and posts
Input validation using Pydantic schemas
Error handling with proper HTTP responses
Modular project structure using routers
SQLAlchemy ORM integration

🛠️ Tech Stack
Python
FastAPI
SQLAlchemy
Pydantic
SQLite (or configured database)
Uvicorn

📁 Project Structure
fastapi_blog/
│
├── routers/
│ ├── users.py
│ ├── posts.py
│
├── models.py
├── schemas.py
├── database.py
├── main.py
└── requirements.txt
⚙️ Installation & Setup

1. Clone the repository
   git clone https://github.com/OgbeweOsawaru/blog-api.git
   cd blog-api
2. Create virtual environment
   python -m venv venv

Activate:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate 3. Install dependencies
pip install -r requirements.txt 4. Run the server
uvicorn main:app --reload 5. Open API docs
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
📌 API Endpoints
Users
POST /api/users → Create user
GET /api/users/{id} → Get user
PATCH /api/users/{id} → Update user
DELETE /api/users/{id} → Delete user
GET /api/users/{id}/posts → Get user posts
Posts
POST /api/posts → Create post
GET /api/posts → Get all posts
GET /api/posts/{id} → Get post
PUT /api/posts/{id} → Update post
PATCH /api/posts/{id} → Partial update
DELETE /api/posts/{id} → Delete post
📚 What I Learned
Building RESTful APIs with FastAPI
Working with SQLAlchemy ORM
Structuring backend applications
Handling request validation and errors
Designing scalable API architecture
📌 Future Improvements
Add authentication (JWT)
Add pagination and filtering
Deploy API to cloud (Render / Railway)
Add unit tests

👨‍💻 Author
Ogbewe Osawaru Favour

GitHub: github.com/OgbeweOsawaru
LinkedIn: www.linkedin.com/in/osawaru-ogbewe

📄 License
This project is for educational purposes.
