arquivo_contatos = open ('/home/leonardoorizio/Documentos/modelos.py', encoding='latin_1')

conteudo = arquivo_contatos.readlines()

for linha in conteudo:
        print(linha, end='')
