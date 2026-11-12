kolonki = int(input())
stroki = int(input())
for stroka in range(1, stroki + 1):
    for kolonka in range(1, kolonki + 1):
        print(kolonka / stroka, end=" ")
    print()