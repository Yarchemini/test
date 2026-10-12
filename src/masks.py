import logging
import os

# Создаем папку logs в корне, если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

log_path = os.path.join("logs", "masks.log")
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формат XXXX XX** **** XXXX."""
    logger.debug(f"Начало маскирования номера карты: {card_number}")

    clean_number = card_number.replace(" ", "")

    if not clean_number.isdigit() or len(clean_number) != 16:
        logger.error(
            f"Некорректный номер карты: '{card_number}'. Должно быть 16 цифр."
        )
        return "Неверный формат карты"

    masked = (
        f"{clean_number[:4]} {clean_number[4:6]}** "
        f"**** {clean_number[12:]}"
    )
    logger.info("Номер карты успешно замаскирован.")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формат **XXXX."""
    logger.debug(f"Начало маскирования номера счета: {account_number}")

    clean_account = account_number.replace(" ", "")

    if not clean_account.isdigit() or len(clean_account) < 4:
        logger.error(
            f"Некорректный номер счета: '{account_number}'. "
            f"Должно быть минимум 4 цифры."
        )
        return "Неверный формат счета"

    masked = f"**{clean_account[-4:]}"
    logger.info("Номер счета успешно замаскирован.")
    return masked
