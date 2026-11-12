vsego_cifr = int(input())
kilometry = 0
nabrannye_cifry = 0
while nabrannye_cifry < vsego_cifr:
    kilometry += 1
    nabrannye_cifry += len(str(kilometry))
print(kilometry)