import unittest
from application.bookkeeping import people_doc_number, shelf_doc_number, list_doc
documents = [
    {"type": "1", "number": "10", "name": "100"},
    {"type": "2", "number": "20", "name": "200"},
    {"type": "3", "number": "30", "name": "300"}
]

directories = {
    '1': ['10', '20', '30'],
    '2': ['40'],
    '3': []}

class TestFunctionsBookkeeping(unittest.TestCase):
    '''Тест проверки имени по номеру документа'''
    def test_people_doc_number(self):
        self.assertEqual(people_doc_number(documents, 20), "200")
        self.assertEqual(people_doc_number(documents, 1000), "Такого номера не существует.")

    '''Тест проверки ячейки хранения по номеру документа'''
    def test_shelf_doc_number(self):
        self.assertEqual(shelf_doc_number(directories, 20), 1)
        self.assertEqual(shelf_doc_number(directories, 1000), "Нет данных")

    '''Тест на неправильный тип'''
    @unittest.expectedFailure
    def test_shelf_doc_number_fail(self):
        self.assertEqual(shelf_doc_number(directories, 10006), "2")

    '''Тест на корректность отображения данных'''
    def test_list_doc(self):

        list_ = [
            {"1": "1", "2": "2", "3": "3"},
            {"4": "4", "5": "5", "6": "6"},
        ]
        self.assertEqual(list_doc(list_), ['1', '2', '3', '4', '5', '6'])
        self.assertEqual(list_doc({'1': 1, '2': 2}), "Неверный тип данных.")

    @unittest.expectedFailure
    def test_list_doc_fail(self):
        list_ = [
            {"1": "1", "2": "2", "3": 3},
            {"4": 4, "5": "5", "6": "6"},
        ]
        self.assertEqual(list_doc(list_), ['1', '2', 3, 4, '5', '6'])