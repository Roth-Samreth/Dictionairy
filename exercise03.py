# Ex1 - Array
# # String to array
# Input: Hello
# Output: ['H','e','l','l','o']

# text = input("Enter the text")
# res  = []
# for i in range(len(text)):
#     res.append(text[i])
# print(res)

# ------------------
# Ex2 - Array
# # String to array seperate by space
# Input: aba bank in Cambodia
# output: ['aba', 'bank','in','Cambodia']

# text = "aba bank in Cambodia"
# res = []
# word = ""
# for i in range(len(text)):
#     if text[i]==" " or i==len(text)-1:
#         if i ==len(text)-1:
#             word+=text[i]
#         res.append(word)
#         word = ""
#     else:
#         word+=text[i]
# print(res)
            


# ------------------
# Ex3 - Array
# # Get only text contains letter A
# Input: ['banana','coconut','mango']
# output: ['banana','mango']

# array = ['banana','coconut','mango']
# res = []
# for i in range(len(array)):
#   if "a" in array[i]:
#     res.append(array[i])
# print(res)

# ------------------
# Ex4 - Array
# # Reverse array and reverse text in array
# Input: ['banana','coconut']
# output: 
# ['coconut','banana']
# ['ananab','tunococ']

# arr = ['coconut','banana']
# res = []
# for i in range(len(arr)):
#     word = ""
#     for j in range(len(arr[i])):
#         word+=arr[i][-(j+1)]
#     res.append(word)
# print(arr)
# print(res)

# ------------------
# Ex5 - Array
# #Count number
# Input1: [2, 2, 3, 5, 2, 3, 2, 5, 8]
# Input2: [2, 3]
# Output: [ { 2: 4} , {3: 2} ]

# num = [2, 2, 3, 5, 2, 3, 2, 5, 8]
# res = []
# count2 = 0
# count3 = 0
# for i in range(len(num)):
#     if num[i] == 2:
#         count2+=1
#     elif num[i]==3:
#         count3+=1
# res.append(count2)
# res.append(count3)
# print(res)
# new = []
# for j in range(len(res)):
#     dic = {}
#     dic[2+j]=res[j]
#     new.append(dic)
# print(new)


# ------------------
# Ex6 - Array
# # Array to object
# input: ['banana','coconut', 'mango', 'orange']
# output: 
# text = ['banana','coconut', 'mango', 'orange']
# dic = {}
# for i in range(len(text)):
#     dic[i]=text[i]
# print(dic)
# [
#   {0: 'banana',1: 'coconut',2: 'mango',3: 'orange'}
# ]
# --------------
# Ex7 - Array
# # Array to object - counting character
# input: ['banana','coconut', 'mango', 'orange']
# output:
#  
# text = ['banana','coconut', 'mango', 'orange']
# dic = {}
# for i in range(len(text)):
#     dic[text[i]]= len(text[i])
# print(dic)

# [
#   {0: 'banana',1: 'coconut',2: 'mango',3: 'orange'}
# ]
# [
#   {'banana':6,'coconut':7,'mango': 5,'orange': 6}
# ]
# --------------
# Ex8 - Dictionary or object

fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quatity': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quatity': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quatity': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quatity': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quatity': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quatity': 13, 'price': 6000},
]

# #1 - How many fruit have price > 3000
# {
#   'numberOfruit': 3,
#   'names': ['Coconut','Orange', 'Jackfruit']
# }
# --------------------
# #2 - How many fruit have price < 5000
# [
#   {'name': 'Coconut'},
#   {'name': 'Banana'},
#   {'name': 'Mango'},
#   {'name': 'Apple'}
# ]
# -------------------
# #3 - Which fruit doens't have in stock
# [
#   {'name': 'Banana', 'quatity': 0},
#   {'name': 'Orange', 'quatity': 0}
# ]