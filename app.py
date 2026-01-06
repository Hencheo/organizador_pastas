import os
import shutil
import time

# Pede a pasta para o usuário
caminho = input()

if not caminho:
    print("Nenhuma pasta selecionada. Encerrando...")
    exit()

def extrair_extensoes():
    lista_ext = []
    if os.path.exists(caminho): 
        for arquivo in os.listdir(caminho):
            if os.path.isfile(os.path.join(caminho, arquivo)):
                ext = arquivo.split('.')[-1]
                lista_ext.append(ext)
        return set(lista_ext)
extensoes_unicas = extrair_extensoes()               

def criar_remover_pastas(acao):
    if acao == 'criar':
        for ext in extensoes_unicas:
            if not os.path.exists(f'{caminho}/{ext}'):
                os.mkdir(f'{caminho}/{ext}')
        print('Patas criadas com sucesso! Pode conferir.')
        print('='*20)

    if acao == 'remover':
        for ext in extensoes_unicas:
            if os.path.exists(f'{caminho}/{ext}'):
                shutil.rmtree(f'{caminho}/{ext}')
        print('Patas deletadas com sucesso! Pode conferir.')
        
def mover_arquivos():
    for ext in extensoes_unicas:
        caminho_pasta = os.path.join(caminho, ext)
        if os.path.exists(caminho_pasta):
            for arquivo in os.listdir(caminho):
                caminho_arquivo = os.path.join(caminho, arquivo)

                if os.path.isfile(caminho_arquivo):
                    if arquivo.endswith(f'.{ext}'):

                        destino = os.path.join(caminho_pasta, arquivo)

                        os.rename(caminho_arquivo, destino)
                
    print('Arquivos movidos com sucesso')
    print('='*20)


extrair_extensoes()
criar_remover_pastas('criar')
time.sleep(3)
mover_arquivos()