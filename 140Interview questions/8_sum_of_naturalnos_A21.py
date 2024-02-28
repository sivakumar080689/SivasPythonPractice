limit = int(input("Enter the limit :"))

#Initialize the sum

sum =0

#use a for loop to calculate the sum of natural numbers

for i in range(1, limit +1):
    sum += i

# print the sum

print("sum of natural number up to the limit",limit,"is:",sum)