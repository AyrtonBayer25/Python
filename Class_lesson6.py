def average(numbers):
    length = len(numbers)
    #print(length)
    total = 0.0
    for number in numbers:
        
        total += number
    return total / length
        #rint(average([1, 5, 9]))

print(average(range(11)))