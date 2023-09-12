# # dictionairy = {
# #     'mango': 7,
# #     'orange': 3,
# #     'banana' : 1
# # }
# # sum = 0
# # for key in dictionairy:
# #     sum+= dictionairy[key]
# print(sum)


# fruit =[
#     {'name': 'banana','quantity':16},
#     {'name': 'orange', 'quantity':0},
#      {'name': 'Pearl', 'quantity':1}
# ]
# sum = 0
# for i in range(len(fruit)):
#     sum+=fruit[i]['quantity']
# print(sum)

# fruit =[
#     {'name': 'banana','quantity':16,'price': 10},
#     {'name': 'orange', 'quantity':0,'price': 10},
#      {'name': 'Pearl', 'quantity':1,'price': 3}
# ]
# for i in range(len(fruit)):
#     if fruit[i]['quantity']>0:
#         print(fruit[i]['name'])

# sum = 0
# for i in range(len(fruit)):
#     sum+=fruit[i]['quantity']*fruit[i]['price']
# print(sum)

array = [[0,0,0],
        [0,1,0],
        [0,0,0]]
# res = []
# found = True
# res.append(len(array))
# res.append(len(array[0]))
# print(res)


# res = []
# for i in range(len(array)):
#     for j in range(len(array[i])):
#         if array[i][j]==1:
#             res.append(i)
#             res.append(j)
# print(res)

# for i in range(len(array)):
#     for j in range(len(array[i])):
#         if array[i][j]==1:
#             array[i][j]=0
#         elif array[i][j]==0:
#             array[i][j]=1
# print(array)
