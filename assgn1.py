import re

#read the file
f=open("regex_sum_210190.txt","r")
read_data=f.read()
#print read_data
num_list= re.findall('[0-9]+',read_data)
count=0
res=0
for i in num_list:
    res=res+int(i) 
    count+=1
    
print count
print res
