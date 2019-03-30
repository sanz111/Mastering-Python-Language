#!/usr/bin/python3

import poplib, imaplib, getpass

sender = "firojvsfacebook@gmail.com"
password = "mummy14343ver"

p = poplib.POP3("pop.gmail.com", 110)
# p = poplib.POP3_SSL("172.30.42.126", 995)
print("Trying to log in")
print(p.getwelcome())
p.user(sender)
p.pass_(password)
print ("getting list of emails:")
print(p.list())
p.quit()

i = imaplib.IMAP4("imap.gmail.com", 143)
# i.login(getpass.getuser(), getpass.getpass_())
i.login(sender,password)
print("logged in successfully")
i.select()
t, l = i.list()
print("Response code: ", t)
print(l)

t, ids = i.search(None, "ALL")
print("Response code: ", t)
print(ids)
t, msg = i.fetch('5', "(UID BODY[TEXT])")
#  store messages on the server
#  i.store()
print(msg)
i.close()
i.logout()


