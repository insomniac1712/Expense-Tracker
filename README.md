# 💰 Expense Tracker

> A lightweight Django web application for managing personal finances with real-time analytics, category tracking, and a modern responsive UI.

Track your spending habits, visualize expense patterns, and stay on top of your finances with an intuitive expense management dashboard.

---

## ✨ Features

- ✅ **Full Expense CRUD** — Create, read, update, and delete expenses in seconds
- 📊 **Smart Analytics Dashboard** — View spending trends across daily, weekly, monthly, and yearly timeframes
- 🏷️ **Category Organization** — Group expenses by custom categories for better insights
- 📈 **Automatic Aggregations** — Real-time calculations of total expenses and category breakdowns
- 🎨 **Modern Responsive UI** — Built with Tailwind CSS for a sleek, mobile-friendly interface
- ⚡ **Lightning Fast** — Optimized Django ORM queries with aggregation

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 4.x (Python) |
| **Database** | SQLite (development) / PostgreSQL (production-ready) |
| **Frontend** | Django Templates |
| **Styling** | Tailwind CSS v2.2.16 |
| **Package Manager** | npm (for Tailwind) |
| **Server** | Django Development Server |

## Project Structure

```
Expense tracker/
├── mysite/                  # Django project root
│   ├── myapp/              # Main expense tracking app
│   │   ├── models.py       # Expense model
│   │   ├── views.py        # View logic (index, edit, delete)
│   │   ├── forms.py        # ExpenseForm
│   │   ├── urls.py         # URL routing
│   │   ├── templates/      # HTML templates
│   │   └── static/         # CSS (Tailwind source + output)
│   ├── mysite/             # Project settings
│   ├── manage.py           # Django management script
│   ├── package.json        # Node.js dependencies
│   └── tailwind.config.js  # Tailwind configuration
├── env/                    # Python virtual environment
└── .gitignore
```

## Setup Instructions

### 1. Clone the repository
```powershell
git clone <repository-url>
cd "Expense tracker"
```

### 2. Set up Python virtual environment
```powershell
# Activate the virtual environment
.\env\Scripts\Activate.ps1

# Install Python dependencies (if requirements.txt exists)
pip install django
```

### 3. Set up Tailwind CSS
```powershell
cd mysite

# Install Node dependencies
npm install

# Compile Tailwind CSS (one-time)
npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css

# OR watch for changes during development
npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css --watch
```

### 4. Run Django migrations
```powershell
cd mysite
python manage.py migrate
```

### 5. Create a superuser (optional)
```powershell
python manage.py createsuperuser
```

### 6. Run the development server
```powershell
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Database Schema

## 📸 Screenshots

### Dashboard View
```
[Your expense list with total, weekly, monthly, yearly summaries]
[Category breakdown with visual charts]
[Quick-add expense form]
```

**Coming soon:** Add actual screenshots after first deployment

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+ (for Tailwind CSS)
- Git

### 1️⃣ Clone & Navigate
```powershell
git clone <repository-url>
cd "Expense tracker"
```

### 2️⃣ Set up Python Virtual Environment
```powershell
# Create and activate virtual environment
python -m venv env
.\env\Scripts\Activate.ps1

# Verify activation
python --version
```

### 3️⃣ Install Django
```powershell
pip install django pillow
```

### 4️⃣ Configure Tailwind CSS
```powershell
cd mysite

# Install Node dependencies
npm install

# Compile Tailwind (development - one time)
npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css

# OR watch mode (auto-recompile on changes)
npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css --watch
```

### 5️⃣ Run Migrations
```powershell
python manage.py migrate
```

### 6️⃣ Start Development Server
```powershell
python manage.py runserver
```

**Open browser:** http://127.0.0.1:8000/ 🎉

---

## 📋 Project Structure

```
Expense tracker/
├── .github/
│   └── copilot-instructions.md  # AI agent guidelines
├── mysite/                       # Django project root
│   ├── myapp/                   # Main app (expenses)
│   │   ├── migrations/          # Database migrations
│   │   ├── static/myapp/
│   │   │   └── src.css          # Tailwind source
│   │   │   └── output.css       # Compiled Tailwind
│   │   ├── templates/myapp/
│   │   │   ├── base.html        # Base template
│   │   │   ├── index.html       # Dashboard
│   │   │   └── edit.html        # Edit form
│   │   ├── models.py            # Expense model
│   │   ├── views.py             # View logic
│   │   ├── forms.py             # Django forms
│   │   └── urls.py              # URL routing
│   ├── mysite/                  # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── package.json             # Node.js deps
│   ├── tailwind.config.js       # Tailwind config
│   └── db.sqlite3               # Database
├── env/                         # Virtual environment
├── .gitignore
├── README.md                    # This file
└── LICENSE
```

---

## 💾 Database Schema

### Expense Model
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `name` | CharField(100) | Expense description |
| `amount` | IntegerField | Amount spent |
| `category` | CharField(50) | Category (Food, Transport, etc.) |
| `date` | DateField | Auto-set to current date |

---

## 🎯 API Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET, POST | View all expenses + add new |
| `/edit/<id>/` | GET, POST | Edit existing expense |
| `/delete/<id>/` | POST | Delete expense |

---

## 📊 Analytics Features

The dashboard auto-calculates:

- **Daily Breakdown** — Expenses aggregated by date
- **Weekly Total** — Last 7 days of spending
- **Monthly Total** — Last 30 days of spending
- **Yearly Total** — Last 365 days of spending
- **Category Breakdown** — Total per category for insights

---

## 🔧 Development Guide

### Add a New Feature

1. **Update Models** (if needed)
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Edit Views** in `myapp/views.py`

3. **Update Templates** in `myapp/templates/myapp/`

4. **Add Tailwind Classes** and recompile:
   ```powershell
   npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css
   ```

5. **Test locally** at http://127.0.0.1:8000/

### Common Commands

```powershell
# Create admin superuser
python manage.py createsuperuser

# Access Django admin
# Visit: http://127.0.0.1:8000/admin

# Run tests
python manage.py test

# Freeze dependencies
pip freeze > requirements.txt
```

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **Tailwind styles not applied?** | Run: `npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css` |
| **`ModuleNotFoundError`?** | Activate venv: `.\env\Scripts\Activate.ps1` |
| **CSS file not found?** | Check `base.html` links to `output.css`, not `styles.css` |
| **Database locked?** | Delete `db.sqlite3` and run migrations again |

---

## 🎉 Future Roadmap

### Phase 1 (Current)
- ✅ Basic CRUD operations
- ✅ Time-based analytics
- ✅ Category tracking
- ✅ Responsive UI with Tailwind

### Phase 2 (Planned)
- [ ] User authentication & registration
- [ ] Multi-user support with data isolation
- [ ] Budget limits per category
- [ ] Recurring expense templates

### Phase 3 (Advanced)
- [ ] Data visualization (Chart.js / Plotly)
- [ ] CSV/PDF export functionality
- [ ] Advanced filtering & search
- [ ] API (Django REST Framework)

### Phase 4 (Polish)
- [ ] Dark mode toggle
- [ ] Multi-currency support
- [ ] Data import/export
- [ ] Analytics reports

---

---

## 📧 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open source and available under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📬 Support & Questions

- **Found a bug?** Open an [Issue](https://github.com/your-repo/issues)
- **Have suggestions?** Start a [Discussion](https://github.com/your-repo/discussions)
- **Need help?** Check the [Troubleshooting](#️-troubleshooting) section above

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) — Web framework
- [Tailwind CSS](https://tailwindcss.com/) — Styling toolkit
- Community contributors and testers
