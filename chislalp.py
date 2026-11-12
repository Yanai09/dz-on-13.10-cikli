for pervoe in range(1, 10000):
    vtoroe = 0
    for delitel in range(1, pervoe // 2 + 1):
        if pervoe % delitel == 0:
            vtoroe += delitel
    if pervoe < vtoroe < 10000:
        summa_vtorogo = 0
        for delitel in range(1, vtoroe // 2 + 1):
            if vtoroe % delitel == 0:
                summa_vtorogo += delitel
        if summa_vtorogo == pervoe:
            print(pervoe, vtoroe)