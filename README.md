# customic_task

This project provides an API for generating T-shirt mockups with user-customized text.
Each mockup is generated asynchronously via Celery + Redis, and users can view their mockup history with pagination and search support.

## Features

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
    👉 `/api/schema/swagger-ui/`

- **Dockerized Setup**
  - Includes Docker Compose for Django, Redis, and Celery worker

## 🧰 Tech Stack

- **Django 5 + Django REST Framework**
- **Celery** (task queue)
- **Redis** (message broker)
- **JWT Authentication**
- **DRF Spectacular** (Swagger documentation)
- **Docker + Docker Compose**

## Repository Structure

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

## Setup & Usage

### 1. Clone the repository

```sh
git clone https://github.com/PandAJ2021/customic_task.git
cd customic_task
```

### 2. Local Development Setup

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Start Redis & Celery manually (if not using Docker):

```sh
redis-server
celery -A core worker -l info
```
### 3. Run via Docker (Recommended)

```sh
docker-compose up --build
```

This command will:

- Build the **Django app** container  
- Start the **Redis** service  
- Run the **Celery worker** automatically  

Once everything is up and running, open the Swagger documentation in your browser:

👉 [http://127.0.0.1:8000/api/schema/swagger-ui/]


## Author

[**PandAJ2021**](https://github.com/PandAJ2021)
