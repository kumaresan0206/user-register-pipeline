import json

def success_response(data: dict, status_code: int = 200) -> dict:
    
    return {
        "statusCode": status_code,
        "body": json.dumps({
            "success": True,
            "message": "User registered successfully",
            "data": data
        })
    }

def error_response(error_message: str, status_code: int = 400) -> dict:
    
    return {
        "statusCode": status_code,
        "body": json.dumps({
            "success": False,
            "message": error_message
        })
    }