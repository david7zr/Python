import builtins
import pytest
from number_guessing import get_user_guess

def test_valid_input(monkeypatch):
    """Test that a valid number between 1 and 100 is accepted."""
    monkeypatch.setattr(builtins, "input", lambda _: "42")
    guess = get_user_guess()
    assert guess == 42

def test_invalid_input(monkeypatch):
    """Test that invalid input (letters, symbols) is rejected until valid."""
    inputs = iter(["abc", "200", "50"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    guess = get_user_guess()
    assert guess == 50

def test_lower_bound(monkeypatch):
    """Test that 1 is accepted as valid input."""
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    guess = get_user_guess()
    assert guess == 1


def test_upper_bound(monkeypatch):
    """Test that 100 is accepted as valid input."""
    monkeypatch.setattr(builtins, "input", lambda _: "100")
    guess = get_user_guess()
    assert guess == 100
