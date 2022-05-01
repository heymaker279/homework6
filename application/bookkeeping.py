documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []}


'''Проверка имени по номеру документа'''
def people_doc_number(documents, num):
    num = str(num)
    for person_dict in documents:
        if num == person_dict["number"]:
            result = person_dict["name"]
            return result
    for person_dict in documents:
        if num != person_dict["number"]:
            return "Такого номера не существует."

'''Проверка ячейки хранения по номеру документа'''
def shelf_doc_number(directories, n):
    n = str(n)
    for key, values in enumerate(directories.values()):
        if n in values:
            directories_list = list(directories)
            result = int(directories_list[key])
            return result
    for values in directories.values():
        if n not in values:
            return "Нет данных"


def list_doc(documents):
    db_list = []
    for lst in documents:
        if type(lst) == dict:
            for key, value in lst.items():
                db_list.append(f"{value}")
    result = db_list
    for lst in documents:
        if type(lst) != dict:
            result = "Неверный тип данных."
    return result


def add_new_person(documents, directories, type_doc, number, name, num_direct):
    if type(name) and type(type_doc) and type(num_direct) and type(number) is not str:
        raise TypeError("Введён неверный тип данных!")
    new_person = {"type": type_doc, "number": number, "name": name}
    if new_person not in documents:
        documents.append(new_person)
    else:
        print("Этот пользователь есть в базе")
    if num_direct not in directories.keys():
        directories[num_direct] = []
        directories[num_direct].append(number)
    elif num_direct in directories.keys():
        directories[num_direct].append(number)
    return documents, directories


def insert_command(command):
    if command == "p":
        num = input("Введите номер документа:")
        return people_doc_number(documents, num)
    elif command == "s":
        n = input("Введите номер документа:")
        return shelf_doc_number(directories, n)
    elif command == "l":
        return list_doc(documents)
    elif command == "a":
        name = input("Введите имя: ").title()
        number = input("Введите номер документа: ")
        type_doc = input("Введите тип документа: ")
        num_direct = input('Выберите номер полки хранения:')
        return add_new_person(documents, directories, name, number, type_doc, num_direct)
    elif command == 'q':
        quit(insert_command)

    else:
        return "Неверная команда"

def run():
    while True:
        command = input("Введите команду:").lower()
        print(insert_command(command))



