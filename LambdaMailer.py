#coding:utf-8
import sendgrid_function
import sns_function
import s3_function

def lambda_handler(event, context):
    try:
        # S3 file read
        file_path = s3_function.get_file(event)
        s3_dict = s3_function.make_dict(file_path)

        # SendGrid
        response = sendgrid_function.send_mail(s3_dict['SUBJECT'], s3_dict['SEND_FROM'], s3_dict['SEND_TO'], s3_dict['CONTENT'])

        if  response.status_code == 202:
            print('Using SendGrid API E-Mail send succeeded. Status code:' + str(response.status_code))
        else:
            print('Using SendGrid API E-Mail send error. Status code:' + str(response.status_code))

        # SNS Publish
        response = sns_function.publish(s3_dict['SUBJECT'], s3_dict['CONTENT'])
    
        if  response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('AWS SNS publish succeeded. Status code:' + str(response['ResponseMetadata']['HTTPStatusCode']))
        else:
            print('AWS SNS publish error. Status code:' + str(response['ResponseMetadata']['HTTPStatusCode']))

        return True

    except Exception as e:
        print(e)
        return False
