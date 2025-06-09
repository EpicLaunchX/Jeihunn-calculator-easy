import builtins

import pytest

from pytemplate.entrypoints.cli.main import main


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["2", "3", "add"], 5),
        (["7", "2", "subtract"], 5),
        (["4", "5", "multiply"], 20),
        (["10", "2", "divide"], 5),
    ],
)
def test_main_valid_inputs(monkeypatch, inputs, expected):
    monkeypatch.setattr(builtins, "input", lambda prompt="": inputs.pop(0))
    assert main() == expected


def test_main_divide_by_zero(monkeypatch):
    inputs = ["5", "0", "divide"]
    monkeypatch.setattr(builtins, "input", lambda prompt="": inputs.pop(0))
    with pytest.raises(ZeroDivisionError):
        main()


@pytest.mark.parametrize(
    "inputs, error_type",
    [
        (["foo", "3", "add"], ValueError),
        (["2", "bar", "add"], ValueError),
        (["1.5", "2.5", "multiply"], ValueError),
    ],
)
def test_main_non_integer_input(monkeypatch, inputs, error_type):
    monkeypatch.setattr(builtins, "input", lambda prompt="": inputs.pop(0))
    with pytest.raises(error_type):
        main()


def test_main_invalid_action(monkeypatch):
    inputs = ["5", "3", "mod"]
    monkeypatch.setattr(builtins, "input", lambda prompt="": inputs.pop(0))
    with pytest.raises(ValueError, match="Invalid action"):
        main()


def test_main_action_case_insensitive(monkeypatch):
    inputs = ["8", "2", "DIVIDE"]
    monkeypatch.setattr(builtins, "input", lambda prompt="": inputs.pop(0))
    assert main() == 4
