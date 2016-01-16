# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter url- ')
linkPosition = raw_input('Enter link position - ')
cycles = raw_input('Enter cycles - ')

for i in range(int(cycles)):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    links = []
    for tag in tags:
        links.append(tag.get('href', None))
    print links[int(linkPosition)-1]
    url = links[int(linkPosition)-1]
