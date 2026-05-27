class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, ataque=15, defesa=10):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.forca = ataque 
        self.defesa = defesa 
        self.vivo = True 

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self, dano_recebido=15):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > dano_recebido:
            self.vida -= dano_recebido
        else:
            self.vida = 0
            self.vivo = False 
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def dialogar(self, mensagem):
        """Método para intrações textuais."""
        print(f'💬 [{self.nome}]: "{mensagem}"')

    def atacar(self, oponente):
        print(f'{self.nome} tentou atacar {oponente.nome}!') 
        dano_final = max(5, self.forca - oponente.defesa)
        oponente.downgrade_vida(dano_final)


    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
