def answer_1():
    f = open("input.txt", "r")
    text = []
    for textline in f:
        text.append(textline)
    total = 0
    linenumber = 0
    for line in text:   
        temp_index = 0
        for char in line:
            #left to right
            if (char == "X" and temp_index < 139):
                if (line[temp_index + 1] == "M"):
                    if (line[temp_index + 2] == "A"):
                        if (line[temp_index + 3] == "S"):
                            total += 1
            #right to left
            if (char == "X" and temp_index > 2):
                if (line[temp_index - 1] == "M"):
                    if (line[temp_index - 2] == "A"):
                        if (line[temp_index - 3] == "S"):
                            total += 1
            #top to bottom
            if (char == "X" and linenumber < 137):
                if (text[linenumber + 1][temp_index] == "M"):
                    if (text[linenumber + 2][temp_index] == "A"):
                        if (text[linenumber + 3][temp_index] == "S"):
                            total += 1
            #bottom to top
            if (char == "X" and linenumber > 2):
                if (text[linenumber - 1][temp_index] == "M"):
                    if (text[linenumber - 2][temp_index] == "A"):
                        if (text[linenumber - 3][temp_index] == "S"):
                            total += 1
            #diagonal to bottom right
            if (char == "X" and temp_index < 139 and linenumber < 137):
                if (text[linenumber + 1][temp_index + 1] == "M"):
                    if (text[linenumber + 2][temp_index + 2] == "A"):
                        if (text[linenumber + 3][temp_index + 3] == "S"):
                            total += 1
            #diagonal to bottom left
            if (char == "X" and temp_index > 2 and linenumber < 137):
                if (text[linenumber + 1][temp_index - 1] == "M"):
                    if (text[linenumber + 2][temp_index - 2] == "A"):
                        if (text[linenumber + 3][temp_index - 3] == "S"):
                            total += 1
            #diagonal to top right
            if (char == "X" and temp_index < 139 and linenumber > 2):
                if (text[linenumber - 1][temp_index + 1] == "M"):
                    if (text[linenumber - 2][temp_index + 2] == "A"):
                        if (text[linenumber - 3][temp_index + 3] == "S"):
                            total += 1
            #diagonal to top left
            if (char == "X" and temp_index > 2 and linenumber > 2):
                if (text[linenumber - 1][temp_index - 1] == "M"):
                    if (text[linenumber - 2][temp_index - 2] == "A"):
                        if (text[linenumber - 3][temp_index - 3] == "S"):
                            total += 1
            temp_index += 1
        linenumber += 1
    print(total)
        
    
def answer_2():
    f = open("input.txt", "r")
    text = []
    for textline in f:
        text.append(textline)
    total = 0
    linenumber = 0
    for line in text:   
        temp_index = 0
        for char in line:
            if (char == "A" and temp_index < 141 and temp_index > 0 and linenumber > 0 and linenumber < 139):
                if (text[linenumber - 1][temp_index - 1] == "M" and text[linenumber - 1][temp_index + 1] == "M"):
                    if (text[linenumber + 1][temp_index - 1] == "S" and text[linenumber + 1][temp_index + 1] == "S"):
                        total += 1
            if (char == "A" and temp_index < 141 and temp_index > 0 and linenumber > 0 and linenumber < 139):
                if (text[linenumber - 1][temp_index - 1] == "S" and text[linenumber - 1][temp_index + 1] == "S"):
                    if (text[linenumber + 1][temp_index - 1] == "M" and text[linenumber + 1][temp_index + 1] == "M"):
                        total += 1
            if (char == "A" and temp_index < 141 and temp_index > 0 and linenumber > 0 and linenumber < 139):
                if (text[linenumber - 1][temp_index - 1] == "M" and text[linenumber - 1][temp_index + 1] == "S"):
                    if (text[linenumber + 1][temp_index - 1] == "M" and text[linenumber + 1][temp_index + 1] == "S"):
                        total += 1
            if (char == "A" and temp_index < 141 and temp_index > 0 and linenumber > 0 and linenumber < 139):
                if (text[linenumber - 1][temp_index - 1] == "S" and text[linenumber - 1][temp_index + 1] == "M"):
                    if (text[linenumber + 1][temp_index - 1] == "S" and text[linenumber + 1][temp_index + 1] == "M"):
                        total += 1
            temp_index += 1
        linenumber += 1
    print(total)
        
    
answer_2()