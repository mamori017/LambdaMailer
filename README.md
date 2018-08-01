# LambdaMailer

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9df9ec41024a402ea0e5465267d05530)](https://www.codacy.com/app/mamori017/LambdaMailer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mamori017/LambdaMailer&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/mamori017/lambdamailer/badge)](https://www.codefactor.io/repository/github/mamori017/lambdamailer)
[![BCH compliance](https://bettercodehub.com/edge/badge/mamori017/LambdaMailer?branch=master)](https://bettercodehub.com/)
[![Release](https://img.shields.io/github/release/mamori017/LambdaMailer.svg)](https://github.com/mamori017/LambdaMailer/releases/latest)
[![License](https://img.shields.io/github/license/mamori017/LambdaMailer.svg)](https://github.com/mamori017/LambdaMailer/blob/master/LICENSE)

![20180731120000](https://user-images.githubusercontent.com/7507701/43430028-d2f4d61e-94a1-11e8-99af-4ae9482e1db0.png)

## Overview

AWS Lambda function to send E-mail using SendGrid or Amazon SNS.

## Requirement

- SendGrid API
- Amazon SNS access permission

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

1. Use sample file(./Test/sample.json) and replace each key value.

    |Key |Description |
    |---|---|
    |TYPE |Set "sendgrid" or "sns" |
    |SEND_FROM  |Send from E-mail address |
    |SEND_TO |Send to E-mail address |
    |CONTENT |Body |

1. Upload sample file to S3 bucket.

## Licence

[MIT](https://github.com/mamori017/LambdaMailer/blob/master/LICENSE)

## Author

[mamori017](https://github.com/mamori017)
