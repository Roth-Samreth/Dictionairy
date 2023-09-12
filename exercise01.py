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
# print(res)
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
fruit_stock = [
  {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
  {'id': 2, 'name': 'Banana', 'quality': 10, 'price': 2500},
  {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000}
]
#1 - How many fruit in stock
#2 - if 1 mango = 2000៛ how much we can get money after sell all mango
#3 - Following price how much money we can get after sell all fruit from stock
# ------------------
# Ex3 - Dictionary or object
# fruit_stock = [
#   {'id': 1, 'name': 'Coconut', 'quality': 3, 'price': 4000},
#   {'id': 2, 'name': 'Banana', 'quality': 0, 'price': 2500},
#   {'id': 3, 'name': 'Mango', 'quality': 23, 'price': 2000},
#   {'id': 4, 'name': 'Orange', 'quality': 0, 'price': 5000},
#   {'id': 5, 'name': 'Apple', 'quality': 5, 'price': 3000},
#   {'id': 6, 'name': 'Jackfruit', 'quality': 13, 'price': 6000},
# ]
#1 - How many fruit have in stock
#2 - How many fruit no more in stock
#3 - Add 10 fruit to stock which fruti doesn't exist
#4 - Add fruit name to array
#5 - Calculate total of price after add 10 to empty fruit
# ----------------
# Ex4 - Array
# input: hello world
# output:
# ['hello', 'world']
# ['h','e','l','l','w','o','r','l','d']
# ['olleh','dlrow']
# -----------------
# Ex5 - Array
# Keep only word with at least 1 letter A
# input: banana coconut mango jackfruit
# ouput:
# banana mango jackfruit
# -----------------
# Ex6 - Array
# arr = ['banana','coconut','mango','Jackfruit','orange','apple']
#1 - Reverse only text contain 1 letter A
#2 - Count letter A in text
# [3, 0, 1, 1, 1, 1]
# #3 - Replace letter A with * in text
# ---------------