# 1 find price
# fruit = [{
# "name": "banana",
# "price": 1000,
# "quantity": 2,
# },
# {"name": "mango",
# "price": 2000,
# "quantity": 1,}
# ]
# total = 0
# for i in range(len(fruit)):
#     total += fruit[i]['price']*fruit[i]['quantity']
# print(total)

# 2 count fruit and meat

# goods = [
# {'fruit': 'banana', 'qty': 10, 'price': 100},
# {'fruit': 'coconut', 'qty': 5, 'price': 10},
# {'fruit': 'mango', 'qty': 12, 'price': 30},
# {'meat': 'bird', 'qty': 1, 'price': 60},
# {'meat': 'fish', 'qty': 3, 'price': 30},
# ]
# fruit = 0
# meat  = 0
# for each in goods:
#     for key in each:
#         if key == "fruit":
#             fruit+=1
#         elif key == "meat":
#             meat+=1
# print("we have fruit " + str(fruit)+ "\n"+ "we have meat "+str(meat))

#
scoreList = [
 {"name": "Bunthoeun",
"score": 76},
{"name": "Kunthy",
"score": 80},
 {"name": "Sreymom",
"score": 95}
]
res = ""
res1 = ""
above75 = False
i = 0
max =  True
maxScore = scoreList[0]['score']
while i < len(scoreList):
    if maxScore<scoreList[i]['score']:
        maxScore= scoreList[i]['score']
        res = scoreList[i]['name']+ " is the best student with the score of "+str(maxScore)
    elif scoreList[i]['score']>75:
        res1 = "All student have score above 75"
        above75 = True
    else:
        res1 = "Not all Student have score above 75"
    i+=1
print(res)
print(res1)