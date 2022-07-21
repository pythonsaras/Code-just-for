import random
n=20
to_be_guessed=int(n*random.random())+1
guess=0
guess_n=0
while guess!=to_be_guessed:
    guess=int(input("Enter number"))
    if guess>0:
        if guess>to_be_guessed:
            print("Number is large")
        elif guess<to_be_guessed:
            print("Number is small")
        guess_n+=1
    else:
        print("You give up!")
        break
else:
    print(f"Congratulation, You win! and you take {guess_n} guess")


