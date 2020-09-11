'''from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
c = int(input('Enter count: '))
p = int(input('Enter position: '))-1
links = list()

#print(type(url))

#for i in range(c):
print(' retriving ' , url)
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
print(type(tags))
print(type(tag))
tag = tags.get('href',None)
    
#print(tag)
for tag in tags: 
    #print(tag.get('href').split())
    links += tag.get('href',None).split()
url = links[p]
#print(type(url))
print(links)
    #print(links[int(p)-1])
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
tags_lst = []

for x in range(count):
    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    tags_lst.append(needed_tag)
    url = str(needed_tag)
    print(url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
val = url.find('by_')
last = re.findall('^known_by_(.+)$.html',url)
print('The last name is :',url[39:-5])