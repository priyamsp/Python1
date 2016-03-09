import urllib
from bs4 import BeautifulSoup
url= raw_input('Enter -')
position = input('Enter Position: ')
count= input('Enter Count: ')
ct = 1
while(ct<=count): 
    html= urllib.urlopen(url).read()
    print(url)
    soup=BeautifulSoup(html,"html.parser")
    tags=soup.find_all('a')
    url=(tags[position-1].get('href'))
    name = tags[position-1].get_text()
    ct=ct+1
print ("Ans",url)
print(name)
