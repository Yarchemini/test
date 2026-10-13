import sys

sys.path.insert(0, "C:/Users/SPO/PycharmProjects/prj")

from src.search import process_bank_operations, process_bank_search


def test_process_bank_search() -> None:
    data = [{"description": "Перевод организации"}, {"description": "Открытие вклада"}]
    assert process_bank_search(data, "Перевод") == [{"description": "Перевод организации"}]
    assert process_bank_search(data, "не найду") == []


def test_process_bank_operations() -> None:
    data = [{"description": "Вклад"}, {"description": "Вклад"}, {"description": "Перевод"}]
    assert process_bank_operations(data, ["Вклад", "Перевод"]) == {"Вклад": 2, "Перевод": 1}
