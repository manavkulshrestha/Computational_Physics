from scipy.special import ellipe
from numpy import sqrt

a = float(input('Enter a: '))
b = float(input('Enter b: '))

print(f'C = {4*a*ellipe(sqrt(1-((b**2)/(a**2))))}')