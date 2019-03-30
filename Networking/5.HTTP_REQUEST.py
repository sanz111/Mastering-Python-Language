#!/usr/bin/python3

import http.client

h = http.client.HTTPConnection("www.facebook.com")
h.request("GET", "/")
data = h.getresponse()
print(data.code,"\n -----------")
print(data.headers,"\n----------------")
text = data.readlines()

for t in text:
    print(t.decode('utf-8'))