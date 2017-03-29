web: python manage.py collectstatic --noinput; newrelic-admin run-program gunicorn badgermapping.wsgi -b 0.0.0.0:$PORT -k gevent
