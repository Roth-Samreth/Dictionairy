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
"score": 99},
{"name": "Kunthy",
"score": 100},
 {"name": "Sreymom",
"score": 95}
]
def findMax(dic):
    maxScore = scoreList[0]['score']
    i = 0
    while i < len(scoreList):
        if maxScore<scoreList[i]['score']:
            maxScore= scoreList[i]['score']
        res = maxScore
        i+=1
    return res

res = ""
res1 = ""
i = 0
max =  True
maxScore = findMax(scoreList)
while i < len(scoreList):
    if scoreList[i]['score'] == maxScore:
        res = scoreList[i]['name']+ " is the best student with the score of "+str(maxScore)
    elif scoreList[i]['score']>75 and scoreList[i]['score'] <maxScore:
        res1 = "All student have score above 75"
    else:
        res1 = " "
    i+=1
print(res)
print(res1)


# ini_dictionary1 = {"2021A": 20, "2021B": 30, "2021C": 15 }
# ini_dictionary2 = {"2021A": 15, "2021C": 10, "2021D": 99 }
# final_dictionary = {}
# for key in ini_dictionary1:
# 	final_dictionary[key] = ini_dictionary1[key] + ini_dictionary2.get(key, 0)
# for key in ini_dictionary2:
# 	if key not in final_dictionary:
# 		final_dictionary[key] = ini_dictionary2[key]

# print("final dictionary", str(final_dictionary))
