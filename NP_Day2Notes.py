a=2
b='CSK'
c='MI'

ipl = ['CSK','MI','RCB','DC']


print(type(ipl))

#indexing
print(ipl[1])

#slicing
print(ipl[2:])

ipl[1]='KKR'



ipl.append('KKR')

# Delhi capitals, Gujarat Titans,
# CSk, Lucknow super giants,KKR
# MI, Punjab kings, Rajasthan Royals
# RCB, Sunrisers Hyderabad
ipl.insert(2,'PW')
ipl.extend([1,2])

ipl_string = 'CSK,MI,PW,RCB,KKR,DC'
print(ipl_string.split(','))

python_list = list('python ')

print(python_list)

ipl_string2 = list('CSK,MI,PK,RCB,SH,DC')
print(ipl_string2)

print(ipl)

ipl.pop(2)

print(ipl)

num = [2,1,3,4]
print(sum(num))
print(min(num))
print(num)
#sort a list

print(num.sort())

print(num)

#to get the index of particular value

print(num.index(1))

#list of list
list_of_list = [[1,2],[3,2],['siv','kumar']]

print(list_of_list)

ipl_new = ipl.copy()

print(ipl_new)


print(1+2.0)
print(type(1+2.0))
print(5/2)
print(5//2)
print(round(2.47))
print(abs(-2.0))
print(pow(2,3))

print('aa'.upper())

a=2.0
print(a.is_integer())


