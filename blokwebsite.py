import time
from datetime import datetime as dt
hotspath=r'*//etc//hosts'
redirect='127.0.0.1'
website=input("Enter your website like www.google.com")
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Sorry")
        with open(hotspath,'+r') as file:
            content=file.read()
            for site in website:
                if site in content:
                    pass
                else:
                    file.write(redirect+""+site+"\n")
    else:
        with open(hotspath,'r+') as file:
            content=file.read()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website):
                    file.write(line)
            file.truncate()
        print("Allow")
    time.sleep(5)


