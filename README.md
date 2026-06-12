# Flask Application with Docker and GitHub Actions CI/CD

## Project Overview

This project demonstrates a complete DevOps workflow using:

* Python Flask Application
* Docker Containerization
* Git Version Control
* GitHub Repository Hosting
* GitHub Actions CI/CD Pipeline
* Ubuntu (WSL2) Development Environment

The application is containerized using Docker and automatically built and tested through GitHub Actions whenever code is pushed to the repository.

---

# Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    | Push Event
    v
GitHub Actions Workflow
    |
    +--> Checkout Source Code
    |
    +--> Setup Python Environment
    |
    +--> Install Dependencies
    |
    +--> Build Docker Image
    |
    +--> Run Docker Container
    |
    +--> Execute Validation Script
    |
    +--> Cleanup
    |
    v
Workflow Success
```

---

# Technologies Used

| Scope                | Tool           |
| -------------------- | -------------- |
| Source Control       | Git            |
| Repository Hosting   | GitHub         |
| Programming Language | Python 3.11    |
| Web Framework        | Flask          |
| Containerization     | Docker         |
| CI/CD                | GitHub Actions |
| Operating System     | Ubuntu (WSL2)  |
| IDE                  | VS Code        |

---

# Project Structure

```text
FlaskApp/
│
├── app.py
├── check_docker.py
├── requirements.txt
├── Dockerfile
│
└── .github
    └── workflows
        └── ci.yml
```

---

# File Description

## app.py

Main Flask application.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "GitHub Actions CI/CD with Docker is Working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## requirements.txt

Contains Python dependencies.

```text
flask==3.0.3
```

---

## Dockerfile

Creates Docker image for the Flask application.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
```

---

## check_docker.py

Validates Docker installation.

```python
import subprocess

result = subprocess.run(
    ["docker","--version"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

---

## ci.yml

GitHub Actions workflow.

Location:

```text
.github/workflows/ci.yml
```

Workflow Tasks:

1. Checkout code
2. Setup Python
3. Install dependencies
4. Build Docker image
5. Run Docker container
6. Validate Docker
7. Cleanup resources

---

# Prerequisites

Before running this project locally, install:

* Windows 10/11
* WSL2
* Ubuntu
* Git
* Docker Desktop
* VS Code

---

# WSL Installation

Check WSL status:

```bash
wsl --status
```

List installed distributions:

```bash
wsl -l -v
```

Expected output:

```text
Ubuntu Running Version 2
```

---

# Ubuntu Package Update

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Git Installation

Install Git:

```bash
sudo apt install git -y
```

Verify:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

---

# Docker Installation

Install Docker Desktop on Windows.

Enable WSL Integration:

Docker Desktop

Settings

→ Resources

→ WSL Integration

Enable:

```text
Ubuntu
```

Verify Docker:

```bash
docker --version
```

Check Docker daemon:

```bash
docker ps
```

Expected output:

```text
CONTAINER ID
IMAGE
COMMAND
STATUS
PORTS
NAMES
```

---

# Clone Repository

Clone the project:

```bash
git clone https://github.com/<username>/<repository>.git
```

Navigate into project:

```bash
cd FlaskApp
```

---

# Running Application Without Docker

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```text
http://localhost:5000
```

---

# Docker Commands

## Build Docker Image

```bash
docker build -t flask-app .
```

Verify:

```bash
docker images
```

Example:

```text
REPOSITORY            TAG
github-actions-demo   latest
```

---

## Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-demo flask-app
```

Verify:

```bash
docker ps
```

---

## View Logs

```bash
docker logs flask-demo
```

---

## Stop Container

```bash
docker stop flask-demo
```

---

## Remove Container

```bash
docker rm flask-demo
```

---

## Remove Image

```bash
docker rmi flask-app
```

---

# Git Commands Used

Initialize repository:

```bash
git init
```

Check status:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial Commit"
```

Create main branch:

```bash
git branch -M main
```

Add remote:

```bash
git remote add origin https://github.com/<username>/<repository>.git
```

Verify remote:

```bash
git remote -v
```

Push code:

```bash
git push -u origin main
```

---

# GitHub Actions Workflow Execution

Trigger:

```text
Push Event
```

When code is pushed:

```text
Developer Pushes Code
            |
            v
GitHub Repository
            |
            v
GitHub Actions
            |
            +--> Checkout
            +--> Python Setup
            +--> Install Dependencies
            +--> Docker Build
            +--> Docker Run
            +--> Validation
            +--> Cleanup
            |
            v
Success
```

---

# GitHub Actions Verification

Open:

GitHub Repository

→ Actions

Verify:

* Workflow Executed Successfully
* Docker Image Built Successfully
* Container Started Successfully
* Validation Script Executed Successfully

---

# Expected Output

Open:

```text
http://localhost:5000
```

Expected Response:

```text
GitHub Actions CI/CD with Docker is Working!
```

---

# Learning Outcomes

Through this project the following concepts are demonstrated:

* Git Fundamentals
* GitHub Repository Management
* Docker Containerization
* Python Flask Development
* CI/CD Pipeline Creation
* GitHub Actions Workflow Automation
* WSL2 Linux Environment
* Container Lifecycle Management
* DevOps Best Practices

---

# Author
Pavankalyan Thotakura
DevOps | Embedded Systems | CI/CD | Docker | GitHub Actions

