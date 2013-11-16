#Script to get the urls and ip addresses of any url

import urllib2
from BeautifulSoup import BeautifulSoup
import subprocess
import socket
import whois

url=''
print whois.whois(url)
content=urllib2.urlopen(url).read()
soup=BeautifulSoup(content)

url_tags=soup.findAll('a') #get all links in the webpage

print "There are %d links in the webpage" %len(url_tags)

links=[]

for url in url_tags:
	links.append(url.get('href'))

unique_links=set(links)

print "There are %d unique links in the webpage" %len(unique_links)

linksfile=open('links.txt','w') #create a file to store the unique addresses


for item in unique_links:
	linksfile.write(item)
	linksfile.write('\n')

#Now we run a few basic BASH commands  to obtain the servers 

grep=subprocess.Popen(['grep','http','links.txt'],stdout=subprocess.PIPE,) #look for http in the links file
cut=subprocess.Popen(['cut','-d','/','-f3'],stdin=grep.stdout,stdout=subprocess.PIPE,) #obtain the hostname of the url
grep2=subprocess.Popen(['grep','<url>',],stdin=cut.stdout, stdout=subprocess.PIPE,) #get only the links that contain the url
sort=subprocess.Popen(['sort','-u'],stdin=grep2.stdout,stdout=subprocess.PIPE,) #sort the links 
end_of_pipe=sort.stdout #pass the output of the command

#The above is the equivalent of the BASH command grep 'http' links.txt | cut -d '/' -f3 | grep 'url' | sort -u

ipsdict=dict() #dictionary to store the key,value pairs of urls and their ip addresses

for line in end_of_pipe:
	print line.strip() #print the urls
	ipsdict[line.strip()]=socket.gethostbyname(line.strip())

print ipsdict



