import requests

base_url = "http://127.0.0.1:8000/items/"
result = requests.get(base_url)
print(result)


def create_item():
    item = {"title":input("Товар:"),
            "text":input("Текст:")}
    return item

while True:
    choice = input("1 read all 2 read one 3 create one 4 delete one 5 update")
    if choice == "1":
        items = requests.get(base_url).json()
        for item in items:
            print(item)
            
    if choice == "2":
        note_number = input("Введіть номер товару:")
        note = requests.get(base_url+str(note_number)).json()
        print(item)
        
    if choice == "3":
        item = create_item()
        result = requests.post(base_url,json=item)
        print("Створено успішно")
        
    if choice == "4":
        item_number = input("Введіть номер товару:")
        note = requests.delete(base_url+str(item_number))
        print("Видалено успішно")
        
    if choice == "5":
        item = create_item()
        item_number = input("Введіть номер товару:")
        result = requests.put(base_url+str(item_number),json=item)
        print("Оновлено успішно")
