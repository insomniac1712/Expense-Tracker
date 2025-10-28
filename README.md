# Expense Tracker

A Django-based web application for tracking personal expenses with categorization, time-based analytics, and interactive dashboards built with Tailwind CSS.

## Features

- ✅ **Expense Management**: Add, edit, and delete expenses
- 📊 **Analytics Dashboard**: View expenses by day, week, month, and year
- 🏷️ **Category Tracking**: Organize expenses by categories
- 📅 **Date-based Filtering**: Automatic calculation of weekly, monthly, and yearly totals
- 🎨 **Modern UI**: Built with Tailwind CSS for a clean, responsive interface

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (development)
- **Frontend**: Django Templates + Tailwind CSS
- **Styling**: Tailwind CSS v2.2.16

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

### Expense Model
- `name` (CharField): Description of the expense
- `amount` (IntegerField): Amount in currency
- `category` (CharField): Expense category (e.g., Food, Transport, Bills)
- `date` (DateField): Auto-generated date of entry

## Key Features in Detail

### Analytics
- **Daily Sums**: Aggregated expenses grouped by date
- **Weekly Summary**: Last 7 days total
- **Monthly Summary**: Last 30 days total  
- **Yearly Summary**: Last 365 days total
- **Category Breakdown**: Expenses grouped by category

### URL Routes
- `/` - Main dashboard (list all expenses + add new)
- `/edit/<id>/` - Edit existing expense
- `/delete/<id>/` - Delete expense (POST only)

## Development Workflow

### Adding new Tailwind classes
After adding Tailwind classes to templates, recompile CSS:
```powershell
cd mysite
npx tailwindcss -i ./myapp/static/myapp/src.css -o ./myapp/static/myapp/output.css
```

### Making database changes
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Running tests
```powershell
python manage.py test
```

## Common Issues

**Tailwind styles not applying?**
- Make sure you've compiled the CSS: `npx tailwindcss -i ... -o ...`
- Check that `base.html` loads `output.css` (not `styles.css`)
- Verify `tailwind.config.js` content paths include your templates

**Module not found errors?**
- Ensure virtual environment is activated
- Check imports use relative paths (e.g., `from . import views`)

## Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Budget tracking with alerts
- [ ] Receipt image uploads
- [ ] Export to CSV/PDF
- [ ] Data visualization charts (Chart.js)
- [ ] Recurring expenses
- [ ] Search and advanced filtering


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
