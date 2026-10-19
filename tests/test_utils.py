import json
from unittest.mock import mock_open, patch
from src.utils import read_json_file


def test_read_json_file_success() -> None:
    """Тест успешного чтения корректного JSON-файла."""
    mock_data = [{"id": 1, "state": "EXECUTED"}]
    mock_json = json.dumps(mock_data)

    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data=mock_json)):
        assert read_json_file("dummy.json") == mock_data


def test_read_json_file_not_found() -> None:
    """Тест ситуации, когда файл не существует."""
    with patch("os.path.exists", return_value=False):
        assert read_json_file("non_existent.json") == []


def test_read_json_file_invalid_json() -> None:
    """Тест обработки битого (некорректного) JSON."""
    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data="invalid json")):
        assert read_json_file("bad.json") == []


def test_read_json_file_not_a_list() -> None:
    """Тест ситуации, когда JSON содержит словарь вместо списка."""
    mock_json = json.dumps({"key": "value"})
    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data=mock_json)):
        assert read_json_file("dict.json") == []
