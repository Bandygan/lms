import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imcslms.settings')

app = Celery('imcslms')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_submit_status': {
        'task': 'celery_app.tasks.update_submit_status',
        'schedule': 10.0,
    }
}
