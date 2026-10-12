import os
from typing import Any

import pandas as pd


def read_csv_file(file_path: str) -> list[dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    if not os.path.exists(file_path):
        return []

    try:
        # Читаем CSV с разделителем точки с запятой (стандарт для Skypro)
        df = pd.read_csv(file_path, sep=";")

        # Заменяем NaN (пустоты) на пустые строки, чтобы не сломать типы
        df = df.fillna("")

        # Превращаем DataFrame в список словарей
        return list(df.to_dict(orient="records"))
    except Exception:
        return []


def read_excel_file(file_path: str) -> list[dict[str, Any]]:
    """Считывает финансовые операции из Excel-файла и возвращает список словарей."""
    if not os.path.exists(file_path):
        return []

    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path)

        # Заменяем NaN на пустые строки
        df = df.fillna("")

        # Превращаем DataFrame в список словарей
        return list(df.to_dict(orient="records"))
    except Exception:
        return []
