

inputN=input()
count=0
temp=int(inputN)
inplace=int(input())
mylist=[1,10,100,1000,10000,100000,1000000,10000000,10000000,100000000,1000000000,10000000000]
# print(mylist[0])


while True:
    rem=temp%10
    temp=temp//10
    if(rem==inplace and temp>0):
        print(f"place value of {inplace} is {mylist[count]}")
        break
    else:
        pass
    count+=1

