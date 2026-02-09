total_produto = int(input('Quantidade: '))
consumo_por_porcao = int(input('Consumo: '))
porcao_por_dia = int(input('Porção por dia: '))

consumo_diario = porcao_por_dia * porcao_por_dia 
dias =  total_produto / consumo_diario

print(dias )