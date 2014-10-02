def fakultet(number):
    summa = 1
    while number > 0:
        summa = summa * number
        number -= 1
    return summa

print fakultet(0)