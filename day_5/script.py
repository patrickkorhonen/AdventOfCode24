import math
def answer_1():
    f = open("input.txt", "r")
    data = f.read()
    splitted = data.split("\n")
    total = 0
    rules = []
    pages = []
    for item in splitted:
        if ("|" in item):
            rules.append(item.split("|"))
        elif (len(item) > 0):
            pages.append(item.split(","))
    for page in pages:
        okay = True
        for rule in rules:
            if (rule[0] in page and rule[1] in page):
                if (page.index(rule[0]) > page.index(rule[1])):
                    okay = False
                    break
        if (okay):
            total += int(page[math.ceil(len(page) / 2) - 1])
    print(total)
    

def answer_2():
    f = open("input.txt", "r")
    data = f.read()
    splitted = data.split("\n")
    total = 0
    rules = []
    pages = []
    fixPages = []
    for item in splitted:
        if ("|" in item):
            rules.append(item.split("|"))
        elif (len(item) > 0):
            pages.append(item.split(","))
    for page in pages:
        for rule in rules:
            if (rule[0] in page and rule[1] in page):
                if (page.index(rule[0]) > page.index(rule[1])):
                    fixPages.append(page)
                    break
    for page in fixPages:
        dictionary = {}
        for number in page:
            dictionary[number] = 0
        for rule in rules:
            if (rule[0] in page and rule[1] in page):
                dictionary[rule[1]] = dictionary[rule[1]] + 1
        sortedDictionary = sorted(dictionary.items(), key=lambda x:x[1])
        total += int(sortedDictionary[math.ceil(len(sortedDictionary) / 2) - 1][0])
    print(total)
