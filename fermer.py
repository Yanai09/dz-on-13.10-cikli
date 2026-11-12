subsidiya = int(input())
vsego_golov = int(input())
for byki in range(1, subsidiya // 20 + 1):
    for korovy in range(0, subsidiya // 10 + 1):
        telyata = vsego_golov - byki - korovy
        if telyata >= 0:
            stoimost = byki * 20 + korovy * 10 + telyata * 5
            if stoimost == subsidiya:
                print(byki, korovy, telyata)
