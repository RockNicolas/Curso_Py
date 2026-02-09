user = input('Digite seu user: ')
senha = input('Digite sua senha: ')

login_valido = user == 'Teste' and senha == '123'

print(f'{login_valido} seu login foi valido ')