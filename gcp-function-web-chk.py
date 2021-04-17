import urllib
import socket
import os
import sendgrid
from sendgrid.helpers.mail import *

def dummy_entry_point(data, context):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Dummy_Entry_point!'    
    """
    return f'Dummy_Entry_point' 

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


# email_sender='yourname@gmail.com'    
urls=["http://www.celpip.ca","https://www.celpip.ca"]
#urls=["http://google.fr","https://google.fr"]

Notify=False
for url in urls:
    #print('checking:',url
    resp=check_url(url)
    print(' ',resp)
    if resp[0]==True:
        Notify=True

if Notify== True:
    # print('Email sent')
    api_key=os.environ.get('SENDGRID_API_KEY')
    print('api_key:',api_key[:5],'...',api_key[-5:])
    email_sender=os.environ.get('SENDGRID_EMAIL_ADDRESS')
    print('email_address',email_sender)
    sg = sendgrid.SendGridAPIClient(api_key)
    from_email = Email(email_sender) #Verify your email via Sendgrid before sending your first email
    to_email = To(email_sender)
    #doesn't support multiple recepians
    subject = "URGENT: CELPIP Website is up"
    content = Content("text/plain", "Verified by Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

print(' ')
