import time
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi 
from utils import HistóricoBatalha 

def main():
    historico = HistóricoBatalha()


    # Criando personagens e vilões
    heroi = Heroi('Link', 30, 100, 'Guerreiro')
    npc = Personagem('Zelda', 28, 80)
    vilao = Vilao('Ganon', 45, 120, 'Alta')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)
    historico.registrar(f"{vilao.nome} atacou {heroi.nome}")

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')
    historico.registrar(f"{heroi.nome} recebeu upgrade de vida")

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')
    historico.registrar(f"Nome do NPC atualizado para {npc.nome}")
    print("=" * 50 + "\n")

    print("=== [ PARTE 2: EXPANSÃO DO DESAFIO ] ===")
    vilao.dialogar("Seu upgrade não será suficiente, Link!")
    heroi.dialogar("Veremos, Ganon!")
    time.sleep(1)

    turno = 1
    while heroi.vivo and vilao.vivo:
        print(f"\n🎮 --- TURNO {turno} ---")
        print(f"❤️ {heroi.nome}: {heroi.vida} HP | ❤️ {vilao.nome}: {vilao.vida} HP")
        print("Escolha a ação do Herói:")
        print("[1] Atacar (Usa a nova função de ataque)")
        print("[2] Usar Poção de Cura")
        print("[3] Salvar um Refém")
        
        opcao = input("Digite sua opção (1-3): ")
        print("-" * 30)

        if opcao == "1":
            heroi.atacar(vilao) 
            historico.registrar(f"Turno {turno}: {heroi.nome} atacou {vilao.nome}")
        elif opcao == "2":
            heroi.usar_pocao()
            historico.registrar(f"Turno {turno}: {heroi.nome} usou poção")
        elif opcao == "3":
            heroi.salvar_refem()
            historico.registrar(f"Turno {turno}: {heroi.nome} salvou refém")
        else:
            print("Opção inválida! Perdeu o turno.")

        if not vilao.vivo:
            break

        # Turno do Vilão
        time.sleep(1)
        print(f"\n👹 Turno de {vilao.nome}...")
        vilao.ataque(heroi) 
        historico.registrar(f"Turno {turno}: {vilao.nome} atacou {heroi.nome}")
        
        turno += 1

    print("\n🏁 FIM DA BATALHA 🏁")
    if heroi.vivo:
        print(f"🎉 {heroi.nome} venceu!")
    else:
        print(f"💀 {vilao.nome} venceu...")

    historico.exibir_resumo()

if __name__ == "__main__":
    main()
