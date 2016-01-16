import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
names = tree.findall('.//name')
print 'Count: ' + str(len(names))
CountSum = 0
for count in counts:
    CountSum += int(count.text)
print 'Sum: ' + str(CountSum)
