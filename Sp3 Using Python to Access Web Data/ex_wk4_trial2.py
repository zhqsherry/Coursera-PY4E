import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup

pos = int(input("Position: "))-1 #For The Position
count = int(input("Times: ")) #For the Times
url = input("Enter URL: ") #For The URL

for i in range(count):  #Desired times the loop should run
    html = urllib.request.urlopen(url).read()  # Taking html from the web address
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a') #Only taking tag from the html file
    tag = tags[pos].get('href',None) #Only taking desired position string value from the tags list & only taking the url address
    url = tag #Redefining the desired positioned url as the new url for running the loop for desired times
    name = tags[pos].contents[0] #Taking only the content from the desired positioned string
    print(name) #Printing the name
