#!/usr/bin/python
# this script is working really well
# low app access should be enabled in gmail of sender for this script to work
import smtplib


s = smtplib.SMTP('smtp.gmail.com',587)

sender = "firojvsfacebook@gmail.com"
password = "**************"
receiver = "firoj.is.available@gmail.com"
message = "\nThis is 3rd message sent from python script"


try:
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender,receiver, message)
    print("Message sent")
except Exception as e:
    print("Message sending failed and error is as follows \n", e)


s.quit()


