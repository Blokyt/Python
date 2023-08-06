
# ---------------------------------------------------------------

# starting_inventory = ["sword","potion","wood","picaxe"]
# inventory = starting_inventory.copy()
# loot = ["diamond_sword","patate","bread"]
#
# def pick_loot(inventory, loot):
#     return inventory + loot
#
# inventory = pick_loot(inventory, loot)
# print(inventory)

# ---------------------------------------------------------------

# rooms = ["salle de bain", "chambre", "jacuzzi", "cuisine"]
# position = 0
#
# def room(position, rooms):
#     print (rooms[position])
#     move_player(position, rooms)
#
# def move_player(position, rooms):
#     action = input("Rentrez l'action up/down :")
#     if action == "up" and position < len(rooms) - 1 :
#         position = position + 1
#         room(position, rooms)
#     elif action == "down" and position > 0:
#         position = position - 1
#         room(position, rooms)
#     elif action == "stop" :
#         pass
#     else :
#         print("Erreur")
#         move_player(position, rooms)
#

# print (rooms[position])
# move_player(position, rooms)

# ---------------------------------------------------------------

def jeux(allumettes, allumettesrestantes, joueur):
    joueurturn = input("Combien d'allumettes voulez-vous enlevez " + joueur +" (1/2/3) ?")
    if joueurturn == "1" or joueurturn == "2" or joueurturn == "3":
        allumettesrestantes = allumettesrestantes - int(joueurturn)
        if allumettesrestantes < 1 :
            print("Vous avez perdu "+ joueur)
            pass
        else :
            if joueur == "joueur1" :
                joueur = "joueur2"
            else :
                joueur = "joueur1"

            end_turn(allumettes, allumettesrestantes, joueur)


    else :
        jeux(allumettes, allumettesrestantes, joueur)

def end_turn(allumettes, allumettesrestantes, joueur):
    print("Allumettes restantes :")
    print(allumettesrestantes)
    jeux(allumettes, allumettesrestantes, joueur)

joueur = "joueur1"
allumettes = int(input("Entrer le nombre d'allumettes pour cette partie :"))
allumettesrestantes = allumettes
jeux(allumettes, allumettesrestantes, joueur);

# fois = 0
# personnage = ""
# listepersonnage = []
# while True :
#     choix = int(input("\nEntrez un nombre entre 0 et 2 : "))
#     print("\nChoix : %s" %str(choix))
#     if choix == 0 :
#         print("FIN\n")
#         break
#
#     elif choix == 1 :
#         fois = fois + 1
#         print("Vous avez fait ce choix %d fois" %fois )
#         continue
#
#     elif choix == 2 :
#         personnage = input("Entrez le nom d'un personnage celebre : ")
#         listepersonnage.append(personnage)
#         for persos in listepersonnage :
#             tableauperso = "\n %d : %s" %(listepersonnage.index(persos) + 1, persos)
#             print(tableauperso)
#
#     else:
#         print("Apprends à lire les consignes connard ! \n")

# ---------------------------------------------------------------

# dico = {}
#
# while True:
#     objet = input("\nQuel objet : ")
#     count = int(input("\nCombien ? : "))
#     if objet == "stop" :
#         break
#     if not objet in dico :
#         dico[objet] = count
#         print("\n%s\n"%dico)
#         continue
#     if objet in dico :
#         currentcount = dico[objet]
#         dico[objet] = count + currentcount
#         print("\n%s"%dico)

# ---------------------------------------------------------------

# from random import *
#
# def menu() :
#
#     print("\n1 : Addition \n2 : Multiplication\n3 : Exit")
#     mode = input("\nSelectionnez le mode de jeu : ")
#     if mode == "3" :
#         return
#     print("\n1 : facile\n2 : moyen\n3 : difficile")
#     difficulty = int(input("\nSelectionnez la difficulté : "))
#
#     if difficulty < 1 :
#         difficulty = 1
#     elif difficulty > 3 :
#         difficulty = 3
#
#     if mode == "1" :
#         game_mode = "+"
#         test(game_mode, difficulty)
#     elif mode == "2" :
#         game_mode = "x"
#         test(game_mode, difficulty)
#     else :
#         menu()
#
# def test(game_mode, difficulty) :
#     reponses = {}
#     min = difficulty
#     max = difficulty * 5
#     i = 0
#     bonnerep = 0
#     n = int(input("Nombres de calculs durant ce test : "))
#     if n == 0 :
#         print("\nTricheur\n")
#         n = 15
#         min = 3
#         max = 15
#     while i < n:
#         a = randint(min, max)
#         b = randint(min, max)
#         reponse = int(input(str(a)+game_mode+str(b)+" : "))
#         if game_mode == "+" :
#             if reponse == a + b :
#                 bonnerep = bonnerep + 1
#                 reponses[str(a)+game_mode+str(b)] = reponse, "vrai"
#
#             else :
#                 reponses[str(a)+game_mode+str(b)] = reponse, "faux"
#
#         elif game_mode == "x" :
#             if reponse == a * b :
#                 bonnerep = bonnerep + 1
#                 reponses[str(a)+game_mode+str(b)] = reponse, "vrai"
#
#             else :
#                 reponses[str(a)+game_mode+str(b)] = reponse, "faux"
#
#
#
#         i += 1
#
#     result(bonnerep, n, reponses)
#
# def result(bonnerep, n, reponses) :
#     result = bonnerep / n * 100
#     print("\n"+str(result)+"% de bonnes réponses\n")
#     print(reponses)
#     menu()
#
# menu()

# ---------------------------------------------------------------

