import pytest
from parameterized import parameterized
from main import show_all_docs_info, get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_doc, delete_doc

class TestFunction:
    def test_show_all_docs_info(self): #тест вывода всех документов, команда l
        list_return = []
        list_return.append('Список всех документов:\n')
        list_return.append('{} "{}" "{}"'.format('passport', '2207 876234', 'Василий Гупкин'))
        list_return.append('{} "{}" "{}"'.format('invoice', '11-2', 'Геннадий Покемонов'))
        list_return.append('{} "{}" "{}"'.format('insurance', '10006', 'Аристарх Павлов'))
        result = show_all_docs_info()
        assert set(result) == set(list_return)
    @parameterized.expand(
        [
            ("2207 876234","Василий Гупкин"),
            ("11-2","Геннадий Покемонов"),
            ("10006","Аристарх Павлов"),
        ],
    )
    def test_get_doc_owner_name(self, user_doc_nomer, etalon): #тест вывода владельца документа, команда 'p'
        result = get_doc_owner_name(user_doc_nomer)
        assert result == etalon
    def test_get_all_doc_owners_names(self): #тест вывода списка владельцев документов, команда 'ap'
        etalon = ["Василий Гупкин","Геннадий Покемонов","Аристарх Павлов"]
        result = get_all_doc_owners_names()
        assert  set(etalon) == set(result)
    @parameterized.expand(
        [
            ("2207 876234",'1'),
            ("11-2",'1'),
            ("10006",'2'),
        ],
    )
    def test_get_doc_shelf(self, user_doc_number, etalon): #тест вывода номера полки, команда 's'
        result = get_doc_shelf(user_doc_number)
        assert result == etalon
    @parameterized.expand(
        [
            ("111","passport","Васильев","1","1"),
            ("222","passport","Петров","2","2"),
            ("333","passport","Васечкин","3","3"),
        ],
    )
    def test_add_new_doc(self, doc_number, doc_type, doc_owner_name, doc_shelf_number, etalon):
        result = add_new_doc(doc_number, doc_type, doc_owner_name, doc_shelf_number)
        assert result == etalon
    @parameterized.expand(
        [
            ("2207 876234","2207 876234",True),
            ("11-2","11-2",True),
            ("10006","10006",True),
        ],
    )
    def test_delete_doc(self, doc_number, etalon_doc, etalon_del):
        result_doc, result_del = delete_doc(doc_number)
        assert result_doc == etalon_doc and result_del == etalon_del