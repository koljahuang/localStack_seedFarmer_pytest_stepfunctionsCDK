def lambda_handler(event, context):
    print("status lambda_handler is called....") # this will not be print
    if event["status"] == "SUCCEEDED":
        return {"status": "SUCCEEDED", "event": event}
    else:
        return {"status": "FAILED", "event": event}  # output