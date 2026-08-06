#!/sh
set -e

echo "Collecting static Bootstrap files..."
python manage.py collectstatic --noinput

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn server..."
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:8000


# force updatess