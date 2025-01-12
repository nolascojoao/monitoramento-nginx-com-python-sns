import time
import requests
import json
import boto3

def check_nginx():
    try:
        response = requests.get("http://localhost", timeout=5)
        if response.status_code == 200:
            return "UP"
    except:
        return "DOWN"
    return "DOWN"

def send_sns_alert(status):
    sns_client = boto3.client('sns', region_name='us-east-1')
    topic_arn = 'ARN_DO_TÓPICO_SNS'
    message = {
        "status": status,
        "server": "EC2 Nginx Server"
    }
    sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message),
        Subject="Nginx Server Status"
    )

if __name__ == "__main__":
    last_status = check_nginx()

    send_sns_alert(last_status)

    while True:
        status = check_nginx()

        if status != last_status:
            send_sns_alert(status)
            last_status = status

        time.sleep(60)
