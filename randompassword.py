import random 
import string

letter=string.ascii_letters
# num='0123456789'
# spe='!`~@#$%^&*()_-+=}{][|\"\':;?/>.<,'
symbol=letter#+num+spe
yourpassword=input("enter your password")
count=0
for i in yourpassword:
    count+=1
print(yourpassword)    
while True:
    password=''.join(random.sample(symbol,count))
    if password==yourpassword:
        print("your password is match")
        break

