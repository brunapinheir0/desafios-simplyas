vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Digite uma palavra: '))
tamanho = len(palavra)
qtd_vogais = 0

for letra in palavra:
    letra.lower()
    if letra in vogais:
        qtd_vogais = qtd_vogais + 1

print("Esta palavra possui ", qtd_vogais, " vogais")