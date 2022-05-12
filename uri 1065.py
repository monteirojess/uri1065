cont = number = 0
for number in range (5):
    number = float(input())
    if number % 2 == 0:
        cont += 1
print('{} valores pares'.format(cont))