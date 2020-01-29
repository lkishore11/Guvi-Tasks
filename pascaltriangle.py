n = int(input('Enter n value: '))
c = n-1
c1 = 1

for i in range(n):
    print((' '*c), ('*'*(c1)))
    c = c-1
    c1 = c1+2
