import os
import sys
from typing import Any

# Наш железобетонный колледжный костыль для путей
sys.path.insert(0, "C:/Users/SPO/PycharmProjects/prj")

from src.csv_excel import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная логика взаимодействия с пользователем."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    data: list[dict[str, Any]] = []
    base_dir = "data"

    if choice == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.")
        data = read_json_file(os.path.join(base_dir, "operations.json"))
    elif choice == "2":
        print("\nПрограмма: Для обработки выбран CSV-файл.")
        data = read_csv_file(os.path.join(base_dir, "transactions.csv"))
    elif choice == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файл.")
        data = read_excel_file(os.path.join(base_dir, "transactions_excel.xlsx"))
    else:
        print("\nПрограмма: Неверный выбор меню. Завершение программы.")
        return

    # Валидация статуса (петля, пока пользователь не введет нормально)
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print("\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").strip().upper()

        if status_input in valid_statuses:
            data = filter_by_state(data, status_input)
            print(f'\nПрограмма: Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'\nПрограмма: Статус операции "{status_input}" недоступен.')

    # Сортировка по дате
    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ").strip().lower()
    if sort_choice == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")
        order_choice = input("Пользователь: ").strip().lower()
        descending = True if order_choice == "по убыванию" else False
        data = sort_by_date(data, descending)

    # Фильтр только рубли
    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    rub_choice = input("Пользователь: ").strip().lower()
    if rub_choice == "да":
        data = [
            t
            for t in data
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            or t.get("currency_code") == "RUB"
        ]

    # Фильтр по слову в описании (наши регулярки!)
    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    word_choice = input("Пользователь: ").strip().lower()
    if word_choice == "да":
        search_word = input("Пользователь (введите слово): ").strip()
        data = process_bank_search(data, search_word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    if not data:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(data)}\n")
    for t in data:
        date_str = get_date(t.get("date", ""))
        desc = t.get("description", "Неизвестная операция")

        from_acc = t.get("from") or t.get("from_account") or ""
        to_acc = t.get("to") or t.get("to_account") or ""

        if from_acc:
            direction = f"{mask_account_card(from_acc)} -> {mask_account_card(to_acc)}"
        else:
            direction = mask_account_card(to_acc)

        amount = t.get("operationAmount", {}).get("amount") or t.get("amount") or "0"
        currency = t.get("operationAmount", {}).get("currency", {}).get("code") or t.get("currency_code") or "RUB"

        print(f"{date_str} {desc}")
        print(direction)
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
