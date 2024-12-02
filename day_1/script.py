
def answer_1():
    f = open("input.txt", "r")
    left = []
    right = []
    total = 0
    for line in f:
        splitted = line.split()
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))
    left.sort()
    right.sort()
    for index in range(len(left)):
        total += abs(left[index] - right[index])
    print(total)

def answer_2():
    f = open("input.txt", "r")
    left = []
    right = []
    total = 0
    for line in f:
        splitted = line.split()
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))
    for i in range(len(left)):
        subtotal = 0
        for j in range(len(right)):
            if (left[i] == right[j]):
                subtotal += 1
        total += left[i] * subtotal 
                
    print(total)

answer_2()