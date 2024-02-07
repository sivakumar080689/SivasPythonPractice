ipl= {
    "CSK" : "Chennai Super Kings",
    "MI"  : "Mumbai Indians"
}

print(ipl.items())

for team in ipl:
    print(team)
    print(ipl[team])

for team,name in ipl.items():
    print(team)
    print(name)

print("######")
ipllist = ["CSK","MI","RCB"]

for i in ipllist:
    if i == "CSK":
        break
    print(i)

for i in ipllist:
    if i == "CSK":
        continue
    print(i)

ipllist2 = ["CSK","MI","RCB","DC"]
ipl_len = []
for i in ipllist2:
    if len(i) > 2:
        ipl_len.append(len(i))
print(ipl_len)



try:
    print("this is try block")
    a=1/0
    print(a)
except Exception as e:
    print("this is exception block")
    print(e)
else:
    print("this is else block")
finally:
    print("this is finally block")


#working with files

f= open("hello.txt",'r')
for a in f:
    print(a)
f.close()

f = open("test123.txt",'w')
f.write("this is first line in write mode")
f.close()


f = open("test5.txt",'a')
f.write("this is first line in write mode \n")
f.write("this is first line in write mode 1")
f.close()


f = open("test.txt",'w')
f.write("this is first line in write mode")
f.close()