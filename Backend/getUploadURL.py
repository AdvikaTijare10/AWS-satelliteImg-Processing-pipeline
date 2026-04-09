import json
import boto3
import time

s3 = boto3.client('s3', region_name='eu-north-1')

BUCKET = "satellite-images-pipeline-100412"

def lambda_handler(event, context):

    file_name = f"input/upload_{int(time.time())}.jpg"

    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': BUCKET,
            'Key': file_name,
            'ContentType': 'image/jpeg'
        },
        ExpiresIn=300
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "upload_url": url,
            "file_key": file_name
        })
    }
