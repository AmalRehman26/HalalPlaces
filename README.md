# Halal Restaurant Review Application

A full‑stack web application for discovering and reviewing halal restaurants. The project is built with FastAPI on the backend, SQLModel for database access, and HTMX for dynamic frontend interactions.

---

## Overview

This application allows users to search for halal restaurants, view details and reviews, and submit their own reviews. It also exposes a RESTful JSON API so the same data can be accessed programmatically. Data is stored in a SQLite database and persists across server restarts.

---

## Features

- Search restaurants by city and cuisine, with results updating dynamically
- Submit reviews with a 1–5 star rating and written feedback
- Responsive, mobile‑friendly UI
- RESTful API for external or programmatic use
- Persistent storage using SQLite
- HTMX‑based UI updates without full page reloads
- Input validation using Pydantic schemas

---

## Project Structure

```
HalalPlaces/
├── main.py
├── requirements.txt
├── restaurants.db
├── README.md
├── KGD.pdf
├── src/
│   ├── database.py
│   ├── models/
│   │   ├── restaurant.py
│   │   └── review.py
│   ├── schemas/
│   │   ├── restaurant.py
│   │   └── review.py
│   └── routers/
│       ├── restaurants.py
│       ├── reviews.py
│       ├── fragments.py
│       └── pages.py
└── templates/
    ├── base.html
    ├── index.html
    ├── restaurant_detail.html
    ├── error.html
    └── fragments/
        ├── restaurant_list.html
        ├── review_item.html
        └── error.html
```

The structure separates concerns clearly: models define database tables, schemas handle validation, routers contain application logic, and templates manage presentation.

---

## Setup Instructions

### 1. Extract and Navigate to the Project

Extract the project archive and navigate to the root directory (the folder containing `main.py`).

```bash
cd path/to/HalalPlaces
```

---

### 2. Create a Virtual Environment

```bash
# In macOS / Linux
python3 -m venv venv
# In Windows
python -m venv venv
```

---

### 3. Activate the Virtual Environment

```bash
# In macOS / Linux
source venv/bin/activate
# In Windows
venv\Scripts\activate
```

Once activated, `(venv)` should appear in your terminal prompt.

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

```bash
#In macOS / Linux
python3 main.py
# In Windows
python main.py
```

Alternatively:

```bash
uvicorn main:app --reload
```

The server will start on port 8000 and create the SQLite database automatically if it does not already exist.

---

## Using the Application

### Web Interface

Open a browser and go to:

```
http://localhost:8000
```

From the home page, you can:

- View all restaurants
- Filter results by city or cuisine
- Click a restaurant to see details and reviews
- Submit a new review directly from the UI

HTMX is used so searches and review submissions update the page without full reloads.

---

### API Documentation

Interactive API documentation is available at:

```
http://localhost:8000/docs
```

This interface can be used to test all endpoints, including creating restaurants and reviews.

---

## CRUD Operations

The application supports full CRUD functionality:

- Create restaurants and reviews using POST requests
- Read all restaurants or a single restaurant using GET requests
- Update restaurant information using PUT requests
- Delete restaurants using DELETE requests

All changes are persisted to the SQLite database.

---

## Data Persistence

The database file (`restaurants.db`) is stored locally. Stopping and restarting the server does not remove existing data, confirming that the application uses persistent storage rather than in‑memory data.

---

## Error Handling and Validation

- Invalid input data is rejected automatically using Pydantic validation (HTTP 422)
- Requests for non‑existent resources return HTTP 404 errors
- User‑friendly error pages are shown in the browser

---

## Knowledge Goals Demonstrated

This project demonstrates the following concepts:

- Defining API endpoints with clear URL paths
- Proper use of HTTP methods and status codes
- Input validation with schemas
- Dependency injection for database sessions
- Data modeling with ORM classes
- Full CRUD functionality with persistent storage
- JSON‑based API responses
- HTML UI endpoints powered by HTMX
- User actions mapped directly to database operations
- Separation of concerns across application layers

Detailed examples and justifications are provided in `KGD.pdf`.

---

## I have used AI to help formart my README file
