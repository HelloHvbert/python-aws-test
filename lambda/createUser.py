import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        first_name = body['first_name']
        age = body['age']

        user_id = str(uuid.uuid4())

        table.put_item(Item={
            'user_id': user_id,
            'first_name': first_name,
            'age': age
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'user_id': user_id})
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
