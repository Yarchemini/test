import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")


def convert_to_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях (тип float).

    Запрашивает курсы относительно EUR/USD и рассчитывает конвертацию.
    """
    amount_info = transaction.get("operationAmount", {})
    amount = float(amount_info.get("amount", 0.0))
    currency_info = amount_info.get("currency", {})
    currency_code = currency_info.get("code", "RUB")

    if currency_code == "RUB":
        return amount

    if currency_code in ["USD", "EUR"]:
        # Самый стандартный базовый URL, доступный на всех тарифах APILayer
        url = "https://apilayer.com"

        # Запрашиваем курсы для RUB и USD относительно базовой EUR (доступно везде)
        params = {
            "symbols": "RUB,USD",
            "base": "EUR"
        }
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                rates = data.get("rates", {})

                # Курс рубля к евро
                rub_rate = float(rates.get("RUB", 0.0))

                if currency_code == "EUR":
                    return amount * rub_rate

                if currency_code == "USD":
                    # Курс доллара к евро
                    usd_rate = float(rates.get("USD", 0.0))
                    if usd_rate > 0:
                        # Считаем кросс-курс USD -> RUB через EUR
                        return amount * (rub_rate / usd_rate)
            return 0.0
        except requests.RequestException:
            return 0.0

    return 0.0
