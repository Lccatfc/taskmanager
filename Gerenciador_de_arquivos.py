import os, re
import pathlib
import shutil

caminho = r"C:\Users\Predator\Downloads"
os.chdir(caminho)
lista_arquivos = os.listdir()

arquivos = []
pasta = []

dicionario_extensoes = set()

for arquivo in lista_arquivos:
    if os.path.isfile(arquivo):
        arquivos.append(arquivo)
    else:
        os.path.isdir(arquivo)
        pasta.append(arquivo)

for arquivo in arquivos:
    arquivo, extensao = os.path.splitext(arquivo)
    if extensao not in dicionario_extensoes:
        E = extensao.replace('.', '')
        dicionario_extensoes.add(E)

    try:
        if dicionario_extensoes == set():
            os.makedirs(extensao)
    except:
        print('já tem uma pasta dessa bro')

for arquivo in arquivos:
    extensao = os.path.splitext(arquivo)
    extensao_sem_ponto = extensao[1].replace('.', '')
    shutil.move(arquivo, extensao_sem_ponto)
