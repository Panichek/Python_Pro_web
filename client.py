'''
Також реалізувати Клієнтську частину (меню)
1 створити
2 читати
3 записати
4 переглянути файли
'''
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8000") as proxy:
    while True:
        choice = input("1. Створити файл \n"
                       "2. Читати файл \n"
                       "3. Записати до файлу \n"
                       "4. Переглянути файли \n"
                       "5 Вихід: "
                       )
        if choice == '1':
            file_name = input("Введіть назву файлу, який потрібно створити: ")
            data = proxy.create_file(file_name)
            print(f"Файл {file_name} створено успішно.")


        elif choice == '2':
            file_name = input("Введіть назву файлу, який потрібно прочитати: ")
            content = proxy.read_file(file_name)
            print(f"Зміст файлу {file_name}:")
            print(content)

        elif choice == '3':
            file_name = input("Введіть назву файлу, до якого потрібно записати: ")
            text = input("Введіть текст для запису: ")
            result = proxy.write_to_file(file_name, text)
            print(result)

        elif choice == '4':
            path = input("Введіть шлях:")
            print(proxy.list_files(path))

        elif choice == '5':
            print("Вихід.")
            break

        else:
           print("Некоректний вибір. Спробуйте ще раз.")
