from unittest.mock import Mock, patch
import requests
from src.external_api import convert_to_rub


def test_convert_to_rub_ruble() -> None:
    """Тест транзакции, которая изначально в рублях (конвертация не требуется)."""
    transaction = {"operationAmount": {"amount": "150.00", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 150.0


def test_convert_to_rub_usd_success() -> None:
    """Тест успешного ответа от внешнего API при конвертации из USD."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}

    with patch("requests.get", return_value=mock_response):
        assert convert_to_rub(transaction) == 7500.0


def test_convert_to_rub_api_error() -> None:
    """Тест обработки ошибки сервера (status_code != 200)."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        assert convert_to_rub(transaction) == 0.0


def test_convert_to_rub_connection_timeout() -> None:
    """Тест обработки падения соединения (Exception)."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("requests.get", side_effect=requests.RequestException):
        assert convert_to_rub(transaction) == 0.0
