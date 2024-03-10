list = [20,10,30,5,98,43,200]

#intialize first element as small

smallest_num = list[0] # 1.assign 20

for i in list: #1.20 in [20,10,30]
    if i < smallest_num: # 1.loop out
        smallest_num = i
print(smallest_num)
