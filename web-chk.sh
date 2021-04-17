#! /bin/sh
# A script to monitor uptime of websites,
# and notify by email if a website is down.
# Tailored from https://gist.github.com/sweetmandm/49567565fd72187ff76f

SITES="ADD COMMA-SEPARATED WEBSITES HERE"
EMAILS="ADD COMMA-SEPARATED EMAILS HERE"
  for SITE in $(echo $SITES | tr "," " "); do
  if [ ! -z "${SITE}" ]; then
    RESPONSE=$(curl -s --head $SITE)
    
    # Change below to 301 if redirected
    if echo $RESPONSE | grep "200 OK" > /dev/null
    then
      echo "The HTTP Server on ${SITE} is up!"
    else
      MESSAGE="The HTTP server at ${SITE} has failed to respond."
      for EMAIL in $(echo $EMAILS | tr "," " "); do
        SUBJECT="${SITE} (http) Failed"
        echo $MESSAGE | mail -s "$SUBJECT" $EMAIL
        echo $SUBJECT
        echo "Alert sent to $EMAIL"
      done
    fi
  fi
done
