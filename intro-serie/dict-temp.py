numbers = [1, 2, 3, 4]

# square_numbers = {number:number**2 for number in numbers if number > 2}

# print(square_numbers)

# Alternativ måte:

numbers = [1, 2, 3, 4]

# Lag tom dictionary 
square_numbers = {}

# Loop gjennom nummer i lista
for number in numbers:
    if number > 2:
        square_numbers[number] = number**2

print(square_numbers)