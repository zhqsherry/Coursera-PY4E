# Actual data: http://py4e-data.dr-chuck.net/comments_555761.json
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import json
import urllib.request

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

count = 0
sum = 0
url = input("Enter url - ")

data = urllib.request.urlopen(url).read()
print(data)

info = json.loads(data)

for i in info['comments']:
    count = count + 1
    sum = sum + i['count']

print('Sum', sum)
print('count', count)



