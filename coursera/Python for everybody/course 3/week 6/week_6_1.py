import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter url :')
link = urllib.request.urlopen(url,context=ctx)
data = link.read().decode()
print('Retriving',url)
info = json.loads(data)

s=0
c=0 
for i in info["comments"]:
    s += i["count"]
    c += 1 
print('count:',c)
print('sum:',s)