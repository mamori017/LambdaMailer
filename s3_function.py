#coding:utf-8
import boto3
import urllib.parse
from datetime import datetime
import random
import json

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
