"""Set these values as environment variables"""
from os import environ, path
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Must have 'less secure applications' disabled
# https://www.google.com/settings/security/lesssecureapps
from_email = environ['from_email']
from_email_pass = environ['from_email_pass']

# Comma separated values
to_email_list = environ['to_email_list'].replace(' ', '').split(',')

# Jinja template engine setup
env = Environment(
    loader=FileSystemLoader(path.join(path.dirname(path.abspath(__file__)), 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)

def get_template(template_name):
    return env.get_template(template_name)
