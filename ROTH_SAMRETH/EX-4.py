
array = eval(input("Enter: "))
count = 0
dic = {}
names = []
for i in range(len(array)):
    if array[i]["score"]<50 and array[i]["subject"]== "Algorithm":
        count+=1
        names.append(array[i]["name"])
dic["number"]= count
dic["student"] = names
print(dic)



















