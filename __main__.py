#! /usr/bin/env python3
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import email_conf as conf

if __name__ == "__main__":
    to_email_list = conf.to_email_list

    message = MIMEMultipart('alternative')
    message['subject'] = 'My custom subject'
    message['From'] = conf.from_email
    message['To'] = ','.join(to_email_list)

    template = conf.get_template('notification_email.html')
    html_text = template.render(message='Your message goes here')

    html_body = MIMEText(html_text, 'html')
    message.attach(html_body)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(conf.from_email, conf.from_email_pass)

    server.sendmail(conf.from_email, to_email_list, message.as_string())
    server.quit()
