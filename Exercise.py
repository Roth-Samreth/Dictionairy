studentRecord = [
    {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
    {"studentName":"seyha","class":"wep-b","algorithm":80,"html":90},
    {"studentName":"Villa","class":" wep-a","algorithm":96,"html":92},
    {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54},
]
def countA(arr):
    sum = 0
    for i in range(len(studentRecord)):
        if studentRecord[i]["class"]=="wep-a":
            sum += 1
    return sum
wepA = countA(studentRecord)
sum = 0
avg  = 0
for i in range(len(studentRecord)):
    if studentRecord[i]["class"]=="wep-a":
        sum += studentRecord[i]['algorithm']
avg = sum/wepA
print(avg)