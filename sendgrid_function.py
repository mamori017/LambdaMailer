#coding:utf-8
import sendgrid
import os
from sendgrid.helpers.mail import *

def send_mail(subject, send_from, send_to, content):
    try:
        sg = sendgrid.SendGridAPIClient(apikey = os.environ['SENDGRID_API_KEY'])
        mail = Mail(Email(send_from), subject, Email(send_to), Content("text/plain", content))
        response = sg.client.mail.send.post(request_body=mail.get())
        
        return response

    except Exception as e:
        print(e)
