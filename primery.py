nachalo = int(input())
konec = int(input())
shag = int(input())
for pervoe in range(nachalo, konec + 1, shag):
    for vtoroe in range(nachalo, konec + 1, shag):
        summa = pervoe + vtoroe
        print(f"{pervoe} + {vtoroe} = {summa}", end="\t")
    print()