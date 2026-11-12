predel = int(input())
obshaya_summa = 0
for chislo in range(1, predel + 1):
    stepen = 0
    if chislo % 2 == 1:
        nachalo = 1
    else:
        nachalo = 2
    for slagaemoe in range(nachalo, chislo + 1, 2):
        stepen += slagaemoe
    obshaya_summa += chislo ** stepen
print(obshaya_summa)