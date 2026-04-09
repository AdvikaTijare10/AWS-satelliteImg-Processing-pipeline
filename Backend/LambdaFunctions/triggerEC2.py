import json
import boto3
import time

ec2 = boto3.client('ec2')
ssm = boto3.client('ssm')

INSTANCE_ID = "your-instance-id"

def lambda_handler(event, context):

    print("Triggered ")

    ec2.start_instances(InstanceIds=[INSTANCE_ID])

    print("Trying to send command...")

    for i in range(6):  # try for ~30 sec
        try:
            response = ssm.send_command(
                InstanceIds=[INSTANCE_ID],
                DocumentName="AWS-RunShellScript",
                Parameters={
                    "commands": [
                        "sudo -u ec2-user -i bash -c 'cd /home/ec2-user && python3 process_image.py'"
                         ,"sudo shutdown now"
                    ]
                }
            )
            print("Command sent ")
            return {"status": "done"}

        except Exception as e:
            print("Retrying... attempt", i+1)
            time.sleep(5)

    print("Failed after retries ")
    return {"status": "failed"}
