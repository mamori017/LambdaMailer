# LambdaMailer

![20180705140608](https://user-images.githubusercontent.com/7507701/42428708-0c2d25dc-8370-11e8-9c8e-a7d8ac189367.png)

## Overview

AWS Lambda function to send emails using SendGrid.

## Requirement

- SendGrid API

## Usage

1. pip install sendgrid.

1. Create new function with this code.

1. Set SendGrid API key to environment valiables.

1. Add S3 trigger.

    |Trigger setting | |
    |---|---|
    |Event source bucket |Any |
    |Event source type  |Create object or put |
    |Prefix |Any |
    |Suffix |Any |

1. Save this function.

1. Use sample file(./sample.json). Replace test file each key value.

1. Upload sample file to S3 bucket.

## Author

[mamori017](https://github.com/mamori017)
