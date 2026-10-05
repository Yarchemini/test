import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")


def convert_to_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях (тип float).

    Получает текущий курс валюты через API и конвертирует сумму вручную.
    """
    amount_info = transaction.get("operationAmount", {})
    amount = float(amount_info.get("amount", 0.0))
    currency_info = amount_info.get("currency", {})
    currency_code = currency_info.get("code", "RUB")

    if currency_code == "RUB":
        return amount

    if currency_code in ["USD", "EUR"]:
        # Официальный URL для получения текущих курсов валют
        url = "https://api.apilayer.com/exchangerates_data/latest"

        # Параметры по документации: базовая валюта и целевая
        params = {
            "base": currency_code,
            "symbols": "RUB"
        }
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                # Извлекаем курс из словаря rates
                rate = float(data.get("rates", {}).get("RUB", 0.0))
                return amount * rate
            return 0.0
        except requests.RequestException:
            return 0.0

    return 0.0
