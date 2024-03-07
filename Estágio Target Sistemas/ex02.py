print ('-' * 40)
print ('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print ('-' *40)
n = int(input('Digite um número: '))
t1 = 0
t2 = 1
t3 = t1 + t2
if n == 1 or n == 0:
    print(f'O número {n} faz parte da sequência de FIbonacci')
else:
    while True:
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        if n == t1:
            print(f'O número {n} faz parte da sequência de FIbonacci')
            break
        elif t1 > n:
            print(f'O número {n} não faz parte da sequência de FIbonacci')
            break
print('FIM')
