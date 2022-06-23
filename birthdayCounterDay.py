import datetime
current_date=datetime.date.today().strftime('%Y-%m-%d')
current_date=current_date.split('-')

b_date=input('Enter birthday in yyyy-mm-dd format: ')

b_date=b_date.split('-')
current_date[0]=int(current_date[0])
current_date[1]=int(current_date[1])
current_date[2]=int(current_date[2])
b_date[0]=int(b_date[0])
b_date[1]=int(b_date[1])
b_date[2]=int(b_date[2])

if current_date[0]<=b_date[0]:
    pass
elif current_date[0]>=b_date[0]:
    if current_date[1]<b_date[1]:
        n_year=current_date[0]-1
        n_month=current_date[1]+12
        if current_date[2]<b_date[2]:
            n_month=n_month-1
            n_date=current_date[2]+30
            r_date=n_date-b_date[2]
            r_month=n_month-b_date[1]
            r_year=n_year-b_date[0]
        else:
            r_date=current_date[2]-b_date[2]
            r_month=n_month-b_date[1]
            r_year=n_year-b_date[0]
            
    else:
        r_date=current_date[2]-b_date[2]
        r_month=current_date[1]-b_date[1]
        r_year=current_date[0]-b_date[0]
    print(f"Age is {r_year} year {r_month} month {r_date}days")
# if current_date[1]==b_date[1] and current_date[2]==b_date[2]:
#     age=int(current_date[0])-int(b_date[0])
#     ordinal_suffix={1:'st',2:'nd',3:'rd',
#     11:'th'}.get(age%10 if not 10<age <=13 else age %14, 'th')
#     print(f"It's {name}'s {age}{ordinal_suffix} Birthday")
#     print("Sorry, today is not birthday")


