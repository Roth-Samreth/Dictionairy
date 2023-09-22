array = [
    ['B','A','N','A','N','A'],
    ['C','O','C','O','N','U','T']
]
result = []
for i in range(len(array)):
    string = ""
    for j in range(len(array[i])):
        string += array[i][j]
    result.append(string)
print(result)