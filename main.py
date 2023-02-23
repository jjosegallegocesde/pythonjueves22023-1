#Condicionales con PYTHON
nivelAgua=int(input("Digita el nivel de agua: "))
if nivelAgua>=0 and nivelAgua<=250:
    print(f'el nivel de agua es muy bajo {nivelAgua} U')
elif nivelAgua>250 and nivelAgua<=450:
    print(f'el nivel de agua es optimo {nivelAgua} U')
elif nivelAgua>450:
    print(f'el nivel de agua es critico, evacue {nivelAgua} U')
else:
    print("Revisar el sensor")