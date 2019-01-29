s = 1000

i, sum = 1, 0
while True:
    sum += i**3
    if sum > s:
        break
    i += 1

print(f'Smallest sum of n**3 greater than {s} is {sum}')