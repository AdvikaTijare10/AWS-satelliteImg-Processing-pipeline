import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('ProcessedImagesData')

def lambda_handler(event, context):

    response = table.scan()
    items = response.get('Items', [])
    items.sort(key=lambda x: int(x['timestamp']))
    print(items)
    return {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps(items)
}
