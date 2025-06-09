import builtins

import pytest

from src.pytemplate.entrypoints.cli.main import main


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["2", "3", "add"], 5),
        (["7", "2", "subtract"], 5),
        (["4", "5", "multiply"], 9),
        (["10", "2", "divide"], 5),
    ],
)
def test_main_valid_inputs(monkeypatch, inputs, expected):
    monkeypatch.setattr(builtins, "input", lambda _: inputs.pop(0))
    assert main() == expected


def test_main_invalid_action(monkeypatch):
    inputs = ["5", "4", "mod"]
    monkeypatch.setattr(builtins, "input", lambda _: inputs.pop(0))
    with pytest.raises(ValueError, match="Invalid action"):
        main()
