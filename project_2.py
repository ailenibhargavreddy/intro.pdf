import random
num = random.randint(1,100)
num2 = input("enter u r number :")
if(num<int(num2)):
    print("smaller num please")
elif(num>int(num2)):
    print("bigger num please")
else:
    print("u entered correct num")