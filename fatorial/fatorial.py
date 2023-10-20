numero = int(input('Fatorial de: '))
resultado = 1
multiplicador =1

while multiplicador <= numero:
    resultado = resultado * multiplicador
    multiplicador = multiplicador + 1

print(resultado)