year = int(input('year? '))
print(f'{"" if year%400 == 0 or (year%4 == 0 and not year%100 == 0) else "not a "}leap year')