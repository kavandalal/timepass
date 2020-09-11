import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('enter url :')
link = urllib.request.urlopen(url, context=ctx)
data = link.read()
data = data.decode()
#print(data)
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
#print(lst)
s = 0 
for item in lst:
    x = item.find('count').text
    s+=int(x)
print(s)
    