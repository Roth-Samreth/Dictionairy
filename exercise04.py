# Ex1 - Array
# #Counter letter
# input1 = ['banana','coconut','mango']
# input2 = ['a','o']
# output:
# {'a': 4, 'o': 3}
# def countLetter(arr,char):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]==char:
#                 count+=1
#     return count
# dic = {}
# for each in input2:
#     dic[each]=countLetter(input1,each)
# print(dic)

# --------------
# Ex2 - Array
# # Find index
# input1 = [3, 3, 4, 5, 6, 6]
# input2 = [3, 4, 6]
# ouput: {3: "01", 4: "2", 6:"45"}
# def countLetter(arr,char):
#     count = ""
#     for i in range(len(arr)):
#         if arr[i]==char:
#             count+=str(i)
#     return count
# dic = {}
# for each in input2:
#     dic[each]=countLetter(input1,each)
# print(dic)
# ------------
# Ex3 - Array
# #Find index
# input1= [3, 3, 4, 5, 6, 6]
# input2= [3, 4, 6]
# ouput: {3: [0, 1], 4: [2], 6:[4, 5]}
# def countLetter(arr,char):
#     count = []
#     for i in range(len(arr)):
#         if arr[i]==char:
#             count.append(i)
#     return count
# dic = {}
# for each in input2:
#     dic[each]=countLetter(input1,each)
# print(dic)

# -----------
# Ex4 - Array
# #Get value by index
# input1 = ['banana','coconut','mango']
# input2 = [0, 2]
# output:
# {0: 'banana', 2: 'mango'}
# dic = {}
# for each in input2:
#     dic[each]=input1[each]
# print(dic)
# --------------
# Ex5 - Array
# #Reverse text by index

# input1 = ['banana','coconut','mango']
# input2 = [0, 2]
# def reverse(arr):
#     res = ""
#     for i in range(len(arr)):
#         res+=arr[-(i+1)]
#     return res
# for i in range(len(input1)):
#     if i in input2:
#         input1[i] = reverse(input1[i])
# print(input1)

# output:
# ['ananab','coconut','ognam']
# ------------
# Ex6 - object

# input1 = ['banana','coconut','mango']
# input2 = [0,2]
# def objectConvert(arr):
#     obj = {}
#     for i in range(len(arr)):
#         obj[i] = arr[i]
#     return obj
# res = []
# for each in input2:
#     res.append(objectConvert(input1[each]))
# print(res)

# [
#   {0:'b',1:'a', 2:'n', 3: 'a', 4: 'n',5:'a'},
#   {0:'m',1:'a', 2:'n', 3: 'g', 4: 'o'},
# ]
# -----------
# Ex7 - Array 2D
# input = [3 ,4, 5, 1]
# ouput: 
# [
#   [1, 2, 3],
#   [1, 2, 3, 4],
#   [1, 2, 3, 4, 5],
#   [1]
# ]
# def printer(arr):
#     res = []
#     for i in range(arr):
#         res.append(i+1)
#     return res
# result =  []
# for each in input:
#     result.append(printer(each))
# print(result)

# -----------
# Ex8 - Object
# #Reverse Object

# def reverse(arr):
#     res = ""
#     for i in range(len(arr)):
#         res+=arr[-(i+1)]
#     return res
# input = {1: 'banana', 2: 'mango', 3: 'coconut'}
# for i in range(len(input)):
#     input[i+1] = reverse(input[i+1])
# print(input)

# output: {1: 'ananab', 2: 'ognam', 3: 'tunococ'}
# ----------
# Ex9 - Array
# #Replace character by something
# input1 = ['banana','coconut','mango']
# input2 = ['a', '*']

# def replacer(arr,string,replace):
#     word = ""
#     for i in range(len(arr)):
#         if arr[i]== string:
#             word += replace
#         else:
#             word+=arr[i]
#     return word
# for i in range(len(input1)):
#     input1[i] = replacer(input1[i],input2[0],input2[1])
# print(input1)

# output:
# ['b*n*n*','coconut','m*ngo']