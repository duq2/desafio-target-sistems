letra_a = [1, 3, 5, 7]
prox_a = letra_a[-1] + 2
print(f'a) Próximo termo: {prox_a}')

letra_b = [2, 4, 8, 16, 32, 64]
prox_b = letra_b[-1] * 2
print(f'b) Próximo termo: {prox_b}')

letra_c = [0, 1, 4, 9, 16, 25, 36]
prox_c = (len(letra_c)) ** 2
print(f'c) Próximo termo: {prox_c}')

letra_d = [4, 16, 36, 64]
prox_d = (len(letra_d) * 2) ** 2
print(f'd) Próximo termo: {prox_d}')

letra_e = [1, 1, 2, 3, 5, 8]
prox_e = letra_e[-1] + letra_e[-2]
print(f'e) Próximo termo: {prox_e}')

letra_f = [2, 10, 12, 16, 17, 18, 19]
prox_f = letra_f[-1] + 1
print(f'f) Próximo termo: {prox_f}')