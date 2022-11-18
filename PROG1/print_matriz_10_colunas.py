aux = int(input())

for a in range (1, aux+1):
    if a % 10:
        res = f'0{a}' if a < 10 else f'{a}'
        print(res, end=" ")
    else:
        print(f'{a}')


exit(0)