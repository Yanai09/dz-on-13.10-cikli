razmer = int(input())
for stroka in range(1, razmer + 1):
    for stolbec in range(1, razmer + 1):
        print(stroka * stolbec, end="\t")
    print()