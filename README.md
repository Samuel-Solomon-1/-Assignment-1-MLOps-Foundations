# Flask Machine Learning App — MLOps Deployment (Azure + GitHub Actions)

This repository contains a fully deployable Flask-based machine learning application, prepared for MLOps workflows using:

- **Azure App Services** (Deployment / Hosting)
- **GitHub Actions** (Continuous Integration)
- **Azure Pipelines** (Continuous Delivery)
- **Python virtual environments** for environment isolation
- **Unit testing**, **linting**, and **automated builds**

This project is part of **Assignment 1: MLOps Foundations**.

---

## Project Overview

This project demonstrates a complete MLOps pipeline using a minimal Flask machine learning API.

The application:

- Loads a trained Logistic Regression model (`model.pkl`)
- Provides a `/predict` POST endpoint
- Accepts JSON input and returns a prediction
- Is deployable to Azure App Services
- Is automatically tested through GitHub Actions CI

---

## Flask Application

### Endpoint Summary

| Method | Endpoint     | Description                      |
|--------|---------------|----------------------------------|
| GET    | `/`           | Health check / welcome message   |
| POST   | `/predict`    | Returns model prediction         |

### Example Prediction Request

```json
{
  "inputs": [0.5, -1.2, 3.1, 0.7]
}
````

---

## Machine Learning Model

A simple **Logistic Regression** classifier is trained on a synthetic dataset generated with `scikit-learn`.
The model is saved as:

```
model.pkl
```

This keeps the project lightweight and deployment-ready.

---

## Repository Structure

```
.
├── app.py
├── model.pkl
├── requirements.txt
├── make_predict_azure_app.sh
├── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── .flake8
```

---

## Setup Instructions (Local)

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

The API will run at:

```
http://localhost:8000
```

---

## Continuous Integration (GitHub Actions)

This repository includes a full CI pipeline defined in:

```
.github/workflows/ci.yml
```

The pipeline performs:

* Python setup (3.10)
* Virtual environment creation
* Dependency installation
* Linting with `flake8`
* Unit tests with `pytest`

Runs automatically on **every push**.

---

## Continuous Delivery (Azure Pipelines)

Azure Pipelines YAML (added in Task 3) performs:

* Python environment setup
* Install requirements
* Linting
* Unit testing
* Deployment to **Azure App Services**

This enables true CI/CD automation.

---

## Azure Deployment

The app can be deployed using Azure App Services.
After deployment, your live API will be accessible at:

```
https://<your-app-name>.azurewebsites.net/
```

Use the provided script to test deployed predictions:

```bash
./make_predict_azure_app.sh
```

---

## Testing

A simple unit test (`test_app.py`) is included:

```bash
pytest
```

## Assignment Requirements Covered

This repo includes:

* Part 1: Conceptual Write-ups
* Part 2:

  * Flask ML App
  * Azure Deployment
  * GitHub Actions CI
  * Azure Pipelines CD
  * Updated prediction script
  * Validation screenshots (to be added)

---

## Author

**Samuel Solomon**

Flask ML | Azure | GitHub Actions | MLOps Foundations
Assignment for: **MLOps Foundations – Part 2**

---

## How to Use This Repository

You may clone, deploy, extend, or use it for academic purposes.
For deployment, simply fork and configure Azure App Service + Azure Pipelines.
