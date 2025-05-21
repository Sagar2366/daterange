# Date Range Overlap Service

A simple FastAPI-based service to determine if two date ranges overlap.  
Includes REST API, Pydantic models, programmatic logic, and CI for linting and testing.

---

## Features

- REST API to check for overlap between two date ranges
- Pydantic-based models for request/response
- Well-tested logic and API
- CI with linting and tests (flake8, pylint, pytest)

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/Sagar2366/daterange.git
cd daterange
```

### 2. Set up a Python Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```
Or with the provided Makefile:
```sh
make build
```
---

## Running the Application

```sh
uvicorn daterange_service.fastapi:app --reload
```
Or with the provided Makefile:
```sh
make run
```

## Run test cases

```sh
PYTHONPATH=. pytest
```
Or with the provided Makefile:
```sh
make test
```

Access the interactive API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Usage

### API Endpoint

- **POST** `/overlap`
- **Content-Type:** `application/json`
- **Request Body Example:**  
  ```json
  {
    "range1": {"start": "2025-05-20T12:00:00", "end": "2025-05-20T14:00:00"},
    "range2": {"start": "2025-05-20T13:00:00", "end": "2025-05-20T15:00:00"}
  }
  ```

---

## Example curl Commands

### Check for Overlap (returns true)

```sh
curl -X POST "http://127.0.0.1:8000/overlap" \
  -H "Content-Type: application/json" \
  -d '{
    "range1": {"start": "2025-05-20T12:00:00", "end": "2025-05-20T14:00:00"},
    "range2": {"start": "2025-05-20T13:00:00", "end": "2025-05-20T15:00:00"}
  }'
```

**Expected Response:**
```json
{
  "overlap": true,
  "details": "Ranges overlap between 2025-05-20T13:00:00 and 2025-05-20T14:00:00"
}
```

---

### Check for No Overlap (returns false)

```sh
curl -X POST "http://127.0.0.1:8000/overlap" \
  -H "Content-Type: application/json" \
  -d '{
    "range1": {"start": "2025-05-20T12:00:00", "end": "2025-05-20T13:00:00"},
    "range2": {"start": "2025-05-20T13:00:00", "end": "2025-05-20T14:00:00"}
  }'
```

**Expected Response:**
```json
{
  "overlap": false,
  "details": "No overlap"
}
```

---

## Continuous Integration

- On every push and pull request to `main`, CI runs linting, testing, and builds an artifact.

---

## Project Structure

```plaintext
daterange_service/
├── __init__.py
├── fastapi.py         # FastAPI app and endpoint
├── models.py          # Pydantic models
├── overlap.py         # Overlap logic

tests/
├── test_app.py        # API endpoint tests
├── test_overlap.py    # Logic tests

.github/
└── workflows/
    └── ci.yaml        # GitHub Actions workflow

requirements.txt
Makefile
README.md
```

---
