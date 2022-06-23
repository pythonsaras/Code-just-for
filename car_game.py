import msvcrt
import time


high_score=17.18
name="Saras"
while True:
    distance=int(0)
    print("\n-------------------------------------------")
    print("\n\nWelcome to the 100m sprint,tap z and x repidly to move!")
    print('*=10m')
    print(f'\nCurrent record: {high_score} by {name}')
    print("\nPress enter to start")
    input()
    print("Ready...")
    time.sleep(1)
    print('Go!')
    start_time=time.time()
    while distance<10:
        k1=msvcrt.getch().decode('ASCII')
        if k1=='z':
            k2=msvcrt.getch().decode('ASCII')
            if k2=='x':
                distance+=1
                if distance==5:
                    print("* You are halfway there!")
                elif distance%1==0:
                    print("*")
    f_time=time.time()-start_time
    f_time=round(f_time,2)
    print("Congratulations on successfully completing the race!")
    print(f"You took {f_time}'seconds to reach  the finish line")

    if f_time<high_score:
        print('Well done you have new high score ')
        name=input("Please enter your name:- ")
        high_score=f_time
