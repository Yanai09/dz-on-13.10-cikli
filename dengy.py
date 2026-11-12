predel = int(input())
for chislo in range(2, predel):
    prostoe = True
    for delitel in range(2, int(chislo ** 0.5) + 1):
        if chislo % delitel == 0:
            prostoe = False
            break
    if prostoe:
        print(chislo)
