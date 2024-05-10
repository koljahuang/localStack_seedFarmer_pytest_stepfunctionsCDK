def lambda_handler(event, context):
    print("submit lambda_handler is called....")
    return {
        "event": event,
        "status": "SUCCEEDED",
    }