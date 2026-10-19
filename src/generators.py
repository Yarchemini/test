from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """Фильтрует транзакции по коду валюты и возвращает итератор."""
    for transaction in transactions:
        amount_info = transaction.get("operationAmount", {})
        currency_info = amount_info.get("currency", {})
        if currency_info.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, end + 1):
        str_num = f"{number:016d}"
        formatted_card = f"{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:]}"
        yield formatted_card


# Блок проверки работы генераторов на данных из ТЗ
if __name__ == "__main__":
    test_transactions = [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
    ]

    print("--- Тест фильтрации по валюте USD ---")
    usd_gen = filter_by_currency(test_transactions, "USD")
    print(next(usd_gen))
    print(next(usd_gen))

    print("\n--- Тест описаний операций ---")
    desc_gen = transaction_descriptions(test_transactions)
    for _ in range(3):
        print(next(desc_gen))

    print("\n--- Тест генератора карт ---")
    for card in card_number_generator(1, 3):
        print(card)
