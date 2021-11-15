import json


def hello(event, context):
    msg = event['message']
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": msg,
    }

    return {"statusCode": 200, "body": json.dumps(body)}