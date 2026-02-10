class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.baneiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')

    def mostrar_quartos(self):
        print(f'essa casa tem: {self.quartos} quartos ')

    def mostrar_banheiro(self):
        print(f'Essa casa tem: {self.baneiros} banheiros')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Esta casa tem {self.quartos} quartos')

    def trocar_cor(self):
        self.cor = 'vermelho'
        print (f'casa 1 agora é {self.cor} ')

    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')

casa1 = Casa('Azul', 4, 2,)
casa2 = Casa('verde', 6, 3, )

print(f'\ncasa 1: ')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiro()
casa1.adicionar_quarto()
casa1.trocar_cor()

print(f'\ncasa 2: ')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiro()
casa2.adicionar_quarto()
casa2.pintar_casa('vermlho')