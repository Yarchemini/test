import pytest
from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест успешного выполнения функции с выводом лога в консоль."""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест записи ошибки функции при выводе лога в консоль."""

    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path: Any) -> None:
    """Тест успешного выполнения функции с записью лога в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    assert multiply(3, 4) == 12
    assert log_file.read_text(encoding="utf-8") == "multiply ok\n"


def test_log_file_error(tmp_path: Any) -> None:
    """Тест записи ошибки функции в файл."""
    log_file = tmp_path / "test_log_error.txt"

    @log(filename=str(log_file))
    def cause_error() -> None:
        raise ValueError("Some test error")

    with pytest.raises(ValueError):
        cause_error()

    file_content = log_file.read_text(encoding="utf-8")
    assert "cause_error error: ValueError. Inputs: (), {}" in file_content
