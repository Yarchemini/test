import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict[str, Any]], search_str: str) -> list[dict[str, Any]]:
    """Ищет транзакции по совпадению строки в поле description с помощью регулярных выражений."""
    if not search_str:
        return data

    result = []
    # Компилируем шаблон, игнорируя регистр букв для удобства поиска
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)

    for transaction in data:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)

    return result


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество транзакций для каждой категории из переданного списка с помощью Counter."""
    # Вытаскиваем все описания из транзакций
    descriptions = [transaction.get("description", "") for transaction in data if "description" in transaction]

    # Счетчик из библиотеки collections
    counts = Counter(descriptions)

    # Возвращаем словарь с количеством операций для нужных категорий
    return {category: counts[category] for category in categories}
