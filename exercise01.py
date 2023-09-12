# Ex1 - Create new object
# container={}
# res = []
# numObject = int(input())
# for i in range(numObject):
#     id = i+1
#     container["id"]= id
#     name = input()
#     container["name"]= name
#     quantity = int(input())
#     container["quantity"]= quantity
#     price = int(input())
#     container["price"]= price
#     res.append(container)
# print(res)``````````````````````````````````````````````````````````````````````````````````````````
# Object container: id, name, quality, price
# number of object: 3
# > {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100}
# > {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150}
# > {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
# output:
#   [
#     {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 100},
#     {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 150},
#     {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 70}
#   ]
# ---------------------------
# Ex2 - Dictionary or object
# fruit_stock = [
#   {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
#   {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
#   {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}
# ]
#1 - How many fruit in stock

# sum = 0
# for i in range(len(fruit_stock)):
#   sum+=fruit_stock[i]['quality']
# print(sum)

#2 - if 1 mango = 2000៛ how much we can get money after sell all mango

# sum = 0
# sum=fruit_stock[2]['quality']*fruit_stock[2]['price']
# print(sum)

#3 - Following price how much money we can get after sell all fruit from stock

# sum = 0
# for i in range(len(fruit_stock)):
#   sum+=fruit_stock[i]['quality']*fruit_stock[i]['price']
# print(sum)

# ------------------
# Ex3 - Dictionary or object
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 0, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000},
  {'id': 4, 'name': 'Orange', 'quality': 0, 'price': 5000},
  {'id': 5, 'name': 'Apple', 'quality': 5, 'price': 3000},
  {'id': 6, 'name': 'Jackfruit', 'quality': 13, 'price': 6000},
]
#1 - How many fruit have in stock

# sum = 0
# for i in range(len(fruit_stock)):
#   if fruit_stock[i]['quality']>0:
#     sum+=1
# print(sum)

#2 - How many fruit no more in stock

# sum = 0
# for i in range(len(fruit_stock)):
#   if fruit_stock[i]['quality']==0:
#     sum+=1
# print(sum)

#3 - Add 10 fruit to stock which fruti doesn't exist
# 
# iD = len(fruit_stock)+1
# for i in range(10):
#     container={}
#     id = iD+i
#     container["id"]= id
#     name = ""
#     container["name"]= name
#     quantity = 0
#     container["quantity"]= quantity
#     price = 0
#     container["price"]= price
#     fruit_stock.append(container)
# print(fruit_stock)

#4 - Add fruit name to array

# iD = len(fruit_stock)+1
# for i in range(10):
#     container={}
#     id = iD+i
#     container["id"]= id
#     name = input
#     container["name"]= name
#     quantity = 10
#     container["quantity"]= quantity
#     price = 3500
#     container["price"]= price
#     fruit_stock.append(container)
# print(fruit_stock)

#5 - Calculate total of price after add 10 to empty fruit
# sum = 0
# for i in range(len(fruit_stock)):
#   sum+=fruit_stock[i]['quality']*fruit_stock[i]['price']
# print(sum)

# ----------------
# Ex4 - Array
# input: hello world
# output:
# ['hello', 'world']
# ['h','e','l','l','w','o','r','l','d']
# ['olleh','dlrow']
# text = input()
# wordarray = []
# result = ""
# for i in range(len(text)):
#     if text[i] == " " or i == len(text)-1:
#         if i == len(text)-1:
#             result+= text[i]
#         wordarray.append(result)
#         result = ""
#     else:
#         result+=text[i]
# print(wordarray)

# wordarray = []
# for i in range(len(text)):
#   if text[i]!=" ":
#     wordarray.append(text[i])
# print(wordarray)

# reverseArray = []
# for k in range(len(wordarray)):
#   string = ""
#   for j in range(len(wordarray[k])):
#     string+=wordarray[k][-(j+1)]
#   reverseArray.append(string)
# print(reverseArray)

# -----------------
# Ex5 - Array
# Keep only word with at least 1 letter A
# input: banana coconut mango jackfruit
# ouput:
# banana mango jackfruit

# array = ['banana', 'coconut', 'mango', 'jackfruit']
# for i in range(len(array)):
#   if "a" in array[i]:
#     print(array[i],end= " ")


# -----------------
# Ex6 - Array
arr = ['banana','coconut','mango','Jackfruit','orange','apple']
# def countA(string):
#   countA = 0
#   for i in range(len(string)):
#       if string[i]=="a":
#         countA +=1
#   return countA

#1 - Reverse only text contain 1 letter A
# res = []
# for i in range(len(arr)):
#   string = ""
#   if countA(arr[i]) == 1:
#     for j in range(len(arr[i])):
#       string += arr[i][-(j+1)]
#     res.append(string)
#   else:
#     res.append(arr[i])
# print(res)
#2 - Count letter A in text
# res = []
# for i in range(len(arr)):
#   res.append(countA(arr[i]))
# print(res)
# [3, 0, 1, 1, 1, 1]
# #3 - Replace letter A with * in text
# result = []
# for i in range(len(arr)):
#   string = ""
#   for j in range(len(arr[i])):
#     if arr[i][j]== "a":
#         string+= "*"
#     else:
#         string+= arr[i][j]
#   result.append(string)
# print(result)