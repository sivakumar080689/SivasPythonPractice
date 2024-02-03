#tuple

a=(1,2,3)
#a[0]=5 #tuples are immutable
print(a)

b=("CSK","MI",2)
#b[1]="4"
print(b[1])
print(b)
print("type : ", type(b))

list = ["hi","vik",4]
print(list)

#dictionaries
ipl = [['CSK','Chennai Super Kings'],['MI','Mumbai indians']] #this is List
print(type(ipl))

ipl ={ "CSK" : "Chennai Super Kings",
       "MI" : "Mumbai Indians"}

print(type(ipl))

ipl["CSK"]
ipl["GT"]= "Gujarat Titans"
ipl["CSK"] = "Chennai"
print(ipl)

del ipl["CSK"]
print(ipl)

ipl = {
       "CSK" : {"Name":"Chennai Super Kings","captain":"MSD"},
       "MI"  : {"Name":"Mumbai Indians","captain":"sachin"},
       "RCB" : {"Name":"Royal Challengers Bangalore","captain":"Virat"}
}

print(ipl)


ipl = {
       "CSK" : {"Name":"Chennai Super Kings","captain":["MSD","Jadeja"]},
       "MI"  : {"Name":"Mumbai Indians","captain":"sachin"},
       "RCB" : {"Name":"Royal Challengers Bangalore","captain":"Virat"}
}

print(ipl)

##############

list = [1,2]
tuple = (1,2)
dictionaries = {"key":"value"}

print(dictionaries)


############################
#strings #numbers #boolean
#control flow using if else
# less than 30 -> fail , else pass

marks = -20
if marks <30:
       print("fail")
       print(f"marks are {marks}")
elif marks >=30 and marks < 60:
       print("pass with second division")
elif marks >=60 and marks < 75:
       print("pass with first division")
else:
       print("pass with distinction")
print("this is outside if")

#loops

num_square = []
num = [1,2,3,4,5,6,7]
num_square.append(num[0]**2)
num_square.append(num[1]**2)

print(num)
print(num_square)


#while

num_square =[]
n=3
while n< len(num):
       print(f"it is still less than 5 iteration number {5}")
       num_square.append(pow(num[n],2))
       n=n+1
       print(num_square)


#for loops
num4 =[7,8]
num_square =[]
n=0
for n in num4:
       num_square.append(pow(n,3))
       print(n)
       print(num4)
       print(num_square)
print(num_square)


x = range(6)
for n in x:
       print(n)


num=[1,2,3]
num_square=[]
for n in range(len(num)):
       print(f"it is still less than 5 iteration number {n}")
       num_square.append(pow(num[n], 2))
       print(num_square)


name4 = ["CSK","MI","RCB","hello"]
len_team=[]
for i in name4:
       print(i)
       len_team.append(len(i))
       print(len_team)



