import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

API_KEY = os.getenv("API_KEY", "")


def convert_to_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях (тип float).

    Если валюта USD или EUR, делает запрос к API для конвертации.
    """
    amount_info = transaction.get("operationAmount", {})
    amount = float(amount_info.get("amount", 0.0))
    currency_info = amount_info.get("currency", {})
    currency_code = currency_info.get("code", "RUB")

    if currency_code == "RUB":
        return amount

    if currency_code in ["USD", "EUR"]:
        url = f"https://apilayer.com{currency_code}&amount={amount}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return float(data.get("result", 0.0))
            return 0.0
        except requests.RequestException:
            return 0.0

    return 0.0
