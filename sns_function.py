#coding:utf-8
import boto3
import os

def publish(subject, content):
    try:
        TOPIC_ARN = os.environ['SNS_PUBLISH_ARN']
        client = boto3.client('sns')
        request = {
            'TopicArn': TOPIC_ARN,
            'Message': content,
            'Subject': subject
        }

        response = client.publish(**request)

        return response

    except Exception as e:
        print(e)