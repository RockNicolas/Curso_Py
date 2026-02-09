idade = int(input('Qual é a sua idade: '))
autorizacao_pais = input('Você tem aturorização dosi pais? (s/n): ')

if idade >= 18:
    print('Acesso ao sistema liberado')
elif idade >= 16 and autorizacao_pais == 's':
    print('Acesso ao sistema liberado com aautorização dos pais ')
else:
    print('Acesso negado')
