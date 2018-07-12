#coding:utf-8
import sendgrid_function
import sns_function
import s3_function

def lambda_handler(event, context):

    ret = False

    try:
        # S3 file read
        file_path = s3_function.get_file(event)
        s3_dict = s3_function.make_dict(file_path)

        if s3_dict['TYPE'] == 'sendgrid':
            # SendGrid
            ret  = sendgrid_function.send_mail(s3_dict['SUBJECT'], s3_dict['SEND_FROM'], s3_dict['SEND_TO'], s3_dict['CONTENT'])
        elif s3_dict['TYPE'] == 'sns':
            # SNS Publish
            ret = sns_function.publish(s3_dict['SUBJECT'], s3_dict['CONTENT'])
        else:
            # Type error
            print('S3 object TYPE error.')

        return ret

    except Exception as e:
        print(e)
        return False
