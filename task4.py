# Задача 4: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом по 
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите 1-ое число: '))
m = int(input('Введите 2-ое число: '))
k = int(input('Введите 3-ее число: '))   
if k <= m * n and (k % m == 0 or k % n == 0):
    print(f'Yes')
else:
    print(f'No')