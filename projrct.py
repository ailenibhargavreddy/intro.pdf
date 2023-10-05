import random
num = random.randint(1,100)
guess = int(input("enterr u rnumber :"))
attempts = 1
while(True):
    if(num>guess):
        guess = int(input("please enter big number"))
        attempts +=1
    elif(num<guess):
        guess = int(input("please enter small number"))
        attempts  +=1
    else:
        print(f"u guessed right one in {attempts} attempts")
        break