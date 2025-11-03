# 🧵 Customic Task

This repository is the solution for the **Customic Mockup Task** challenge.

It provides an API for generating T-shirt mockups with user-customized text.
Each mockup is generated asynchronously via **Celery + Redis**, and users can view their mockup history with pagination and search support.

---

## ✨ Features

- **Dynamic Mockup Generation**
  - Choose **font**
  - Choose **text color**
  - Select **specific shirt color(s)**

- **Celery + Redis Integration**
  - Used for handling mockup generation in the background

- **Mockup History**
  - Paginated list of mockups per user
  - Includes **search** functionality

- **JWT Authentication**
  - Secure API access via `rest_framework_simplejwt`

- **Swagger UI (DRF Spectacular)**
  - Full interactive documentation at:  
    👉 [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

- **Dockerized Setup**
  - Includes Docker Compose for Django, Redis, and Celery worker

---

## 🧰 Tech Stack

- **Django 5 + Django REST Framework**
- **Celery** (task queue)
- **Redis** (message broker)
- **JWT Authentication**
- **DRF Spectacular** (Swagger documentation)
- **Docker + Docker Compose**

---

## 📂 Repository Structure

```
customic_task/
├── accounts/           # Contains JWT authentication logic
├── core/               # Project settings
├── mockups/            # Mockup generation logic
├── static/             # Fonts and shirt images
├── .dockerignore       # Docker build ignore rules
├── .gitignore          # Git ignore rules
├── docker-compose.yml  # Multi-container Docker application setup
├── dockerfile          # Docker image build instructions
├── manage.py           
├── requirements.txt    # Python package dependencies
├── schema.yml          # Swagger schema (generated)
```

---

## ⚙️ Setup & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PandAJ2021/customic_task.git
cd customic_task
```

### 2️⃣ Local Development Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Start Redis & Celery manually (if not using Docker):

```bash
redis-server
celery -A core worker -l info
```

### 3️⃣ Run via Docker (Recommended)

```bash
docker-compose up --build
```

This command will:

- 🏗️ Build the **Django app** container  
- 🔄 Start the **Redis** service  
- ⚙️ Run the **Celery worker** automatically  

Once everything is up and running, open the Swagger documentation in your browser:

👉 [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## 🔑 Authentication

This project uses **JWT (JSON Web Token)** for authentication.

### Obtain Token

```http
POST /api/token/
```

Example request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Use the returned access token in headers for authorized requests:

```
Authorization: Bearer <your_access_token>
```

---

## 🧵 Notes

- **Celery + Redis** handle asynchronous mockup generation.  
- Fonts and shirt base images are stored under `static/`.  
- Each user can view their **mockup history** with pagination and search.  
- Docker Compose automatically sets up Redis, Celery, and Django services.  

---

## 👤 Author

**Ali Jalili**  
GitHub: [PandAJ2021](https://github.com/PandAJ2021)
