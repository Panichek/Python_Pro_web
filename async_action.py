'''
Створити асинхронний парсер api
отримати всі дані із https://jsonplaceholder.typicode.com/todos
'''
import asyncio
import aiohttp

base_url = "https://jsonplaceholder.typicode.com/todos/"


async def parse_page(url, session):
    async with session.get(url) as response:
        return await response.json()


async def my_action():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(1, 101):
            task = asyncio.create_task(parse_page(base_url + str(i), session))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)


asyncio.run(my_action())

import requests

base_url = "https://jsonplaceholder.typicode.com/todos/"
for i in range(1, 101):
    print(requests.get(base_url + str(i)).json())

