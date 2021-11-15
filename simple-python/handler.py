import json


def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event
    }
    body["Lambda function ARN"] = context.invoked_function_arn
    body["CloudWatch log stream name"] = context.log_stream_name
    body["CloudWatch log group name"] = context.log_group_name
    body["Lambda Request ID"] = context.aws_request_id
    body["Lambda function memory limits in MB"] = context.memory_limit_in_mb

    return {"statusCode": 200, "body": json.dumps(body)}
