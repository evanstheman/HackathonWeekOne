import random

numbers = []

for i in range(1000):
 numbers.append(random.randint(1,100))

total = sum(numbers)
average = total / 1000

print(round(average))
