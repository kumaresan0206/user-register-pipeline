import pytest

from src.register.validator import validate_data


def test_valid_user():

    user = {"username": "kumar_2", "email": "kumar@gmail.com", "age": 25}

    assert validate_data(user) is True


def test_missing_username():

    with pytest.raises(ValueError):
        validate_data({"email": "kumar@gmail.com", "age": 25})


def test_invalid_email():

    with pytest.raises(ValueError):
        validate_data({"username": "kumar_2", "email": "abc", "age": 25})


def test_invalid_age():

    with pytest.raises(ValueError):
        validate_data({"username": "kumar_2", "email": "kumar@gmail.com", "age": 15})


def test_short_username():

    with pytest.raises(ValueError):
        validate_data({"username": "ab", "email": "kumar@gmail.com", "age": 25})
