# web-chk
Python/bash script to check if websites are up every 5minutes, send email if down/up.

### Follow the details from the official website for how to send email by SendGrid
https://app.sendgrid.com/guide/integrate/langs/python

### Verify your single sender before sending your first email by SendGrid
https://app.sendgrid.com/settings/sender_auth/senders/new

## Deploy to Linux
### expose the key to Linux os so that Python can access vis os module
```
export SENDGRID_API_KEY='SG.F--...Y'
```
### Run at linux terminal every 5 minutes
```
x=1; while true; do echo $x;python3 web-chk.py; (( x++ ));sleep 300; done
```

## Deploy to GCP Cloud Function
1. Create Function with 2 variables: SENDGRID_API_KEY SENDGRID_EMAIL_ADDRESS
2. copy the code from file gcp-function-web-chk.py
3. Create Scheduler => pub/sub `*/5 * * * *` to trigger the function

## Simple version as bash script
refer to the bash-chk-web.sh file

## Known issues:
* SendGrid doesn't support multiple recipiens in the current Python module
* It can't send any email if I make the sendgrid api call as a function in Python3
