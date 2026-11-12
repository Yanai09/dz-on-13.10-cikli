predel = int(input())
tekushee_chislo = 1
dlina_stroki = 1
while tekushee_chislo <= predel:
    for shag in range(dlina_stroki):
        if tekushee_chislo <= predel:
            print(tekushee_chislo, end=" ")
            tekushee_chislo += 1
    print()
    dlina_stroki += 1