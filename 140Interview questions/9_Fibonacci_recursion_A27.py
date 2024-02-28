#Display the fibonacci using recursion

#0,1,1,2,3,5,8,13.....

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))

nterms = int(input("Enter the no of terms(greater than zero)"))

if nterms <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence")
    for i in range(nterms):
        print(recur_fibo(i))