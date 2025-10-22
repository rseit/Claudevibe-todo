# TaskFlow - Todo Application

A Django-based task management application with calendar view and hourly scheduling.

## Features

- User authentication (register, login, logout)
- Monthly calendar view with task indicators
- Hourly schedule (4 AM - 10 PM)
- Task management (create, edit, delete, mark complete)
- User profiles with statistics
- Responsive design for mobile and desktop

## Security Features

- Environment-based configuration for sensitive settings
- CSRF protection on all state-changing operations
- User authorization checks on all task operations
- Secure password handling with Django's built-in validators
- Database indexes for optimized queries

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd todo
```

### 2. Create a virtual environment
```bash
python -m venv virt
source virt/bin/activate  # On Windows: virt\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and update the values:
```bash
cp .env.example .env
```

Generate a new SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit http://localhost:8000 to use the application.

## Production Deployment

### Important Settings for Production

1. Set `DJANGO_DEBUG=False` in your environment
2. Set a strong `DJANGO_SECRET_KEY` (never use the default!)
3. Update `DJANGO_ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Collect static files: `python manage.py collectstatic`
6. Use a production WSGI server like Gunicorn
7. Set up HTTPS with a reverse proxy (nginx/Apache)

### Example Production Setup

```bash
# Install production dependencies
pip install gunicorn psycopg2-binary whitenoise

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn todo.wsgi:application --bind 0.0.0.0:8000
```

## Project Structure

```
todo/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── todo/
│   ├── settings.py      # Main settings
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py
└── website/
    ├── models.py        # Task model
    ├── views.py         # View logic
    ├── urls.py          # App URLs
    ├── admin.py         # Admin configuration
    ├── templates/       # HTML templates
    └── static/          # CSS, JS files
```

## Development Notes

- The application uses SQLite by default for development
- All user tasks are isolated by user authentication
- Database indexes are configured for optimal query performance
- The calendar displays tasks grouped by day with completion status

## Recent Improvements

### Security
- Environment-based configuration for secrets
- Proper error handling with get_object_or_404()
- POST-only mutations with @require_POST decorator
- Fixed bare except clauses

### Performance
- Added database indexes on frequently queried fields
- Composite indexes for user+date and user+completed queries

### Code Quality
- Reorganized imports following Django conventions
- Registered Task model in Django admin
- Fixed template bugs in profile statistics
- Added comprehensive .gitignore

### Documentation
- Created requirements.txt for dependency management
- Added .env.example for environment configuration
- Created this README for setup instructions

## License

This project is for educational purposes.
