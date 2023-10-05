t=int(input(("enter how many times:")))
for tc in range(t):
    a=list(map(int,input().split()))
    if(a[2]>=a[0] and a[2]<a[1]):
        print("yes")
    else:
        print("no")
    