import random
from os import path
def iprime_mensagem_abertura():
    print("***************************")
    print("------ JOGO DA FORCA ------")
    print("***************************")
def definir_tema():
    dica = int(input("""
                    Digite a opção para o tema
                     1 - Carros
                     2 - Cidades do Brasil
                     3 - países
                     4 - Nome de pessoas
                     5 - Frutas
                    """))
    dicas = ('carro', 'cidade', 'país', 'nome', 'fruta')
    return dicas[dica-1]
def carrega_palavra_secreta(tema):
    dirName = path.dirname(path.abspath(__file__))
    arquivo = open(f"{dirName}\\{tema}.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close
    numero = random.randrange(0, len(palavras)+1)
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def init_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]