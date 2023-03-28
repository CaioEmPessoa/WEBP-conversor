import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

# location do app
location = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

# lista os arquivo q ta na pasta do app
dir_list = os.listdir(location)


def png():
    dir_list = os.listdir(location)
    # Pega a imagem e converte ela pra jpg
    for item in dir_list:
        # checa se o ITEM contem '.webp'
        if item.find('.webp') != -1:
            # se achou, monta o caminho do item
            img_path = (location + '/' + item)
            print(img_path)

            # converte a imagem JPG do caminho
            im = Image.open(img_path)
            index = dir_list.index(item)
            im.save(location + '/' + str(index) + '.png')

            # deleta os arquivos .webp
            os.remove(img_path)


def gif():
    for item in dir_list:
        # checa se o ITEM contem '.webp'
        if item.find('.webp') != -1:

            # se achou, monta o caminho do item
            img_path = (location + '/' + item)
            print(img_path)

            # converte a imagem GIF do caminho
            im = Image.open(img_path)
            im.info.pop('background', None)

            index = dir_list.index(item)
            im.save(location + '/' + str(index) + '.gif', 'gif', save_all=True)

            # deleta os arquivos .webp
            os.remove(img_path)


def choose_gif():

    print('Escreva o nome do gif e digite enter. \n (não coloque a extenção no nome)')
    print(dir_list)
    hold_on = input('')

    try:
        # abre a imagem com o nome
        im = Image.open(location + '/' + hold_on + '.webp')
        im.info.pop('background', None)

    # mensagem de erro
    except FileNotFoundError as e:
        print(FileNotFoundError(
            'Arquivo não encontrado! \n precione "enter" para reiniciar...'))
        merda = input('')
        começo()

    # salva a imagem com o nome passado
    im.save(location + '/' + str(hold_on) +
            '.gif', 'gif', save_all=True)

    # deleta o arquivo antigo
    os.remove(location + '/' + hold_on + '.webp')

    print('Acabou? s/n')
    choose_gif_end = input('')

    # volta pro começo
    if choose_gif_end == 'n':
        choose_gif()

    # chama o png caso acabou
    elif choose_gif_end == 's':
        png()

    else:
        print('resposta inválida! \n Recomeçando... \n')
        começo()


def ico():
    dir_list = os.listdir(location)
    # Pega a imagem e converte ela pra jpg
    for item in dir_list:
        # checa se o ITEM contem '.png'
        if item.find('.png') != -1:
            # se achou, monta o caminho do item
            img_path = (location + '/' + item)
            print(img_path)

            # converte a imagem JPG do caminho
            im = Image.open(img_path)
            index = dir_list.index(item)
            im.save(location + '/' + str(index) + '.ico')

            # deleta os arquivos .png
            os.remove(img_path)

# COMEÇO DO APP


def começo():

    # pergunta de qual tipo de conversão quer
    print('Converte todas imagem .webp da pasta para:' +
          '\n 1 = .png \n 2 = .gif \n 3 = .ico' +
          "\n\npara sair digite exit \n")
    type_qst = input('')

    match type_qst:

        # converte os arquivos pra png
        case '1':
            png()

    # Converte todas pra gif
        case '2':
            gif()

        case '3':
            ico()

        # sai do app
        case 'exit':
            exit

    # Resposta Inválida
        case _:
            print('resposta inválida! \n Recomeçando... \n')
            começo()


começo()
