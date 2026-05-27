class HistóricoBatalha:
    def __init__(self):
        self.logs = []

    def registrar(self, acao):
        self.logs.append(acao)

    def exibir_resumo(self):
        print("\n📜 --- HISTÓRICO DA BATALHA ---")
        for i, log in enumerate(self.logs, 1):
            print(f"{i}. {log}")
        print("-" * 32)