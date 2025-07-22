
# Helpdesk Django App

System zgłoszeń stworzony w Django, gotowy do hostowania na Render.com.

## Uruchomienie lokalne

```bash
python manage.py migrate
python manage.py runserver
```

## Deploy na Render.com

1. Zaloguj się do Render
2. Wybierz **New Web Service**
3. Ustaw:
   - **Build Command**:
     pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
   - **Start Command**:
     gunicorn helpdesk.wsgi
4. W zmiennych środowiskowych ustaw:
   - `DJANGO_SETTINGS_MODULE=helpdesk.settings`
   - `SECRET_KEY=...` (z `settings.py`)
   - `DEBUG=False`
   - `ALLOWED_HOSTS=*`
