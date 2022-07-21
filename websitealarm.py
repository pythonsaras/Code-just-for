from calendar import timegm
import time 
import webbrowser

set_alarm=input("Sat the website alarm as H:M:S ")

url=input("Enter url here ")

actual_time=time.strftime("%I:%M:%S")
while(actual_time!=set_alarm):
    print("The time is "+actual_time)
    actual_time=time.strftime("%I:%M:%S")
    time.sleep(1)
    if actual_time==set_alarm:
        print("You should see your webpage now :- ")
        webbrowser.open(url)
        

