# Student Survey FastAPI Application

A FastAPI-based web app to collect student survey responses, containerized with Docker and deployed via Jenkins CI/CD to a Kubernetes cluster with MySQL on AWS RDS.

## Features
- Frontend: HTML Form
- Backend: FastAPI + SQLAlchemy
- DB: AWS RDS (MySQL)
- Containerized: Docker
- Orchestrated: Kubernetes
- CI/CD: Jenkins pipeline

## Deployment
1. Jenkins builds and pushes Docker image
2. Kubernetes updates the deployment
3. Form data is submitted and stored in RDS

## Endpoint
- `/survey-form` – HTML form UI
- `/submit-survey` – Form handler

---

## Author
Sathvika Veluru
