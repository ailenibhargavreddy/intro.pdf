import random
number = random.randint(1,100)
attempt = 1
guess = int(input("enter u r number : "))
while(True):
    if(number>guess):
        guess = int(input("please enter ig no "))
        attempt += 1
    elif(number <guess):
       guess = int(input("please enter small no"))
       attempt+=1
    else:
        print(f"u guessed corresct no in {attempt}attempts")
        break  