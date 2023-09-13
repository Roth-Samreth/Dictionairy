# Ex1:
# number of array: 3
# > [3, 3]
# > [1, 3, 4]
# > [4, 5, 9, 1]

numarray = int(input())
res = []
for i in range(numarray):
    array = eval(input())
    res.append(array)
print(res)
for j in range(len(res)):
    sum = 0
    for k in range(len(res[j])):
        sum+=res[j][k]
    print(sum)

# output:
# 6
# 8
# 19
# --------------------
# Ex2:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

numarray = int(input())
res = []
for i in range(numarray):
    array = eval(input())
    res.append(array)
    print(res)
# output:
# [2, 3]
# [4, 3, 1]
# -------------------
# Ex3:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

numarray = int(input())
res = []
avg = 0
for i in range(numarray):
    array = eval(input())
    res.append(array)
print(res)

for j in range(len(res)):
    sum = 0
    for k in range(len(res[j])):
        sum+=res[j][k]
    avg = sum/len(res[j])
    print(avg)
# output:
# 2.5
# 2.66666666
# -----------------
# Ex4:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]
numarray = int(input())
res = []
for i in range(numarray):
    array = eval(input())
    res.append(array)
    print(res)
# output:
# [9, 4]
# [1, 9, 16]
# ----------------
# Ex5:
# Find index of number in list (each value is unique)
# Test case 1:
#
# Enter array: [1,2,4,10,9]
# Enter number: 10
# ouput
# 10 at position 3

# Test case 2:

# Enter array: [5,4,10,3]
# Enter number: 5
# ouput
# 5 at position 0

# Test case 3:

# Enter array: [5,4,10,3]
# Enter number: 8
# ouput
# 8 not found in list

arr = eval(input())
num = int(input())
res = str(num)+" is not found."
for i in range(len(arr)):
    if arr[i]==num:
        res = str(num)+" is at position "+str(i)
print(res)
# ----------------
# Ex6:
# Count number in list (each value is unique)
# Test case 1:

# Enter array: [1,2,4,10,9]
# Enter number: 10
# ouput
# number 10 is 1

# Test case 2:

# Enter array: [5,4,5, 5, 5, 10,3]
# Enter number: 5
# ouputr: 
# number 5 is 4

# Test case 3:

# Enter array: [5,4,10,3]
# Enter numbe 8
# ouput
# number 8 is 0

arr = eval(input())
num = int(input())
res = 0
for i in range(len(arr)):
    if arr[i]==num:
        res+=1
print(res)
# --------------

# Ex7:
# Count number 10 in list of array 2D
# Test case 1:

# Enter array: [[1, 2, 4, 5], [14, 16, 10, 11], [10, 9, 10, 10]]

arr = eval(input())
num = int(input())
res = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==num:
            res+=1
print(res)
# ouput
# number 10 is 4

# Test case 2:
# Enter array: [[1, 2, 4, 5], [14, 16, 8, 11], [8, 9, 8, 8]]
# ouput
# number 10 is 0
# -----------------------
# Ex8
# Search students from list of array 2D
students = [
  ['bopha','2024A','kandal'],
  ['romdule','2024C','kompot'],
  ['kaka','2024C','Rathanakiri'],
  ['chompey','2024B','Siem Riep'],
  ['chompa','2024B','Battambang']
]
# #1 - how many students from class A? B? and C?

classA = 0
classB = 0
classC = 0
for i in range(len(students)):
    if students[i][1]=="2024A":
        classA+=1
    elif students[i][1]=="2024B":
        classB+=1
    elif students[i][1]=="2024C":
        classC+=1
print(classA,classB, classC)

# #2 - Where kaka come from?

for i in range(len(students)):
    if students[i][0]=="kaka":
        print(students[i][0]+" is from "+students[i][len(students[i])-1])

# #3 - Which class Chompey study?

for i in range(len(students)):
    if students[i][0]=="chompey":
        print(students[i][0]+" is from class "+students[i][1])
#4 - Replace Chompa province to Prey Veng
for i in range(len(students)):
    if students[i][0]=="chompa":
        students[i][len(students[i])-1]= "preyveng"
print(students)

# Ex9
# From list of array 2D
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
# #1 - How many letter "A" from array 2D (function)

def countA(arr):
  countA = 0
  for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i])):
            if arr[i][j][k]== "a":
                countA +=1
  return countA
print(countA(fruits))

# #2 - How many banana in list (function)

def countBanana(arr):
    countBanana = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "banana":
                countBanana+=1
    return countBanana
print(countBanana(fruits))

#3 - How many mango in list (function)

def countMango(arr):
    countMango= 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "mango":
                countMango+=1
    return countMango
print(countMango(fruits))

# #4 - How many orange in list (function)

def countOrange(arr):
    countOrange= 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "orange":
                countOrange+=1
    return countOrange
print(countOrange(fruits))

# #5 - Replace mango by # sign

def countOrange(arr):
    countOrange= 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "orange":
                countOrange+=1
    return countOrange
print(countOrange(fruits))

# Ex10
# From list of array 2D
numbers = [
  [1, 3, 4, 4],
  [3, 4, 0, 4],
  [5, 6, 9, 0],
  [4, 5, 9, 7]
]
# #1 - How many number 4 from array 2D (function)

def count4(arr):
    count4= 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 4:
                count4+=1
    return count4
print(count4(numbers))

# #2 - Sum each list of array in array 2D (function)

def count4(arr):
    res = []
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[i])):
           sum+=arr[i][j]
        res.append(sum)
    return res
print(count4(numbers))

# output: [12, 11, 20, 25]
# #3 - Sum only number 4 in list 

def count4(arr):
    sum= 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 4:
                sum+=arr[i][j]
    return sum
print(count4(numbers))

# #4 - Replace number 0 with 99 (function)

def count4(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j]= 99
    return arr
print(count4(numbers))

# #5 - where find index of 7 in list 
def index3(arr):
    res = []
    for i in range(len(arr)):
      for j in range(len(arr[i])):
        if arr[i][j] == 7:
          res.append(i)
          res.append(j)
    return res
print(index3(numbers))
# output: [3][3]