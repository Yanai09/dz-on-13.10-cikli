dorogi = int(input())
otvet = (0, 0)
for nomer in range(1, dorogi + 1):
    tuneli = int(input())
    min_vysota = min(int(input()) for _ in range(tuneli))
    otvet = max(otvet, (min_vysota, nomer))
print(otvet[1], otvet[0])