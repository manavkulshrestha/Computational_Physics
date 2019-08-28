x = float(input('Input x: '))
e = [int(x) for x in input('Input e: ').split('e')]
e = e[0]**e[1]

print(f'x = {x}\nx+ex = {x+e*x}')

for i in range(1, 1000):
    if x == x+(10**-i)*x:
        print(i)
        break
