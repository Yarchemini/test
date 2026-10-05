import json
import os
from typing import Any


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей.

    Если файл пустой, не найден или содержит не список, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []
