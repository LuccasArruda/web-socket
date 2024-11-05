frase = input('Informe a string: ')
palavraProcurada = input('Qual a palavra que deseja encontrar? ')

if palavraProcurada in frase:
    print('Possui!')
else:
    print('nunten')

print(len(frase.replace(' ','')))

palavras = frase.split('a')
print(len(palavras))

textao = 'eu sou um cara muito bacana, gosto de comer sorvete e dirigir aviões no mar'

textao = textao.split()
textao.sort()
print(textao)

novoTexto = textao[0] + ' ' + textao[5]
print(novoTexto)