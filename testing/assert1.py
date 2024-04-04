def summer(liste):
    # Alternativ 1:
    # return sum(liste)

    # Alternativ 2:
    total = 0
    for i in liste:
        total += i
    return total

# print(summer([1, 2, 3]))

assert summer([1, 2, 3]) == 6, "Should be 6"
assert summer([1, 2, 3, 4]) == 10, "Should be 10"
assert summer([1, 2, 3, 4, 5]) == 15, "Should be 15"