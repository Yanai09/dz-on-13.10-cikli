apparaty = int(input())
for nomer in range(1, apparaty + 1):
    for sekundy in range(nomer - 1, -1, -1):
        print(f"Осталось секунд: {sekundy}")
    print(f"Пуск {nomer}")