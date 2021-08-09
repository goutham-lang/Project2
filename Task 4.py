n=int(input("Enter the number of terms in  fibonacci series: "))
n1, n2 = 0, 1
count = 0
if n<0:
    print("enter valid number of terms!")
elif n==1:
    print("Fibonacci series upto "+str(n)+"terms is :"+str(n1))
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
