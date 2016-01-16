import json
import urllib

url = raw_input("enter location: ")
print "Retrieving", url
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(data)
print 'Retrieved', len(data), 'characters'

count = 0
for comment in info["comments"]:
    count += 1
print 'Retrieved', str(count), 'names'

count2 = 0
for comment in info["comments"]:
    count2 += int(comment['count'])
print 'Retrieved', count2, 'sum total'
