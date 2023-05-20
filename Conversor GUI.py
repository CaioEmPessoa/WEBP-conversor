import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os


root = tk.Tk()
root.title('Image Conversor')

#  __BACKEND__  #

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

    def one_gif(imagem):
        item_numb = 0
        for item in dir_list:
            # checa se o ITEM contem '.webp'
            if item.find('.webp') != -1:

                # se achou, monta o caminho do item
                img_path = (location + '/' + item)
                print(img_path)

            if item_numb == 0 and imagem == 0:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            if item_numb == 1 and imagem == 1:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            if item_numb == 2 and imagem == 2:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            if item_numb == 3 and imagem == 3:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            if item_numb == 4 and imagem == 4:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            if item_numb == 5 and imagem == 5:
                # converte a imagem GIF do caminho
                im = Image.open(img_path)
                im.info.pop('background', None)

                index = dir_list.index(item)
                im.save(location + '/' + str(index) +
                        '.gif', 'gif', save_all=True)

                # deleta os arquivos .webp
                os.remove(img_path)

            print(item_numb)
            item_numb = item_numb + 1

    # Cria outra GUI
    root.destroy()
    choose_gif_root = tk.Tk()
    choose_gif_root.title('Choose the GIF')

    # Titulo Desse
    choose_gif_label = tk.Label(
        text='Escolha Uma das Imagens, quando terminar cliquei em "Confirmar."', font=('Comic Sans MS', 12))
    choose_gif_label.grid(row=0, column=0, columnspan=3)

    # Botão de confirmar
    confirmar = tk.Button(text='Confirmar.', font=(
        'Arial', 10), bg='lime', command=png)
    confirmar.grid(row=3, column=1)

    item_numb = 0
    for item in dir_list:
        # checa se o ITEM contem '.webp'
        if item.find('.webp') != -1:

            # se achou, monta o caminho do item
            img_path = (location + '/' + item)
            print(img_path)

            if item_numb == 0:
                gif_1 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_1 = tk.Button(image=gif_1, command=lambda: one_gif(0))
                exibir_1.grid(row=1, column=0)

            if item_numb == 1:
                gif_2 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_2 = tk.Button(image=gif_2, command=lambda: one_gif(1))
                exibir_2.grid(row=1, column=1)

            if item_numb == 2:
                gif_3 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_3 = tk.Button(image=gif_3, command=lambda: one_gif(2))
                exibir_3.grid(row=1, column=2)

            if item_numb == 3:
                gif_4 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_4 = tk.Button(image=gif_4, command=lambda: one_gif(3))
                exibir_4.grid(row=2, column=0)

            if item_numb == 4:
                gif_5 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_5 = tk.Button(image=gif_5, command=lambda: one_gif(4))
                exibir_5.grid(row=2, column=1)

            if item_numb == 5:
                gif_6 = ImageTk.PhotoImage(
                    Image.open(img_path).resize((200, 300)))

                exibir_6 = tk.Button(image=gif_6, command=lambda: one_gif(5))
                exibir_6.grid(row=2, column=2)

            if item_numb >= 6:
                direita = tk.Button(text='direita >>',
                                    font=('Arial', 10))
                direita.grid(row=3, column=2)

                esquerda = tk.Button(text='<< esquerda', font=('Arial', 10))
                esquerda.grid(row=3, column=0)

            print(item_numb)
            item_numb = item_numb + 1

    choose_gif_root.mainloop()


def webp():
    dir_list = os.listdir(location)
    # Pega a imagem e converte ela pra jpg
    for item in dir_list:
        # checa se o ITEM contem '.webp'
        if item.find('.png') != -1:
            # se achou, monta o caminho do item
            img_path = (location + '/' + item)
            print(img_path)

            # converte a imagem JPG do caminho
            im = Image.open(img_path)
            index = dir_list.index(item)
            im.save(location + '/' + str(index) + '.webp')

            # deleta os arquivos .webp
            os.remove(img_path)


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


def webp_delete():
    def delete():
        dir_list = os.listdir(location)
        # Pega a imagem e converte ela pra jpg
        for item in dir_list:
            # checa se o ITEM contem '.webp'
            if item.find('.webp') != -1:
                # se achou, monta o caminho do item
                img_path = (location + '/' + item)
                print(img_path)

                # deleta os arquivos .webp
                os.remove(img_path)
    webp_delete_button = tk.Button(
    text='CONFIRM DELETE?', bg='red', command=delete, padx=40, pady=10)
    webp_delete_button.grid(row=2, column=2)

            # __FRONT END__#


# Titulo:
titulo = tk.Label(text='Bem vindo ao conversor de imagens muitofoda!\n escolha uma das opções abaixo:', font=(
    'Comic Sans MS', 12))
titulo.grid(row=0, column=0, columnspan=3)

# Botões:
# WEBP to PNG
webp_png_button = tk.Button(
    text='WEBP to PNG \n (all images are png)', command=png, padx=20, pady=10)
webp_png_button.grid(row=1, column=0)

# WEBP TO GIF
web_gif_button = tk.Button(
    text='WEBP to GIF \n (all images are gif)', command=gif, padx=20, pady=10)
web_gif_button.grid(row=1, column=1)


# CHOOSE GIF
choose_gif_button = tk.Button(
    text='WEBP to GIF \n (One of the images are gif)', command=choose_gif, padx=20, pady=10)
choose_gif_button.grid(row=1, column=2)

# PNG TO WEBP
png_webp = tk.Button(
    text='PNG to WEBP \n (all images are png)', command=webp, padx=20, pady=10)
png_webp.grid(row=2, column=0)

# PNG TO ICO
png_webp = tk.Button(
    text='PNG to ICO \n (all images are png)', command=ico, padx=20, pady=10)
png_webp.grid(row=2, column=1)

# DELETE ALL WEBP (caution)
webp_delete_button = tk.Button(
    text='DELETE ALL WEBP \n (caution)', command=webp_delete, padx=40, pady=10)
webp_delete_button.grid(row=2, column=2)

# //    STATUS:
status_status = tk.Label(root, text='Status:', bd=1, anchor=E, fg='green')
status_status.grid(row=3, column=1, sticky=W+E)

conversion_status = tk.Label(
    root, text='Nothing...', bd=1, relief=SUNKEN, anchor=E)
conversion_status.grid(row=3, column=2, columnspan=1, sticky=W+E)

root.mainloop()
