# web-chk
Python script to check if websites are up, send email if down/up

### Follow the details from the official website for how to send email by SendGrid
https://app.sendgrid.com/guide/integrate/langs/python

### Verify your single sender before sending your first email by SendGrid
https://app.sendgrid.com/settings/sender_auth/senders/new

### expose the key to Linux os so that Python can access vis os module
```
export SENDGRID_API_KEY='SG.F--...Y'
```
### Run at linux terminal every 5 minutes
```
x=1; while true; do echo $x;python3 web-chk.py; (( x++ ));sleep 300; done
```

## Known issues:
* SendGrid doesn't support multiple recepians in the current Python module
* It can't send any email if I make the sendgrid api call as a function in Python3
