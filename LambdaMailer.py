#coding:utf-8

import sendgrid
import os
from sendgrid.helpers.mail import *
import urllib.parse
import boto3
from datetime import datetime
import random
import subprocess
import json
from collections import OrderedDict

def send_mail(subject, send_from, send_to, content):
    try:
        sg = sendgrid.SendGridAPIClient(apikey = os.environ['SENDGRID_API_KEY'])
        mail = Mail(Email(send_from), subject, Email(send_to), Content("text/plain", content))
        response = sg.client.mail.send.post(request_body=mail.get())
        
        return response

    except Exception as e:
        print(e)

def get_file(event):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        file_path = '/tmp/' + '_' + datetime.now().strftime('%Y%m%d%H%M%S')

        s3 = boto3.resource('s3')

        bucket = s3.Bucket(bucket)
        bucket.download_file(key, file_path)
        
        print('Target:' + file_path + key)

        return file_path

    except Exception as e:
        print(e)

def make_dict(file_path):
    try:
        read_file = open(file_path)
        read_data = read_file.read()
        read_file.close()
        ret_dict = json.loads(read_data)
        
        return ret_dict

    except Exception as e:
        print(e)

def lambda_handler(event, context):
    try:
        file_path = get_file(event)
        s3_dict = make_dict(file_path)
        response = send_mail(s3_dict['SUBJECT'], s3_dict['SEND_FROM'], s3_dict['SEND_TO'], s3_dict['CONTENT'])

        if  response.status_code == 202:
            print('E-Mail send succeeded. Status code:' + str(response.status_code))
        else:
            print('E-Mail send error. Status code:' + str(response.status_code))

        return response.status_code
    
    except Exception as e:
        print(e)
