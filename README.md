# Flask DevOps App with Jenkins CI/CD Pipeline

This repository contains a Python Flask web application integrated with a full DevOps CI/CD pipeline using **Jenkins**, **Docker**, and **GitHub**, deployed on an **AWS EC2 instance**.

---

## Project Overview

The goal of this project is to demonstrate a complete DevOps workflow from source code to production using:

- Flask for a lightweight Python web app
- Pytest for unit testing
- Docker for containerization
- Jenkins for CI/CD automation
- GitHub for version control
- AWS EC2 as the cloud host

---

## Project Structure

flask-devops-app/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker instructions
├── Jenkinsfile # Jenkins Pipeline as Code
└── tests/
└── test_app.py # Unit test for Flask app

---

##  Prerequisites

- GitHub account
- Jenkins installed (running on AWS EC2 or local)
- Docker installed on Jenkins host
- Python 3.8+ installed
- Git installed
- Internet access to install packages

---

##  Local Development

###  Run the Flask App Locally

git clone https://github.com/yatindrap6/flask-devops-app.git
cd flask-devops-app
pip install -r requirements.txt
python app.py

Run Unit Tests
pytest

Docker Usage
Build Docker Image
docker build -t flask-devops-app .

Run Docker Container
docker run -d -p 5000:5000 flask-devops-app

Output Example
When the app is running:
Hello, DevOps World! CI/CD Pipeline is Working 🚀

Author
Yatindra Panchal
