array1 = eval(input("Enter here: "))
array2 =[
 {"teacher-id": 45, "first-name": "Mengheang", "last-name": "Pho"},
 {"teacher-id": 39, "first-name": "ronan", "last-name": "the best"},
 {"teacher-id": 68, "first-name": "him", "last-name": "Hey"},
]

def algorithmId(arr,val,val1):
    res = []
    for i in range(len(arr)):
        if arr[i][val]=="algorithm":
            res.append(arr[i][val1])
    return res
def indexFinder(arr,num,value):
    res = 0
    for i in range(len(arr)):
        if arr[i][value] == num:
            res = i
    return res

teacherId = algorithmId(array1,"subject","teacher-id")
result = "No teacher in algorithm subjects"
if len(teacherId)>0:
    for each in teacherId:
        index = indexFinder(array2,each,"teacher-id")
        result = array2[index]["first-name"]+" "+array2[index]["last-name"]
        print(result)
else:     
    print(result)
