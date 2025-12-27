
# 💰 Expense Tracker

### *Django • PostgreSQL • Analytics*

> A backend-focused expense tracking application built with Django, demonstrating secure multi-user data handling, ORM-based analytics, and production-ready architecture.

---

## 🧭 Overview

This project was built to practice **real-world Django backend patterns**, including:

* secure user-based data isolation
* database-level aggregations and analytics
* separation of business logic from views
* API + template hybrid architecture
* production-oriented configuration

The goal was **correctness, clarity, and maintainability**, not frontend complexity.

---

## ✨ Features

### 🔐 Authentication & Authorization

* Login-required access (no public data)
* Each record is associated with an authenticated user
* User-scoped querysets to prevent data leakage
* Object-level ownership enforcement

---

### 💸 Expense Management

* Full Expense CRUD (Create, Read, Update, Delete)
* User-specific Categories (CRUD)
* Relational models with foreign keys
* Django Forms with server-side validation

---

### 📊 Analytics & Aggregations

* Time-based expense summaries:

  * Last **7 days**
  * Last **30 days**
  * Last **365 days**
* Daily expense aggregation
* Category-wise totals
* Backend-calculated analytics using Django ORM
* Structured data exposed for frontend consumption (JSON)

---

### 📉 Budget Tracking

* Monthly budget limits per category
* Real-time calculation of spending vs budget
* Over-budget detection
* Business logic implemented in a dedicated service layer

---

## 🧱 Architecture & Design Decisions

| Concern        | Implementation                              |
| -------------- | ------------------------------------------- |
| ORM Usage      | `annotate`, `aggregate`, filtered querysets |
| Business Logic | Service layer (`services.py`)               |
| Data Isolation | User-scoped queries + object checks         |
| APIs           | Django REST Framework                       |
| Configuration  | Environment variables (`.env`)              |
| Database       | PostgreSQL (production-ready)               |

---

## 🛠️ Tech Stack

| Layer             | Technology            |
| ----------------- | --------------------- |
| Backend Framework | Django 6.x            |
| Language          | Python 3              |
| Database          | PostgreSQL            |
| API Layer         | Django REST Framework |
| Authentication    | Django Auth           |
| Configuration     | django-environ        |
| Charts            | Chart.js              |

---

## 📁 Project Structure (Key Parts)

```
mysite/
├── myapp/
│   ├── models.py        # Expense, Category, Budget models
│   ├── services.py      # Business logic (budget calculations)
│   ├── views.py         # Template-based views
│   ├── api/             # REST API endpoints
│   ├── forms.py         # Django forms
│   └── templates/       # Server-rendered templates

---

## 🌐 API Endpoints (Authenticated)

| Endpoint              | Method       | Description               |
| --------------------- | ------------ | ------------------------- |
| `/api/expenses/`      | GET / POST   | List & create expenses    |
| `/api/expenses/<id>/` | PUT / DELETE | Update / delete expense   |
| `/api/categories/`    | GET / POST   | Category management       |
| `/api/analytics/`     | GET          | Aggregated analytics data |

* All endpoints require authentication
* All queries are user-scoped
* Pagination and filtering enabled

---

## 🚀 Local Setup (Quick)

```bash
git clone https://github.com/insomniac1712/Expense-Tracker.git
cd Expense-Tracker

python -m venv env
env\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧠 What This Project Demonstrates (For Recruiters)

* Strong Django fundamentals
* Secure multi-user backend design
* Practical ORM aggregation usage
* Clean separation of concerns
* API development with DRF
* Production-aware configuration (PostgreSQL, env vars)

---

## 📌 Status

Actively maintained.
Built as part of a backend-focused portfolio.

---

## 📜 License

MIT License

---
