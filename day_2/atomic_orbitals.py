n_max = int(input('n_max? '))

for n in range(1, n_max+1):
    for l in range(0, n):
        for m in range(-l, l+1):
            print(f'n = {n}   l = {l}   m = {m}')
    print(f'Total states with n = {n} : {n*n}')
