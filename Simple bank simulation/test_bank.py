import pytest
from bank import deposit, withdraw

def test_deposit_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "50")
    assert deposit(100.0) == 150.0

def test_deposit_invalid_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "-10")
    assert deposit(100.0) == 100.0

def test_withdraw_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "30")
    assert withdraw(100.0) == 70.0

def test_withdraw_insufficient(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "200")
    assert withdraw(100.0) == 100.0
