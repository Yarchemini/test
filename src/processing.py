def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по дате в формате ISO (по умолчанию по убыванию)."""
    return sorted(data, key=lambda item: item.get("date", ""), reverse=reverse)


# Блок проверки работы функций на входных данных из ТЗ
if __name__ == "__main__":
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("Проверка фильтрации (по умолчанию EXECUTED):")
    print(filter_by_state(test_data))

    print("\nПроверка фильтрации (CANCELED):")
    print(filter_by_state(test_data, "CANCELED"))

    print("\nПроверка сортировки по дате (по убыванию):")
    print(sort_by_date(test_data))
