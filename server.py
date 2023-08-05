'''
Створити Серверний додаток XML RPC який має декілька функцій
1 створення файлу отримує назву файлу і створює в директорії
2 читання файлу отримує назву файлу читає його і надсилає результат
3 запис до файлу вказується назва файлу і текст який необхідно записати
4 функція перегляду наявних файлів
'''
import glob
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            f.write('')
        return f"Файл {file_name} створено успішно."
    except Exception as e:
        return f"Помилка при створенні файлу: {str(e)}"


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Помилка при читанні файлу: {str(e)}"


def write_to_file(file_name, text):
    try:
        with open(file_name, 'a') as f:
            f.write(text)
        return "Текст успішно записано до файлу."
    except Exception as e:
        return f"Помилка при записі до файлу: {str(e)}"


def list_files(path):
    try:
        return glob.glob(f"{path}*")
    except Exception as e:
        return f"Помилка при отриманні списку файлів: {str(e)}"


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(create_file, 'create_file')
server.register_function(read_file, 'read_file')
server.register_function(write_to_file, 'write_to_file')
server.register_function(list_files, 'list_files')
print("Listening on port 8000...")
server.serve_forever()
