# Vou comentar essa desgraça inteira pra não esquecer na hora de apresentar S2
import warnings
from customtkinter import *
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib as mpl

# Desativa os avisos gerados pelo CTk e Pillow, deixando o código mais rápido e o console menos poluído
warnings.filterwarnings("ignore")

# Define o tamanho da janela
padrao_x = 1366
padrao_y = 768

trocar = input("Deseja trocar a resolução da tela? (S/N)")
if trocar.upper() == "S":
    padrao_x = int(input("Tamanho X: "))
    padrao_y = int(input("Tamanho Y: "))
else:
    pass

# Cria a janela principal e aplica o modo escuro
root = CTk()
root.geometry(f'{padrao_x}x{padrao_y}')
set_appearance_mode('Dark')

# Coloca a janela em modo de tela cheia e força sua abertura em primeiro plano
root.attributes('-fullscreen', True)
root.focus_force()
root.attributes('-topmost', True)
# Permite novamnete que a janela seja minimizada ou tirada de foco após 1 segundo
root.after(1000, lambda: root.attributes('-topmost', False))

# Lista de nomes das pessoas do grupo
group_members = ["Pedro", "Carlos Eduardo", "Luis Felipe", "Gabriel", "Vinicius"]
# Lista de imagens correspondentes
group_images = ["frame_pedro_1.png", "frame_luiz_1.png", "frame_gabriel_1.png", "frame_carlos_1.png", "frame_vinicius_1.png"]
group_images_result = ["frame_pedro_2.png", "frame_luiz_2.png", "frame_gabriel_2.png", "frame_carlos_2.png", "frame_vinicius_2.png"]
current_member_index = 0


# Códigos de cada membro no arquivo jupyter


# Função para limpar todos os widgets da janela
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Função para criar um novo label, com texto e coordeenadas
def create_label(text, x, y):
    label = CTkLabel(root, text=text, bg_color="transparent", corner_radius=12, font=("Arial", 20))
    label.place(relx=x, rely=y, anchor="center")

# Função para criar um novo botão, pedindo apenas o comando dele,   ue será outra função
def create_button(command):
    if padrao_x <= 1100:
        # define a imagem utilizada como botão (é mais bunitin)
        image = Image.open('botao.png')
        resized_image = image.resize((round(int(15/100 * padrao_x)), round(int(8/100 * padrao_y))))
        photo = ImageTk.PhotoImage(resized_image)
        # especificações gigantescas pra fazer isso funcionar com uma imagem
        button = CTkButton(root, text='', image=photo, command=command, corner_radius=25, 
                        border_width=0, fg_color='#29243E', bg_color='#29243E', hover_color='#29243E')
        button.image = photo
        # posiciona o botao em um local prefedinido
        button.place(relx=0.9, rely=0.928, anchor="center")
        
        # tava comentando de baixo pra cima, isso é a mesma coisa que a próxima
        image2 = Image.open('fuckedcorner.png')
        resized_image2 = image2.resize((28, 90))
        photo2 = ImageTk.PhotoImage(resized_image2)
        image_label = CTkLabel(root, text="", image=photo2)
        image_label.image2 = photo2
        image_label.place(relx=0.982, rely=0.93, anchor="center")
    else:
        # define a imagem utilizada como botão (é mais bunitin)
        image = Image.open('botao.png')
        resized_image = image.resize((round(int(15/100 * padrao_x)), round(int(8/100 * padrao_y))))
        photo = ImageTk.PhotoImage(resized_image)
        # especificações gigantescas pra fazer isso funcionar com uma imagem
        button = CTkButton(root, text='', image=photo, command=command, corner_radius=25, 
                        border_width=0, fg_color='#29243E', bg_color='#29243E', hover_color='#29243E')
        button.image = photo
        # posiciona o botao em um local prefedinido
        button.place(relx=0.89, rely=0.9, anchor="center")


# Função para criar uma nova imagem
# Pede o endereço da imagem, localização para inserir e o tamanho
def create_image(image_path, x, y, tamx, tamy):
    # abre e redimensiona a imagem
    image = Image.open(image_path)
    resized_image = image.resize((tamx, tamy))
    # utiliza o pillow para carregar a imagem, ja que a porra do tkinter nao funciona
    photo = ImageTk.PhotoImage(resized_image)
    image_label = CTkLabel(root, text="", image=photo)
    image_label.image = photo
    # posiciona a imagem na posicao indicada
    image_label.place(relx=x, rely=y, anchor="center")

# Função para criar a tela inicial
def create_initial_screen():
    clear_window()
    # projeta a imagem inicial
    create_image('inicial.png', 0.5, 0.5, padrao_x, padrao_y)
    create_button(create_member_screen)

def create_final_screen():
    clear_window()
    # projeta a imagem final
    create_image('encerramento.png', 0.5, 0.5, padrao_x, padrao_y)
    global current_member_index
    current_member_index = 0
    create_button(create_initial_screen)

# Função para criar a tela de cada pessoa
def create_member_screen():
    clear_window()
    # criar a imagem correspondente do membro atual
    create_image(group_images[current_member_index], 0.5, 0.5, padrao_x, padrao_y)
    create_button(create_result_screen)

# Função para criar a tela de resultado
def create_result_screen():
    clear_window()
    # projeta a imagem referente ao membro
    create_image(group_images_result[current_member_index], 0.5, 0.5, padrao_x, padrao_y)
    create_button(next_member)

# Função para passar para o próximo membro
def next_member():
    # Aumenta o índice, para trocar de membro 
    global current_member_index
    current_member_index += 1
    # se o indice for maior que o numero de membros, o código reinicia
    if current_member_index < len(group_members):
        create_member_screen()
    else:
        create_final_screen()



# Cria a tela inicial
create_initial_screen()

# Inicia o loop principal da janela
root.mainloop()
