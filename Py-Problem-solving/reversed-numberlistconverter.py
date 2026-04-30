numbers = []

def convert(number):
    myList = list(str(number))
    
    for item in myList:
        numbe = int(item)
        numbers.insert(0, numbe)
    return numbers

print(convert(176768264356))