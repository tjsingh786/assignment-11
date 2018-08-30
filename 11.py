#Q.1
import re
email=input('Enter Email-ID')
a=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',email)
if a:
    print('valid id')
else:
    print('not a valid id')
  


#Q.2
import re
x=input('Enter Indian Phone number:')

match=re.fullmatch('(\+91-)[6-9][0-9]{9}',x)
if a:
    print('valid')
else:
    print('invalid')
  
