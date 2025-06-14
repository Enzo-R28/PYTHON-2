"""
    Objetivo: revisar manipulação de tuplas
    Comandos utolizados: tupla,
"""

from os import system, name
import random
def gg():
    pass
    opcao = 'S'
    while opcao.upper()=='S':
        system('cls') if(name== 'nt')else system('clear')
        computador = random.randint(0,2) #randomiza a escolha da CPU
        jogador = int(input('''Escolha uma opção para se jogar:
        [1] Pedra
        [2] Papel
        [3] Tesoura
        Digite sua escolha: '''))-1
        pecas = ("Pedra", "Papel", "Tesoura")
        mJogador = "Você GANHOU. Hoje está com sorte!!"
        mCPU = "Deu RED. Tente de novo marreco!!"
        mEmpate = "Humm... empatou, ó perdeu temo!"
        tabela =(
            (mEmpate,  mJogador , mCPU),
            (mCPU, mEmpate,  mJogador  ),
            ( mJogador  , mCPU, mEmpate)
        )
        print(f'você escolheu {pecas[jogador]}')
        print(f'A CPU escolheu {pecas[computador]}')
        print(f'{tabela[computador][jogador]} Ganhou!!!')
        opcao=input('Jogar Novamente? Aperte S para jogar novamente.')

if(__name__ == "__main__"):
    gg()