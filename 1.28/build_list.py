data = []

while True:
    inp = float(input('Enter reading (<0 to stop): '))
    if(inp >= 0):
        data.append(inp)
    else:
        break

length = len(data)
mean = sum(data)/length
print(f'Readings: {data}')
print(f'Number of readings: {length}')
print(f'Average reading: {mean}')

print('Average reading (formatted): {:2.4}'.format(mean))
print(f'Smallest reading: {min(data)}')
print(f'Largest reading: {max(data)}')

print(f'Standard deviation: {((sum((x-mean)**2 for x in data)/length)**.5)}')