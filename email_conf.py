"""Set these values as environment variables"""
from os import environ

# Must have 'less secure applications' disabled
# https://www.google.com/settings/security/lesssecureapps
from_email = environ['from_email']
from_email_pass = environ['from_email_pass']

# Comma separated values
to_email_list = environ['to_email_list'].replace(' ', '').split(',')
