def findMaxMin( numbers ):
    max = numbers[0]
    min = numbers[0]

    for n in numbers:
        if n > max:
            max = n
        elif n < min:
            min = n

    return max, min

numbers = [4, -7, 45, 28, 9, -12]
print("List of numbers:", numbers)
print("Max and Min:", findMaxMin(numbers))