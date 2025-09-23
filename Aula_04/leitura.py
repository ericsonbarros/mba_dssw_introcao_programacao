from time import sleep
with open('curso em vídeo python.txt', 'r', encoding='utf-8') as arquivo:
# PARA LER O CONTEUDO POR INTEIRO
    # conteudo = arquivo.read()
    # print(conteudo)

# PARA LER LINHA A LINHA
    # i = 0
    # for linha in arquivo:
        # i += 1
        # print(f'{i} - {linha.rstrip()}')
        # sleep(1)

# PARA LER LINHA
    # linhas = arquivo.readline()
# for l in linhas:
    # print(f'{l.rstrip()}', end='')

    conteudo = arquivo.read()
    print(conteudo)
