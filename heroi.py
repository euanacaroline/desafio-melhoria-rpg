from personagem import Personagem 

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """

    def __init__(self, nome, idade, vida, classe_heroi="Guerreiro"):
        super().__init__(nome, idade, vida, ataque=25, defesa=12)
        self.classe = classe_heroi
        self.inventario = ["Poção de Cura"] 

    def usar_pocao(self):
        """Método próprio do herói para curar usando item da lista."""
        if "Poção de Cura" in self.inventario:
            self.inventario.remove("Poção de Cura")
            print(f'🧪 {self.nome} usou uma Poção de Cura!')
            self.upgrade_vida(20) 
        else:
            print(f'❌ {self.nome} não tem mais poções!')

    def salvar_refem(self):
        """Método próprio do herói que concede bônus de vida."""
        print(f'🦸 {self.nome} salvou um refém e ganhou vigor!')
        self.upgrade_vida(15)