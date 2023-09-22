# find the number that has accured more than one time
array = [9,9,8,8,8,1,3]
result = []
for i in range(len(array)):
    res = array[i]
    if res != array[i]:
        res = ''
    result.append(res)
print(result)