razmer = int(input())
for pervyy_mnozhitel in range(1, razmer + 1):
    for vtoroy_mnozhitel in range(1, razmer + 1):
        rezultat = pervyy_mnozhitel * vtoroy_mnozhitel
        print(f"{pervyy_mnozhitel} * {vtoroy_mnozhitel} = {rezultat}")