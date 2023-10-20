n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

try: 
    int_n1 = int(n1)
    int_n2 = int(n2)

    print(f'A soma dos números é: {int_n1 + int_n2}')
except:
    print('Favor utilizar apenas números')
