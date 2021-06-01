n=int(input("enter a number"))
i=1
fact=0
while i<=n:
    if n%i==0:
        fact+=1
    i+=1
if fact==2:
    print("prime number")
else:
    print("not a prime number")
