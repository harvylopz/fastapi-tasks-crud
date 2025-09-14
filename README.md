# Tasks API

**Task management REST API** built with **FastAPI**, **SQLAlchemy (async)**, and **SQLite**.

🔗 **Base URL:** `http://38.54.57.138:8000`  
📄 **Swagger Documentation:** [http://38.54.57.138:8000/docs](http://38.54.57.138:8000/docs)  
📖 **ReDoc Documentation:** [http://38.54.57.138:8000/redoc](http://38.54.57.138:8000/redoc)

---

## 📋 Table of Contents
- [Tasks API](#tasks-api)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [📦 Requirements](#-requirements)
  - [🛠 Installation](#-installation)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Install dependencies](#2-install-dependencies)
    - [3. Run the API locally](#3-run-the-api-locally)
  - [📂 Project Structure](#-project-structure)
  - [🚀 Endpoints](#-endpoints)
  - [📌 Usage Examples](#-usage-examples)
    - [List all tasks](#list-all-tasks)
    - [Create a task](#create-a-task)
    - [Get a task by ID](#get-a-task-by-id)
    - [Update a task (partial)](#update-a-task-partial)
    - [Delete a task](#delete-a-task)
  - [📜 API Responses](#-api-responses)
  - [🤝 Contribution](#-contribution)
  - [📄 License](#-license)

---

## ✨ Features
- Full CRUD operations for tasks.
- Integrated **SQLite** database.
- Data validation with **Pydantic**.
- Support for **pagination** (`skip` and `limit`).
- Automatic documentation with **Swagger UI** and **ReDoc**.

---

## 📦 Requirements
- Python **3.9+**
- FastAPI **0.95+**
- SQLAlchemy **2.0+**
- Uvicorn (for local execution)

---

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/tasks-api.git
cd tasks-api
```

### 2. Install dependencies
```bash
pip install "fastapi[standard]"
pip install "sqlalchemy[aiosqlite]"

```

### 3. Run the API locally
```bash
uvicorn src.main:app --reload
```
- The API will be available at: [http://localhost:8000](http://localhost:8000)  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure
```
tasks-api/
├── src/
│   ├── main.py          # FastAPI configuration and routes
│   ├── crud.py          # Database CRUD operations
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic validation schemas
│   ├── database.py      # Database configuration
│   └── tasks.db         # SQLite database (auto-generated)
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

---

## 🚀 Endpoints

| Method | Path           | Description                    | Parameters                   |
|--------|----------------|--------------------------------|------------------------------|
| GET    | `/tasks/`      | List all tasks                 | `skip` (int), `limit` (int) |
| POST   | `/tasks/`      | Create a new task              | JSON Body (see [example](#-usage-examples)) |
| GET    | `/tasks/{id}`  | Get a task by ID               | `id` (int)                   |
| PUT    | `/tasks/{id}`  | Update a task                  | `id` (int), JSON Body        |
| DELETE | `/tasks/{id}`  | Delete a task                  | `id` (int)                   |

---

## 📌 Usage Examples

### List all tasks
```bash
curl http://38.54.57.138:8000/tasks
```

### Create a task
```bash
curl -X POST http://38.54.57.138:8000/tasks   -H "Content-Type: application/json"   -d '{"title": "Buy bread", "description": "Go to the bakery", "done": false}'
```

### Get a task by ID
```bash
curl http://38.54.57.138:8000/tasks/1
```

### Update a task (partial)
```bash
curl -X PUT http://38.54.57.138:8000/tasks/1   -H "Content-Type: application/json"   -d '{"done": true}'
```

### Delete a task
```bash
curl -X DELETE http://38.54.57.138:8000/tasks/1
```

---

## 📜 API Responses

| Code | Description                   |
|------|-------------------------------|
| 200  | Successful operation          |
| 201  | Resource successfully created |
| 404  | Resource not found            |
| 422  | Validation error              |

---
Successful response example (GET `/tasks/1`):
```json
{
  "id": 1,
  "title": "Buy bread",
  "description": "Go to the bakery",
  "done": false
}
```

Error example (404):
```json
{
  "detail": "Task not found"
}
```

---

## 🤝 Contribution
1. Fork the project.  
2. Create a feature branch (`git checkout -b feature/new-feature`).  
3. Commit your changes (`git commit -m "Add new feature"`).  
4. Push your branch (`git push origin feature/new-feature`).  
5. Open a Pull Request.  

---

## 📄 License
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.
See the `LICENSE` file for more details.
