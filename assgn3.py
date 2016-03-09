import urllib
import re
from bs4 import BeautifulSoup
url= raw_input('Enter -')
html= urllib.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")
data=(soup.get_text())
numlist=re.findall("[0-9]+",data)
sum=0
for num in numlist:
    sum =sum+int(num)

print ("sum",sum)    
