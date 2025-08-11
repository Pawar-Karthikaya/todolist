## Todolist (Django)

A simple, modern web-based to-do list application built with Django. It supports user registration/login, profile management with profile pictures, and full CRUD for tasks with priorities, statuses, due dates, and completion tracking.

### Features
- **Authentication**: Register, login, logout
- **Task management**: Create, edit, delete, and toggle completion
- **Task metadata**: Priority (low/medium/high), status (pending/in-progress/completed), due date
- **Dashboard**: Quick stats (totals, completed, pending, high priority, due today)
- **User profile**: Update name/email, bio, phone, date of birth, and upload a profile picture
- **Media handling**: User profile images stored under `media/profile_pics/`

### Tech stack
- **Backend**: Django 5
- **Database**: SQLite (development default)
- **Templates/Styling**: Django templates + Bootstrap classes

### Project structure
- `todolist/todo/manage.py`: Django entry point
- `todolist/todo/todo/settings.py`: Project settings (static/media, auth redirects, etc.)
- `todolist/todo/tasks/`: App with models, forms, views, urls, templates
- `todolist/todo/static/`: Project static assets (optional/local)
- `todolist/todo/media/`: Uploaded user media (created at runtime)

### Prerequisites
- Python 3.10+ recommended
- pip

### Setup (local)
1) Move into the Django project directory:
```bash
cd todolist/todo
```

2) Create and activate a virtual environment:
- Windows (PowerShell):
```powershell
python -m venv ..\venv
..\venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
python -m venv ../venv
source ../venv/bin/activate
```

3) Install dependencies:
```bash
pip install -r ../requirements.txt
```

4) Apply database migrations:
```bash
python manage.py migrate
```

5) (Optional) Create an admin user:
```bash
python manage.py createsuperuser
```

6) Run the development server:
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

### Default routes
- `/` → Home/Dashboard (requires login)
- `/register/` → Register
- `/login/` → Login
- `/logout/` → Logout
- `/profile/` → View/Update profile (with profile picture upload)
- `/task/add/` → Create task
- `/task/<id>/edit/` → Edit task
- `/task/<id>/delete/` → Delete task
- `/task/<id>/toggle/` → Toggle completion (AJAX)

### Static & media
- Static: `STATIC_URL = 'static/'`, local directory: `todolist/todo/static/`
- Media: `MEDIA_URL = '/media/'`, media root: `todolist/todo/media/`
- In development (`DEBUG=True`), media files are served automatically via project `urls.py`.

### Environment and production notes
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` in `todolist/todo/todo/settings.py` for production.
- Provide a secure `SECRET_KEY` via environment or settings for production.
- Collect static files for production:
```bash
python manage.py collectstatic
```

### License
Specify your preferred license here (e.g., MIT) if you plan to open-source this project.

