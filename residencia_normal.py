# Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3
#---------------------------------------------------------------------------------------------------------------------------------------------

consumo = float(input('Digite seu consumo de água em m3:  '))

if consumo <= 10:
    print('O valor da conta está em R$ 22,38')
elif consumo <= 20:
    print(f'O valor da conta está em R$ {3.50 * consumo}')
elif consumo <= 50:
    print(f'O valor da conta está em R$ {8.75 * consumo}')
else:
    print(f' valor da conta está em R$ {9.64 * consumo}')