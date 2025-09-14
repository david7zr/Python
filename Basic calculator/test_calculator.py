import builtins
import pytest
import calculator  # Assumes main file is named calculator.py

# Utility to simulate user input
def mock_input(monkeypatch, inputs):
    """Mock the builtins.input function with a list of values."""
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(it))

def test_addition(monkeypatch):
    mock_input(monkeypatch, ["3", "4"])
    result = calculator.addition()
    assert result == 7

def test_subtract(monkeypatch):
    mock_input(monkeypatch, ["10", "4"])
    result = calculator.subtract()
    assert result == 6

def test_multiply(monkeypatch):
    mock_input(monkeypatch, ["3", "5"])
    result = calculator.multiply()
    assert result == 15

def test_divide(monkeypatch):
    mock_input(monkeypatch, ["20", "4"])
    result = calculator.divide()
    assert result == 5

def test_divide_by_zero(monkeypatch, capsys):
    mock_input(monkeypatch, ["10", "0"])
    result = calculator.divide()
    captured = capsys.readouterr()
