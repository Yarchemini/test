import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 3),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("NON_EXISTENT", 0),
    ],
)
def test_filter_by_state(sample_transactions: list[dict], state: str, expected_count: int) -> None:
    """Тестирование фильтрации по разным статусам с использованием фикстуры."""
    filtered = filter_by_state(sample_transactions, state)
    assert len(filtered) == expected_count
    for item in filtered:
        assert item["state"] == state


def test_sort_by_date_descending(sample_transactions: list[dict]) -> None:
    """Тестирование сортировки по дате по убыванию (по умолчанию)."""
    sorted_data = sort_by_date(sample_transactions)
    assert sorted_data[0]["id"] == 4  # Самая свежая дата 2020 года
    assert sorted_data[-1]["id"] in [2, 5]  # Самые старые даты 2018 года


def test_sort_by_date_ascending(sample_transactions: list[dict]) -> None:
    """Тестирование сортировки по дате по возрастанию."""
    sorted_data = sort_by_date(sample_transactions, reverse=False)
    assert sorted_data[0]["id"] in [2, 5]  # Самые старые первыми
    assert sorted_data[-1]["id"] == 4  # Самая свежая последняя

