Expense Tracker — Django

A production-oriented, multi-user expense tracking system built with Django and PostgreSQL, demonstrating secure data ownership, analytics, and clean backend architecture.

Why this project exists

This project was built to practice real-world Django backend patterns, not just CRUD:

Secure multi-user data isolation

Aggregated analytics at scale

Business logic separation

API + Template hybrid architecture

Production-ready database setup

Core Features
Authentication & Security

Login-required access (no public data)

Every record tied to an authenticated user

Owner-only access enforced at query & object level

Expense Management

Full Expense CRUD

User-specific Categories (CRUD)

PostgreSQL-backed relational models

Django Forms with validation

Analytics & Insights

Time-based summaries:

Last 7 days

Last 30 days

Last 365 days

Category-wise aggregations

Daily spending trends

Interactive charts (Chart.js)

Backend → frontend data flow using structured JSON (no DOM scraping)

Budget Tracking

Monthly budget limits per category

Real-time progress calculation

Over-budget detection with visual indicators

Business logic isolated in a service layer

Architecture Highlights

Django ORM for all aggregations (annotate, aggregate)

Service layer (services.py) for budget calculations

Django REST Framework

Expense API

Analytics API

Pagination & filtering

PostgreSQL for production readiness

Environment-based configuration using .env

Clean separation between:

Views

Business logic

Templates

APIs

Tech Stack

Backend: Django 6.x

Database: PostgreSQL

API: Django REST Framework

Auth: Django Auth

Styling: Tailwind CSS

Charts: Chart.js

Config: django-environ

Language: Python 3

📁 Project Structure (Key Parts)
mysite/
├── myapp/
│   ├── models.py        # Expense, Category, Budget
│   ├── services.py      # Budget business logic
│   ├── views.py         # Template views
│   ├── api/             # DRF APIs
│   ├── forms.py         # Styled Django forms
│   └── templates/       # Dark-mode UI

🌐 API Endpoints (Authenticated)
Endpoint	Description
/api/expenses/	Expense CRUD
/api/categories/	Category CRUD
/api/analytics/	Aggregated insights

Local Setup (Quick)
git clone https://github.com/insomniac1712/Expense-Tracker.git
cd Expense-Tracker

python -m venv env
env\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Status

Actively maintained.
Built as part of a backend-focused portfolio.