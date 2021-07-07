import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from decouple import config


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'mufassaproductions@gmail.com'
# email['to'] = 'mustafizur.prodhan2@gmail.com'
email['bcc'] = 'mustafizur.prodhan@gmail.com', \
                    'mustafizur.prodhan2@gmail.com'
email['subject'] = 'Test'

email.set_content('This is a test of your TV! We control the vertical, the horizontal.')
email.set_content(html.substitute({'name': 'Chobi'}), 'html')


with smtplib.SMTP(host=config('host'), port=config('port')) as smtp:
    smtp.ehlo()
    smtp.starttls()
    LOGIN = config('LOGIN')
    PASSWORD = config('PASSWORD')
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(email)
    print('sent')