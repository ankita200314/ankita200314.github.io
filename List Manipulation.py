
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number ** 2)


numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)