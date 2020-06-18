import urllib.request, urllib.error
import xml.etree.ElementTree as ET

# http://py4e-data.dr-chuck.net/comments_555760.xml
# You are to look through all the <comment> tags and find the <count> values sum the numbers.

url = input('Enter location: ')
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

total = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)

print(total)

''' Cleaner version
import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_555760.xml'
response = urllib.request.urlopen(url)
tree = ET.fromstring(response.read())
total = sum([int(count.text) for count in tree.findall('comments/comment/count')])
print(total)
'''