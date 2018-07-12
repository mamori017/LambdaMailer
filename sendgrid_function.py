#coding:utf-8
import sendgrid
import os
from sendgrid.helpers.mail import *

def send_mail(subject, send_from, send_to, content):

    ret = False

    try:
        sg = sendgrid.SendGridAPIClient(apikey = os.environ['SENDGRID_API_KEY'])
        mail = Mail(Email(send_from), subject, Email(send_to), Content("text/plain", content))
        response = sg.client.mail.send.post(request_body=mail.get())

        if  response.status_code == 202:
            ret_msg =  'succeeded'
            ret = True
        else:
            ret_msg =  'error'
            ret = False

        print('Using SendGrid API E-Mail send ' + ret_msg + '. Status code:' + str(response.status_code))
        
        return ret

    except Exception as e:
        print(e)
