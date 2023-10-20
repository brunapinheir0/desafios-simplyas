continuar = True 
notas = []
sum_notas = 0
erro = False

while continuar is True: 
    nota = input('Digite sua nota OU para encerrar digite "fim" : ')
    if nota == "fim":
        continuar = False
        break

    try:
        nota = float(nota)
    except:
        print("por favor, use apenas numeros")
        continuar = False
        erro = True
        break

    notas.append(nota)
    sum_notas = sum_notas + nota

if erro == False:
    resultado = sum_notas / len(notas)
    print(f'A média das suas notas é: {resultado}')

