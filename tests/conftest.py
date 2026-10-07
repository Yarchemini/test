import pytest


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Фикстура, возвращающая тестовый список транзакций."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "PENDING", "date": "2020-10-14T08:21:33.419441"},
        {"id": 5, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # Одинаковая дата со 2-й
    ]
