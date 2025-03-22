list = [4,5,6,7,0,1,2]
list.sort(reverse = True)
target = 0
for i in list:
    if i == target:
        print(list.index(i))