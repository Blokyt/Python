from random import *
from tkinter import *

window = Tk()
window.title("LoL")
window.iconbitmap("assets/icon.ico")

var_manage_entry = ""

def storage():
    with open('assets/lists/champ_list.txt', 'w') as f:
        for item in champ_list:
            f.write(f'{item}\n')

    with open('assets/lists/game_mode_list.txt', 'w') as f:
        for item in game_mode_list:
            f.write(f'{item}\n')

    with open('assets/lists/player_list.txt', 'w') as f:
        for item in player_list:
            f.write(f'{item}\n')

def reset(list):
    global champ_list, game_mode_list, player_list
    if list == champ_list :
        champ_fichier = open("assets/lists/champ_list.txt", "w")
        champ_fichier.close()
        champ_list = []
    elif list == game_mode_list :
        mode_fichier = open("assets/lists/game_mode_list.txt", "w")
        mode_fichier.close()
        game_mode_list = []
    elif list == player_list :
        player_fichier = open("assets/lists/player_list.txt", "w")
        player_fichier.close()
        player_list = []

    manage_entry.delete(0, END)
    random_entry.delete(0, END)

with open('assets/lists/champ_list.txt', 'a') as f:
    f.close()
with open('assets/lists/game_mode_list.txt', 'a') as f:
    f.close()

with open('assets/lists/player_list.txt', 'a') as f:
    f.close()

with open('assets/lists/champ_list.txt', 'r') as f:
    champ_list = f.read().splitlines()
    f.close()
with open('assets/lists/game_mode_list.txt', 'r') as f:
    game_mode_list = f.read().splitlines()
    f.close()

with open('assets/lists/player_list.txt', 'r') as f:
    player_list = f.read().splitlines()
    f.close()

liste_managing = champ_list

def list(list):
    global liste_managing
    random_entry.delete(0, END)
    liste_managing = list
    choice = choices(list)
    random_entry.insert(0, choice)
    print(list)

def suppr(list):
        del list[list.index(manage_entry.get())]
        manage_entry.delete(0, END)
        storage()

def add(list):
        list.append(manage_entry.get())
        manage_entry.delete(0, END)
        storage()

big_frame = Frame(bg="#666666")
big_frame.pack(expand=YES)

button_add = Button(big_frame,width=7, text="+",bg="#999999", command= lambda:add(liste_managing))
button_add.grid(column = 0, row = 1, pady=5,padx=5)

button_suppr = Button(big_frame,width=7, text="-",bg="#999999" ,command= lambda:suppr(liste_managing))
button_suppr.grid(column = 1, row = 1, pady=5,padx=5)

button_reset = Button(big_frame,width=2, text="*",bg="#999999" ,command= lambda:reset(liste_managing))
button_reset.grid(column = 2, row = 1, pady=5,padx=5)

manage_entry = Entry(big_frame,bg="#999999", textvariable=var_manage_entry)
manage_entry.grid(column = 0, row = 0, columnspan = 3, pady=5)

random_entry = Entry(big_frame,bg="#999999")
random_entry.grid(column = 3, row = 0, columnspan = 6, pady=5)

button1 = Button(big_frame, text="champ",bg="#999999", command= lambda:list(champ_list))
button1.grid(column = 3, row = 1, pady=5,padx=5)

button2 = Button(big_frame, text="gamemode",bg="#999999", command= lambda:list(game_mode_list))
button2.grid(column = 4, row = 1, pady=5,padx=5)

button3 = Button(big_frame, text="player",bg="#999999", command= lambda:list(player_list))
button3.grid(column = 5, row = 1, pady=5,padx=5)

window.mainloop()
