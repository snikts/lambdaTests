import boto3
import json

class WidgetRequests:

    def post_update(self, body):
        lambda_client = boto3.client('lambda')
        lambda_payload = body
        response = lambda_client.invoke(FunctionName='widget-request-handler',
                             InvocationType='Event',
                             Payload=json.dumps(lambda_payload))
        return response

    def post_create(self, body):
        lambda_client = boto3.client('lambda')
        lambda_payload = body
        response = lambda_client.invoke(FunctionName='widget-request-handler',
                             InvocationType='Event',
                             Payload=json.dumps(lambda_payload))
        return response

    def post_delete(self, body):
        lambda_client = boto3.client('lambda')
        lambda_payload = body
        response = lambda_client.invoke(FunctionName='widget-request-handler',
                             InvocationType='Event',
                             Payload=json.dumps(lambda_payload))
        return response
