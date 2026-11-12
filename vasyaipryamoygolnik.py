vysota = int(input())
shirina = int(input())
simvol = input()
for stroka in range(vysota):
    for stolbec in range(shirina):
        if stroka == 0 or stroka == vysota - 1 or stolbec == 0 or stolbec == shirina - 1:
            print(simvol, end="")
        else:
            print(" ", end="")
    print()