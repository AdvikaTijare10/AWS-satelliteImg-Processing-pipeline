import boto3
import cv2
import numpy as np
import time

s3 = boto3.client('s3', region_name='eu-north-1')
dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('your-table-name')

BUCKET_NAME = "your-bucket-name"

def process_latest_image():

```
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
files = response.get('Contents', [])

input_files = [f for f in files if f['Key'].startswith('input/')]

if not input_files:
    print("No input files found")
    return

latest_file = sorted(input_files, key=lambda x: x['LastModified'], reverse=True)[0]
key = latest_file['Key']

print("Processing:", key)

obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
raw_bytes = obj['Body'].read()

image = cv2.imdecode(np.frombuffer(raw_bytes, np.uint8), cv2.IMREAD_COLOR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

output_file = f"processed_{int(time.time())}.jpg"
output_key = f"processed/{output_file}"

cv2.imwrite(output_file, binary)
s3.upload_file(output_file, BUCKET_NAME, output_key)

table.put_item(
    Item={
        "image_id": output_file,
        "input_key": key,
        "output_key": output_key,
        "timestamp": str(int(time.time()))
    }
)

print("Done ")
```

if name == 'main':
process_latest_image()
