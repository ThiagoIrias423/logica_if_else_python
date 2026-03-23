# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Entregando o consumo já em m3 para entrega do valor
consumo = float(input('Digite seu consumo de água em m3:  '))
#m3 = metros cubicos
if consumo <= 10:
    print('O valor da conta está em R$ 7,59')
elif consumo <= 20:
    print(f'O valor da conta está em R$ {1.31 * consumo:.2f}')
elif consumo <= 30:
    print(f'O valor da conta está em R$ {4.64 * consumo:.2f}')
elif consumo <= 50:
    print(f'O valor da conta está em R$ {6.62 * consumo:.2f}')
else:
    print(f'O valor da conta está em R$ {7.31 * consumo:.2f}')
