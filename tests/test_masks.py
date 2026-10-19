import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("123", "Неверный формат карты"),
        ("abcdefghijklmnop", "Неверный формат карты"),
        ("", "Неверный формат карты"),
    ],
)
def test_get_mask_card_number(card_num: str, expected: str) -> None:
    """Тестирование маскирования карт, включая некорректные форматы."""
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "acc_num, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345", "**2345"),
        ("123", "Неверный формат счета"),
        ("abc", "Неверный формат счета"),
        ("", "Неверный формат счета"),
    ],
)
def test_get_mask_account(acc_num: str, expected: str) -> None:
    """Тестирование маскирования счетов, включая короткие номера."""
    assert get_mask_account(acc_num) == expected
