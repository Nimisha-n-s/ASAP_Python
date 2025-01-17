data ={
    "John": {
        "Math": [85, 90, 95],
        "Science": (88, 92, 89),
        "Languages": {"English": [78, 80], "Spanish": [85]}
        },
    "Alice": {
        "Math": [78, 80, 82],
        "Science": (90, 85, 88),
        "Languages": {"English": [85, 87], "French": [82, 88]}
    },
    "Bob": {
        "Math": [90, 85],
        "Science": (85, 87),
        "Languages": {"English": [80], "German": [78, 83]}
    }
}

#1.avg for maths
sum = 0
count = 0
avgsum = 0
tavg = 0
pplcount = 0
for ppl in data.keys():
    pplcount += 1
    for mathMarks in data[ppl]["Math"]:
        count += 1
        sum += mathMarks
        avg = sum/count
    count = 0
    sum = 0
    avgsum += avg
    tavg = avgsum/pplcount


print("Math avg:", tavg)
print()

#2.avg for science

sum = 0
count = 0
avgsum = 0
tavg = 0
pplcount = 0
for ppl in data.keys():
    pplcount += 1
    for Marks in data[ppl]["Science"]:
        count += 1
        sum += Marks
        avg = sum/count
    count = 0
    sum = 0
    avgsum += avg
    tavg = avgsum/pplcount

print("Science avg: ", tavg)

#3.unique science score

uniqueScore = []
for ppl in data.keys():
    for Marks in data[ppl]["Science"]:
        for i in uniqueScore:
            if(i != Marks):
                uniqueScore.append(Marks)

#print("unique science score:", uniqueScore)

#4.add a new subject history with scores
print()
for ppl in data.keys():
    data[ppl]["History"] = [80, 82, 85]

for ppl in data.keys():
    print("History scores of", ppl)
    print(data[ppl]["History"])

#5.sort students by total average score

#6.avg score for each subject of each student
print()
sum=0
avg=0
count = 0
for ppl in data.keys():
    for subjects in data[ppl]:
        if(subjects == "Languages"):
            continue
        else:
            for marks in data[ppl][subjects]:
                count += 1
                sum += marks
                avg = sum/count
            count = 0
            sum = 0
            print(subjects + " marks for " + ppl + " is", end=" ")
            print(avg)
    print()

#7.unique scores for each subjects for each student

#8.sum of 2nd and 3rd highest scores for each subject for each student

#9.sum of list and second average of second element each dictionary