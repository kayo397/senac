class Ataque:
    def __init__(self, nome, dano, tipo, geraEnergia):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.geraEnergia = geraEnergia

    def __str__(self):
        return f"Nome: {self.nome}, Dano: {self.dano}, Tipo: {self.tipo}, Geração de Energia: {self.geraEnergia}"

class AtaqueRapido(Ataque):
    def __init__(self, nome, dano, tipo, geraEnergia):
        super().__init__(nome, dano, tipo, geraEnergia)

class AtaqueCarregado(Ataque):
    def __init__(self, nome, dano, tipo, geraEnergia):
        super().__init__(nome, dano, tipo, geraEnergia)

class Pokemon:
    def __init__(self, nome, hp, iv, tipos, ataqueRapido, ataquesCarregados):
        self.nome = nome
        self.hp = hp
        self.iv = iv
        self.tipos = tipos
        self.ataqueRapido = ataqueRapido
        self.energiaAcumulada = 0
        self.ataquesCarregados = ataquesCarregados

    def atacar(self, alvo, ataque):     
        dano = (ataque.dano * self.iv) / 65
        print(f"{self.nome} usou {ataque.nome} em {alvo.nome} e causou {dano} de dano.")
        self.energiaAcumulada += ataque.geraEnergia
        print(f"{self.nome} acumulou {ataque.geraEnergia} de energia.")
        alvo.hp -= dano
        if alvo.hp <= 0:
            print(f"{alvo.nome} foi derrotado!")
            return True 
        return False

    def __str__(self):
        return f"Nome: {self.nome}, HP: {self.hp}"