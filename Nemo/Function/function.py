#def greet():   #function definition
   # print("hello,welcome")

#greet()  # function call

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
def maths():
   
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
maths()
def science():
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
science()
