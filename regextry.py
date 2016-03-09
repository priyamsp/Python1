import re

data= "<p>Please click <a href='http://www.dr-chuck.com'>here</a></p>"
#print read_data
num_list= re.findall("'(.+)'",data)
print num_list
##print res
