# factorial using recursion
# 5! = 5 x 4 x 3 x 2 x 1
def rec_fun(n):
    if(n==1):
        return n
    else:
        return n*rec_fun(n-1)

num = int(input("Enter a num : "))

if num<0:
    print("pls enter a positive no")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print(f"factorial of", num, "is", rec_fun(num))