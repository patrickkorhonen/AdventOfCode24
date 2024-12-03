def answer_1():
    f = open("input.txt", "r")
    data = f.read()
    splitted = data.split("mul")
    mul_array = []
    updated_mul_array = []
    total = 0
    for item in splitted:
        x = item.split(")")[0]
        if (x.find("(") == 0 and x.find(",") > 1):
            mul_array.append(x)
    for item in mul_array:
        x = item.split("(")[1]
        y = x.split(",")
        if ((y[0]).isnumeric() and (y[1]).isnumeric()):
            updated_mul_array.append(y)   
    for mul_item in updated_mul_array:
        total += int(mul_item[0]) * int(mul_item[1])
    print(total)


def answer_2():
    f = open("input.txt", "r")
    data = f.read()
    only_included = []
    splitted_do = data.split("do")
    for i in splitted_do:
        if (not i.startswith("n't")):
            only_included.append(i)
    splitted = []
    for item in only_included:
        for x in item.split("mul"):
            splitted.append(x)
    mul_array = []
    updated_mul_array = []
    total = 0
    for item in splitted:
        x = item.split(")")[0]
        if (x.find("(") == 0 and x.find(",") > 1):
            
            mul_array.append(x)
    for item in mul_array:
        x = item.split("(")[1]
        y = x.split(",")
        if ((y[0]).isnumeric() and (y[-1]).isnumeric()):
            
            updated_mul_array.append(y)   
    for mul_item in updated_mul_array:
        total += int(mul_item[0]) * int(mul_item[1])
    print(total)

answer_2()
