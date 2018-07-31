#coding:utf-8
import boto3
import os

def publish(subject, content):

    ret = False

    try:
        TOPIC_ARN = os.environ['SNS_PUBLISH_ARN']
        client = boto3.client('sns')
        request = {
            'TopicArn': TOPIC_ARN,
            'Message': content,
            'Subject': subject
        }

        response = client.publish(**request)

        if  response['ResponseMetadata']['HTTPStatusCode'] == 200:
            ret_msg =  'succeeded'
            ret = True
        else:
            ret_msg =  'error'
            ret = False

        print('AWS SNS publish ' + ret_msg + '. Status code:' + str(response['ResponseMetadata']['HTTPStatusCode']))

        return ret

    except Exception as e:
        print(e)