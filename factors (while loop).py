n=int(input("enter a number"))
i=1
iterations=0
while i<=n//2:
    iterations=iterations+1
    if n%i==0:
        print(i)
    i=i+1
print(n)
print("Total number of iterations%d" %iterations)
