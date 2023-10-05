def sumof(n):
    if(n==1):
        return 1
    else:
        return n + sumof(n-1)
    
a = sumof(3)
print(a)