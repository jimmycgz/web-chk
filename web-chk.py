import urllib
import socket
import sendgrid
import os
from sendgrid.helpers.mail import *


def check_url( url, timeout=2 ):
    response='False'
    try:
        response=urllib.request.urlopen(url,timeout=timeout).getcode()
        # print(response)
        if response == 200 or response == 301:
           return True,response,url

    except socket.timeout as e:
        return False,e,url

    #except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')
    except urllib.error.HTTPError as e:
        return False,e,url

    except urllib.error.URLError as e:
        return False,e,url


def send_email_failed():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(email_sender)  # Change to your verified sender
    to_email = To(email_sender)  # Change to your recipient
    subject = "Website is up"
    content = Content("text/plain", "Verified by Python")
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

def send_email_work_cmd():
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python

    message = Mail(
        from_email='yourname@gmail.com',
        to_emails='yourname@gmail.com',
        subject='Website is up',
        html_content='<strong>Verified by Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def send_email():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(email_sender)
    to_email = To(email_sender)
    subject = "Website is up"
    content = Content("text/plain", "Verified by Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

email_sender='yourname@gmail.com'    
urls=["http://google.fr","https://google.fr"]

Notify=False
for url in urls:
    #print('checking:',url
    resp=check_url(url)
    print(' ',resp)
    if resp[0]==True:
        Notify=True

if Notify== True:
    # print('Email sent')
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(email_sender) #Verify your email via Sendgrid before sending your first email
    to_email = To(email_sender)
    #doesn't support multiple recipients
    subject = "TEST Website is up"
    content = Content("text/plain", "Verified by Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

print(' ')
