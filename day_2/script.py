def answer_1():
    f = open("input.txt", "r")
    total = 0
    increasing_and_decreasing = []
    for line in f:
        list = []
        for number in line.split():
            list.append(int(number))
        sorted = list.copy()
        sorted_rev = list.copy()
        sorted.sort()
        sorted_rev.sort()
        sorted_rev.reverse()
        
        if (list == sorted or list == sorted_rev):
            increasing_and_decreasing.append(list)
    total += check_safety_1(increasing_and_decreasing)

    print(total)

def check_safety_1(in_list):
    total = 0
    for list in in_list:
        subtotal = 0
        for index in range(0, len(list) - 1):
            if (abs(list[index] - list[index + 1]) > 0 and abs(list[index] - list[index + 1]) < 4):
                subtotal += 1
        if (subtotal == len(list) - 1):
            total += 1
    return(total)

def check_safety(in_list):
    total = 0
    for list in in_list:
        subtotal = 0
        for index in range(0, len(list) - 1):
            if (abs(list[index] - list[index + 1]) > 0 and abs(list[index] - list[index + 1]) < 4):
                subtotal += 1
        if (subtotal == len(list) - 1):
            total += 1
        else:
            total_ns = 0
            for index in range(len(list)):
                copy = list.copy()
                copy.pop(index)
                if (check_list_safety(copy) == 1):
                    total_ns += 1
                    break
            total += total_ns
    return(total)

def check_list_safety(in_list):
    total = 0
    subtotal_dec = 0
    subtotal_inc = 0
    for index in range(0, len(in_list) - 1):
        if (in_list[index] - in_list[index + 1] > 0 and in_list[index] - in_list[index + 1] < 4):
            subtotal_dec += 1
        elif (in_list[index] - in_list[index + 1] < 0 and in_list[index] - in_list[index + 1] > -4):
            subtotal_inc += 1
    if (subtotal_dec == len(in_list) - 1 or subtotal_inc == len(in_list) - 1):
        total += 1
    return(total)
            

def answer_2():
    f = open("input.txt", "r")
    total = 0
    increasing_and_decreasing = []
    not_safe = []
    for line in f:
        list = []
        for number in line.split():
            list.append(int(number))
        sorted = list.copy()
        sorted_rev = list.copy()
        sorted.sort()
        sorted_rev.sort()
        sorted_rev.reverse()
        
        if (list == sorted or list == sorted_rev):
            increasing_and_decreasing.append(list)
        else:
            not_safe.append(list)
        
    total += check_safety(increasing_and_decreasing)

    total_for_nosafe = 0

    for list in not_safe:
        for index in range(len(list)):
            copy = list.copy()
            copy.pop(index)
            if (check_list_safety(copy) == 1):
                total_for_nosafe += 1
                break
    total += total_for_nosafe

    print(total)
answer_2()