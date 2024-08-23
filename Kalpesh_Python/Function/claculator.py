def add (num, num1):
    return num + num1

def addition(*num) :   #for dynamic additions (kitne bhi addition kar shakte hai)
    result = 0
    for i in num:
        result=result+i
    return result

def substraction(*num) :   #for dynamic additions (kitne bhi substraction kar shakte hai)
    result = 0
    for i in num:
        result=result-i
    return result

def multiplication(*num) :   #for dynamic additions (kitne bhi addition kar shakte hai)
    result = 0
    for i in num:
        result=result*i
    return result
