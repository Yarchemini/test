import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions_mock() -> list[dict]:
    """Фикстура с тестовыми данными транзакций из ТЗ."""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод со счета на счет"},
        {"id": 3, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Оплата услуг"},
    ]


def test_filter_by_currency_success(transactions_mock: list[dict]) -> None:
    """Тест успешной фильтрации транзакций по валюте."""
    usd_iterator = filter_by_currency(transactions_mock, "USD")
    res1 = next(usd_iterator)
    res2 = next(usd_iterator)
    assert res1["id"] == 1
    assert res2["id"] == 2
    with pytest.raises(StopIteration):
        next(usd_iterator)


def test_filter_by_currency_empty() -> None:
    """Тест фильтрации пустого списка транзакций."""
    iterator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(iterator)


def test_filter_by_currency_not_found(transactions_mock: list[dict]) -> None:
    """Тест ситуации, когда транзакций с указанной валютой нет."""
    iterator = filter_by_currency(transactions_mock, "EUR")
    with pytest.raises(StopIteration):
        next(iterator)


def test_transaction_descriptions_success(transactions_mock: list[dict]) -> None:
    """Тест извлечения описаний операций."""
    desc_iterator = transaction_descriptions(transactions_mock)
    assert next(desc_iterator) == "Перевод организации"
    assert next(desc_iterator) == "Перевод со счета на счет"
    assert next(desc_iterator) == "Оплата услуг"


def test_transaction_descriptions_empty() -> None:
    """Тест извлечения описаний из пустого списка."""
    iterator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(iterator)


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (999, 1000, ["0000 0000 0000 0999", "0000 0000 0000 1000"]),
    ],
)
def test_card_number_generator_range(start: int, end: int, expected: list[str]) -> None:
    """Тестирование диапазонов и форматирования номеров карт."""
    gen = card_number_generator(start, end)
    assert list(gen) == expected
