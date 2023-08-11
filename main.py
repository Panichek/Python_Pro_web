'''
Встановити RabbitMq по теоретичній частині
створити функцію hard_task яка виконує time sleep() на 3 секунди після чого до файлу results.txt записує текст "Виконано успішно"
'''
from flask import Flask
from celery_app import make_celery
import time
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Flask(__name__)
app.config.update(CELERY_CONFIG={
    'broker_url': 'amqp://guest:guest@localhost:5672',
    'result_backend': 'db+sqlite:///db.db',
})

celery = make_celery(app)

@celery.task(name="new task")
def hard_task():
    time.sleep(3)
    return "ok"


@app.route("/")
def index():
    hard_task.delay()
    return "Виконано успішно"

if __name__ == "__main__":
    app.run()
