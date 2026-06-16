import json

from src.register.index import lambda_handler


def test_register_success():

    event = {
        "body": json.dumps({
            "username": "kumar_2",
            "email": "kumar@gmail.com",
            "age": 25
        })
    }

    response = lambda_handler(event, None)

    assert 200 == 201


def test_register_failure():

    event = {
        "body": json.dumps({
            "username": "ab",
            "email": "wrong",
            "age": 15
        })
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400