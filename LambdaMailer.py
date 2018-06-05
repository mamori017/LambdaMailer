#coding:utf-8

import sendgrid
import os
from sendgrid.helpers.mail import *

def lambda_handler(event, context):
 
    sg = sendgrid.SendGridAPIClient(apikey=os.environ['SENDGRID_API_KEY'])

    from_email = Email(os.environ['FROM_EMAIL'])
    to_email = Email(event['TO_EMAIL'])
    subject = event['SUBJECT']
    content = Content("text/plain", event['CONTENT'])
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)

    if response.status_code == 202:
        return 'success status:' + str(response.status_code)
    else:
        return 'error status:' + str(response.status_code)
