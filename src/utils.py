import json
import logging
import os
from typing import Any

# Создаем папку logs в корне, если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join("logs", "utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей."""
    logger.debug(f"Попытка чтения JSON-файла по пути: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан. Найдено транзакций: {len(data)}")
                return data
            logger.error(f"Файл {file_path} содержит не список, а {type(data).__name__}")
            return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except OSError as e:
        logger.error(f"Ошибка ввода-вывода при работе с файлом {file_path}: {e}")
        return []
