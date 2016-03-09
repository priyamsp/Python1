import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
url = raw_input('Enter address: ')
#if len(url) < 1 : break
#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
input = uh.read()
print input
info = json.loads(input)
#print info["not"]
sum=0
cnt=0
for item in info["comments"]:
    #print'Name', item["name"]
    #print 'Id', item["count"]
    sum=sum+item["count"]
    cnt=cnt+1
print 'Count:',cnt
print 'sum:',sum

    
    
