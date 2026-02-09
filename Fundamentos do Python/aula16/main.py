from funcoes import saudacao,soma, verficar_maioridade

saudacao('rock')
print(soma(2,10))

minha_idade = int(input('Digite a sua idade: '))

if verficar_maioridade(minha_idade):
    print('vocè é maior de idade: ')
else:
    print('vc é menor de idade')