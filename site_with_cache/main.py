'''
Підключити до фласк сайту Кешування (flask-cache)
Створити маршрут hard_task який має виконуватись 5 секунд
потрібно закешувати маршрут і перевірити працездатність
P.S. або файловий кеш або redis на Ваш вибір
'''
import time
from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": False,
    "CACHE_TYPE": 'filesystem',
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_DIR": 'cache_dir',
    "CACHE_THRESHOLD": 100
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/hard_task')
@cache.cached(timeout=10)
def hard_task():
    time.sleep(5)
    return "Task completed!"


app.run()