# from random import *
#
# champ_list = ["1"]
# game_mode_list = ["1"]
# player_list = ["1"]
#
#
# def random_list(list):
#     choice = choices(list)
#     print("\n"+str(choice)+"\n")
#
# def modify(list):
#     print("\n"+str(list))
#     modif = input("\nEntrez ce que vous voulez ajouter/supprimer à cette liste : ")
#     print("\n1 : add\n2 : suppr")
#     add_suppr = int(input("\nChoississez l'action : "))
#     if add_suppr == 1 :
#         list.append(modif)
#         print ("\n"+str(list)+"\n")
#     elif add_suppr == 2 and modif in list:
#         del list[list.index(modif)]
#         print ("\n"+str(list)+"\n")
#
#
# while True :
#     print(champ_list, game_mode_list, player_list)
#     print("\n1 : Random_Champ\n2 : Random_Game_Mode\n3 : Random_Player")
#     choix_list = (input("\nChoisissez le mode : "))
#     print("\n1 : Random\n2 : modify")
#     mode = int(input("\nChoisissez l'action : "))
#     if choix_list == "stop" :
#         break
#     elif int(choix_list) == 1 :
#         if mode == 1 :
#             random_list(champ_list)
#         if mode == 2 :
#             modify(champ_list)
#     elif int(choix_list) == 2 :
#         if mode == 1 :
#             random_list(game_mode_list)
#         if mode == 2 :
#             modify(game_mode_list)
#     elif int(choix_list) == 3 :
#         if mode == 1 :
#             random_list(player_list)
#         if mode == 2 :
#             modify(player_list)

# ---------------------------------------------------------------

# from random import *
# from tkinter import *
#
# window = Tk()
# window.title("LoL")
# window.iconbitmap("icone.ico")
#
# var_manage_entry = ""
#
# champ_list = ["1"]
# game_mode_list = ["2"]
# player_list = ["3"]
#
# liste_managing = champ_list
#
# def list(list):
#     global liste_managing
#     random_entry.delete(0, END)
#     liste_managing = list
#     choice = choices(list)
#     random_entry.insert(0, choice)
#     print(list)
#
# def suppr(list):
#         del list[list.index(manage_entry.get())]
#         manage_entry.delete(0, END)
#
# def add(list):
#         list.append(manage_entry.get())
#         manage_entry.delete(0, END)
#
#
#
#
#
#
# big_frame = Frame(bg="#666666")
# big_frame.pack(expand=YES)
#
# button_add = Button(big_frame,width=8, text="+",bg="#999999", command= lambda:add(liste_managing))
# button_add.grid(column = 0, row = 1, pady=5,padx=5)
#
# button_suppr = Button(big_frame,width=8, text="-",bg="#999999" ,command= lambda:suppr(liste_managing))
# button_suppr.grid(column = 1, row = 1, pady=5,padx=5)
#
# manage_entry = Entry(big_frame,bg="#999999", textvariable=var_manage_entry)
# manage_entry.grid(column = 0, row = 0, columnspan = 2, pady=5)
#
# random_entry = Entry(big_frame,bg="#999999")
# random_entry.grid(column = 2, row = 0, columnspan = 5, pady=5)
#
# button1 = Button(big_frame, text="champ",bg="#999999", command= lambda:list(champ_list))
# button1.grid(column = 2, row = 1, pady=5,padx=5)
#
# button2 = Button(big_frame, text="gamemode",bg="#999999", command= lambda:list(game_mode_list))
# button2.grid(column = 3, row = 1, pady=5,padx=5)
#
# button3 = Button(big_frame, text="player",bg="#999999", command= lambda:list(player_list))
# button3.grid(column = 4, row = 1, pady=5,padx=5)
#
# window.mainloop()

# ---------------------------------------------------------------

# class Player():
#     health = 10
#     caracters_list = []
#     all_actions = {}
#
#     def __init__(self, name):
#         self.attack_damage = 2
#         self.velocity = 5
#         self.name = name
#         self.caracters_list.append(name)
#         self.__spawn()
#
#     def __spawn(self):
#         print("\n"+self.name+" has spawned")
#
#     def fight(self, enemy):
#         enemy.health = enemy.health - self.attack_damage
#         result = (str(self.name)+" attaque "+str(enemy.name)+", "+str(enemy.name)+" perd "+str(self.attack_damage)+" hp, il lui reste maintenant "+str(enemy.health)+" hp !")
#         print("\n"+result)
#         self.actions_storage("fight")
#
#     def soin(self, soin):
#         self.health = self.health + soin
#         result = (str(self.name)+" prend un pack de soin, il récupère donc 1 hp, il a maintenant "+str(self.health)+" hp !")
#         print("\n"+result)
#         self.actions_storage("soin")
#
#     def faim(self):
#         print("\nJ'ai tellement faim que je pourrais manger n'importe quoi !")
#
#     def display_caracters_list(self):
#         print(self.caracters_list)
#
#     def actions_storage(self, action):
#         if not action in self.all_actions:
#             self.all_actions[self.name+"_"+action] = 1
#         else :
#             self.all_actions[self.name+"_"+action] = self.all_actions[self.name+"_"+action] + 1
#
#     def display_all_actions(self):
#         print("\n"+str(self.all_actions))
#
#
# Jimmy = Player("Jimmy")
# Bobby = Player("Bobby")
# Game_Master = Player("Master")
#
#
# Jimmy.fight(Bobby)
#
# Bobby.soin(2)
#
# Bobby.faim()
#
# Game_Master.display_all_actions()

# ---------------------------------------------------------------
