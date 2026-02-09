def calcular_desconto(preco, porcetagem):
    return preco - (preco * porcetagem / 100)

final = calcular_desconto(100, 20)

print(f'valor final com o desconto é de R${final:.2f}')