n=int(input("Enter a number:"))
print("\nPrime without recursion")
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
print("\nPrime without recursion")
def prime(n):
    global i
    if i<n//2:
        if n%i==0:
            return 1
        else:
            i=i+1
            return prime(n)
    else:
        return 0
i=2
y=prime(n)
if y==0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
