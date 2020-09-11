from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum= 0 
for tag in tags:
    print(tag.contents[1])
    sum += int(tag.contents[0])
print(sum)


'''word= list()
z = list()
sum = 0 
tags = soup('td')
for line in tags:
    word = str(line).split()
    for x in word:
        y= re.findall("[0-9]+",x)
        z = z+y
print(z)
for s in z:
    sum += int(s)
print(sum)'''
