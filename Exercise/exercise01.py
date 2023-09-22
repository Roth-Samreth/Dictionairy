array =[
    ['A','B','C'],                                                                                              
    ['D','F','C'],
    ['A','A','F'],
    ['V','B','C']
    ]
result = ""
for i in range(len(array)):
    if len(array[i])<3:
        array = "Column Error"
    elif len(array[i])==3:
        array[i][-1]='*'
print(array)