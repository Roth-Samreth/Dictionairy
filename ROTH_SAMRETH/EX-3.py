array = eval(input("Enter array of strings "))

def reverseText(arr):
    result = ""
    for i in range(len(arr)):
        result+=arr[-(i+1)]
    return result

result = []
for i in range(len(array)):
    result.append(reverseText(array[-(i+1)]))
print(result)









