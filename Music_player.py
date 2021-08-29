from tkinter import *
from sys import exit
import pygame
from pygame.constants import QUIT

# Configurações da tela
janela = Tk()
janela.title("Player musical")
janela.configure(bg="black")

# Lista com todas as músicas
songs = ['Lovely (Liu Remix).mp3', 'mywar.mpeg', 'snkop2.mpeg', 'snkop3.mpeg',
 'snkop5.mpeg', 'we are young.mp3', 'Lorde - Team.mp3',
 'The Neighbourhood - Sweater Weather (Official Video).mp3',
 'Capital Cities - Safe And Sound (Official Music Video).mp3',
 'twenty one pilots - Ride (Official Video).mp3', 'Aaron Smith - Dancin (KRONO Remix).mp3',]
number = 0
volume = 1


# Inicia as músicas
def music_r_play_songs_onclick():
    pygame.mixer.init()
    pygame.mixer.music.load(songs[number])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
   

# Passar uma música
def bt_passar_onclick():
    global number
    number = number + 1
    if number == len(songs) + 1:
        number = 0
    
    pygame.mixer.init()
    pygame.mixer.music.load(songs[number])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    
   
# Voltar uma música
def bt_voltar_onclick():
    global number
    number = number - 1
    if number == len(songs) - 1:
        number = 3

    pygame.mixer.init()
    pygame.mixer.music.load(songs[number])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


# Botão de sair do pause
def bt_play_onclick():
    pygame.mixer.music.unpause()


# Botão de pause
def bt_pause_onclick():
    pygame.mixer.music.pause()


# Aumentar o volume
def bt_volume_mais_onclick():
    global volume
    volume = volume + 0.5
    pygame.mixer.music.set_volume(volume)
    print(volume)


# Diminuir o volume
def bt_volume_menos_onclick():
    global volume
    volume = volume - 0.5
    pygame.mixer.music.set_volume(volume)
    print(volume)
    print(volume)


# Criando os botões
# Borda geral
borda_nome = PhotoImage(file="borda_geral.png")
borda_nome_image = Label(janela, image=borda_nome, bd=0, bg="black")
borda_nome_image.place(x=10, y=10)

# logo nome do programa
logo_spotiry = PhotoImage(file='rmp_logo.png')
logo_spotiry_image = Label(janela, image=logo_spotiry, bd=0)
logo_spotiry_image.place(x=20, y=20)

# Borda dos botões
borda = PhotoImage(file="music_borda.png")
borda_image = Label(janela, image=borda, bd=0, bg="black")
borda_image.place(x=20, y=337)

# Botão de play
bt_play = Button(janela, bg="black", fg="grey", text="PLAY", width=15, height=3, command=bt_play_onclick)
bt_play.place(x=30, y=400)

# Botão de pause
bt_pause = Button(janela, bg="black", fg="grey", text="PAUSE", width=15, height=3, command=bt_pause_onclick)
bt_pause.place(x=156, y=400)

# Botão de voltar
bt_voltar = Button(janela, bg='black', fg='grey', text='  <--  ', width=10, command=bt_voltar_onclick)
bt_voltar.place(x=30, y=365)

# Botão de passar
bt_passar = Button(janela, bg='black', fg='grey', text='  -->  ', width=10, command=bt_passar_onclick)
bt_passar.place(x=191, y=365)

# Botão de aumentar o volume
bt_volume_mais = Button(janela, bg='black', fg='grey', text=" + ", width=3, command=bt_volume_mais_onclick)
bt_volume_mais.place(x=114, y=365)

# Botão de diminuir o volume
bt_volume_menos = Button(janela, bg='black', fg='grey', text=" - ", width=3, command=bt_volume_menos_onclick)
bt_volume_menos.place(x=156, y=365)

# Botão/logo de inicializar as músicas
music_r = PhotoImage(file="music_r.png")
music_r_play_songs = Button(
    janela, image=music_r, bd=0, bg="black", fg='black', command=music_r_play_songs_onclick)
music_r_play_songs.place(x=30, y=60)

janela.geometry("300x500+0+0")
mainloop()