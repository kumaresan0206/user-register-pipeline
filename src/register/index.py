import json

from .validator import validate_data
from .response import success_response, error_response


def lambda_handler(event, context):

    try:
        body = json.loads(event["body"])

        validate_data(body)

        return success_response(body, 201)

    except ValueError as ex:
        return error_response(str(ex), 400)

    except Exception as ex:
        print(str(ex))

        return error_response("Internal Server Error", 500)
