array = eval(input("Enter array"))
result  = []
for n in array:
    if "ee" in n or "EE" in n:
        result.append(n)
print(result)


newArray = []
for i in range(len(array)):
    res = ""
    for j in range(len(array[i])):
        if array[i][j]==array[i][j].upper():
            res+=array[i][j].lower()
        elif array[i][j]==array[i][j].lower():
            res+=array[i][j].upper()
    newArray.append(res)
print(newArray)













