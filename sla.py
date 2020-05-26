aux = int(input())

for a in range (1, aux+1):
    if a % 10:
        print("{}" .format(a), end=" ")
    else:
        print("{}" .format(a), end="\n")


exit(0)