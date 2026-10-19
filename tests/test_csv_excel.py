import sys

sys.path.insert(0, "C:/Users/SPO/PycharmProjects/prj")

import unittest.mock

import pandas as pd

from src.csv_excel import read_csv_file, read_excel_file


def test_read_csv_file_success() -> None:
    """Тест успешного чтения CSV через mock-датафрейм."""
    mock_data = [{"amount": 100, "id": 1}]
    mock_df = pd.DataFrame(mock_data)

    # Мокаем сразу и проверку файла, и чтение pandas
    with unittest.mock.patch("os.path.exists", return_value=True):
        with unittest.mock.patch("pandas.read_csv", return_value=mock_df):
            result = read_csv_file("fake.csv")
            assert result == mock_data


def test_read_csv_file_not_found() -> None:
    """Тест возврата пустого списка, если CSV-файл не существует."""
    with unittest.mock.patch("os.path.exists", return_value=False):
        assert read_csv_file("non_existent.csv") == []


def test_read_excel_file_success() -> None:
    """Тест успешного чтения Excel через mock-датафрейм."""
    mock_data = [{"amount": 200, "id": 2}]
    mock_df = pd.DataFrame(mock_data)

    # Мокаем сразу и проверку файла, и чтение pandas
    with unittest.mock.patch("os.path.exists", return_value=True):
        with unittest.mock.patch("pandas.read_excel", return_value=mock_df):
            result = read_excel_file("fake.xlsx")
            assert result == mock_data


def test_read_excel_file_not_found() -> None:
    """Тест возврата пустого списка, если Excel-файл не существует."""
    with unittest.mock.patch("os.path.exists", return_value=False):
        assert read_excel_file("non_existent.xlsx") == []
 