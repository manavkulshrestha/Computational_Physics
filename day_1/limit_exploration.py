t = None

for i in range(1, 10000):
    t = 10**i

print(t)

for i in range(-1, -1000, -1):
    t = 10**i
    if(t == 0.0):
        print(f'smallest possible float is 10e{i+1}')
        break