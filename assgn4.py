import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_210192.xml'

#while True:
    #address = raw_input('Enter location: ')
    #if len(address) < 1 : break

#url = serviceurl
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum=0
for count in counts:
    sum=sum+int(count.text)
print "sum:",sum
            
