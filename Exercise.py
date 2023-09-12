studentRecord = [
    {"studentName":"Seyla","class":"wep-a","algorithm":98,"html":90},
    {"studentName":"seyha","class":"wep-b","algorithm":80,"html":90},
    {"studentName":"Villa","class":" wep-a","algorithm":96,"html":92},
    {"studentName":"mengheang","class":"wep-a","algorithm":66,"html":54},
]
sum = 0
avg  = 0
res = []
for i in range(len(studentRecord)):
    sum = 0
    if studentRecord[i]["class"]=="wep-a":
        sum = studentRecord[i]['algorithm']+studentRecord[i]['html']
        avg = sum/2
        res.append(studentRecord[i]["studentName"]+": "+str(avg))
print(res)