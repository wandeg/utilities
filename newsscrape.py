'''
A script to help parse news items ang tag them geographically
I've been working on this for a while. I'll need to add a little more functionality before I can upload it
'''

import urllib2
import folium

from BeautifulSoup import BeautifulSoup

def get_words(url):
    url=url
    html=urllib2.urlopen(url)
    
    soup=BeautifulSoup(html)
    
    kwtag=soup.findAll('meta',{'name':'keywords'})
    tit=soup.find('title')
    header=soup.find('h1')
    
    headlist=[i.strip().lower() for i in header.text.encode('utf-8').split()]
    titlist=[i.strip().lower() for i in tit.text.encode('utf-8').split()]
    kwlist=[i.strip().lower() for i in kwtag[0].attrs[1][1].encode('utf-8').split(',')]
    
    wordlist=headlist+titlist+kwlist
    words=list(set(wordlist))
    
    return words


coords={}

tileset='http://{s}.tile.cloudmade.com/c4b88afd12b34ea39facebea75c281fe/997/256/{z}/{x}/{y}.png'

map1=folium.Map(location=[-1.2667,36.8], zoom_start=12, tiles=tileset, attr='My Data Attribution')

url_list=[]
url='http://127.0.0.1'
while url != '':
    url=raw_input("Enter url:")
    if len(url)>5:
        url_list.append(url)
         
for url in url_list:
    words=get_words(url)
    for item in words:
        if coords.has_key(item):
            map1.simple_marker(coords[item],popup=url)

map1.create_map('map2.html')
