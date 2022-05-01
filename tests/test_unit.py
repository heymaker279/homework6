import unittest
from application.bookkeeping import people_doc_number, shelf_doc_number, list_doc, add_new_person
documents = [
    {"type": "1", "number": "10", "name": "100"},
]

directories = {
    '1': ['10', '20', '30'],
    '2': ['40'],
    '3': []}

class TestFunctionsBookkeeping(unittest.TestCase):
    '''Тест проверки добавления данных'''
    def test_add_new_person(self):# проверка на добавление новых данных
        self.assertEqual(add_new_person(documents, directories, '2', '20', '200', '1'), ([
            {'name': '100', 'number': '10', 'type': '1'},
            {'name': '200', 'number': '20', 'type': '2'}],
            {'1': ['10', '20', '30', '20'], '2': ['40'], '3': []})
            )

    @unittest.expectedFailure
    def test_add_new_person_fail(self):  # проверка на добавление некорректных данных
        self.assertEqual(add_new_person(documents, directories, 2.4, [20], {200}, 1), ([
            {'name': '100', 'number': '10', 'type': '1'},
            {'name': '200', 'number': '20', 'type': '2'}],
            {'1': ['10', '20', '30', '20'], '2': ['40'], '3': []})
            )


    '''Тест проверки имени по номеру документа'''
    def test_people_doc_number(self):
        self.assertEqual(people_doc_number(documents, 10), "100")
        self.assertEqual(people_doc_number(documents, 1000), "Такого номера не существует.")

    '''Тест проверки ячейки хранения по номеру документа'''
    def test_shelf_doc_number(self):
        self.assertEqual(shelf_doc_number(directories, 10), 1)
        self.assertEqual(shelf_doc_number(directories, 1000), "Нет данных")

    '''Тест на неправильный тип'''
    @unittest.expectedFailure
    def test_shelf_doc_number_fail(self):
        self.assertEqual(shelf_doc_number(directories, 10006), "2")

    '''Тест на корректность отображения данных'''
    def test_list_doc(self):
        self.assertEqual(list_doc(documents), ['1', '10', '100', '2', '20', '200'])
        self.assertEqual(list_doc({'1': 1, '2': 2}), "Неверный тип данных.")

    @unittest.expectedFailure
    def test_list_doc_fail(self):# проверка на неудачный результат после добавления данных
        self.assertEqual(list_doc(documents), ['1', '10', '100'])



