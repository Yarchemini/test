from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список словарей по ключу 'date'."""
    valid_data = [item for item in data if "date" in item]

    sorted_data = sorted(
        valid_data,
        key=lambda x: str(x.get("date", "")),
        reverse=reverse
    )
    return sorted_data
