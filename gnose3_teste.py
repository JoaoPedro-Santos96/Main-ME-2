class Gnose:
    obj = []  # lista para armazenar todos os objetos criados

    def __init__(self, tecido):
        self.tecido = tecido
        Gnose.obj.append(self)

    def rasgar(self):
        print(f"O tecido da realidade foi rasgado em {self.tecido}% ")

    def costurar(self):  # <-- Função nova (inverso de rasgar)
        print(f"O tecido da realidade foi costurado em {self.tecido}% ")

    def excluir(self):
        Gnose.obj.remove(self)
        print("Objeto excluído")

    def editar(self, novo_tecido):
        self.tecido = novo_tecido
        print(f"Tecido atualizado para {self.tecido}%")

    def detalhes(self):
        print(f"Objeto com tecido = {self.tecido}%")

    @classmethod
    def lista(cls):
        return cls.obj


# Testando
g1 = Gnose(200)
g2 = Gnose(400)

g1.rasgar()
g1.editar(250)
g1.detalhes()
g1.costurar()  # usando a nova função

print("Objetos existentes:", Gnose.lista())
g2.excluir()
print("Objetos restantes:", Gnose.lista())
