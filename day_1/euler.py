from numpy import exp, sin, cos, pi

def print_euler(alpha):
    print(f'LHS = {exp((0+1j)*alpha)}\nRHS = {complex(cos(alpha),sin(alpha))}')

for i in range(0, 11):
    print(f'{print_euler(i)}\n')

alpha = complex(input('Input alpha: '))
print_euler(alpha)