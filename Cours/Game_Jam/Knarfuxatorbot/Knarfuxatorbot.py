
# module random

from random import *

# module colored

from colored import *

color = fg('cyan')
color2 = fg('green')
color3 = fg('red')
color4 = fg(172)
reset = attr('reset')

#variable while
running = True

class Room():

    # variable pour les différentes instance des pièces

    list_rooms = []
    list_escalier = []

    # definitions des différentes propriétées

    def __init__(self, name, dechets, desc):
        self.dechets = dechets
        self.name = name
        self.description = desc

        #permet d'identifer les escalier

        if self.dechets :
            self.propre = False
            self.escalier = False
        else :
            self.propre = True
            self.escalier = True
            self.list_escalier.append(self.name)

        # création de la liste des piece en evitant que les escalier sois aux extremités

        self.list_rooms.append(self)
        shuffle(self.list_rooms)
        while not self.list_rooms[0].dechets or not self.list_rooms[-1].dechets or any(self.list_rooms[i].dechets==self.list_rooms[i+1].dechets for i in range(len(self.list_rooms)-1)) :
            shuffle(self.list_rooms)

    def display_desc(self):

        #en fonction du dechet lui attribuer une couleur

        for dechets in self.dechets :
            if dechets == "chat" :
                self.description = self.description.replace(dechets, color4+dechets+reset)
            else :
                self.description = self.description.replace(dechets, color3+dechets+reset)

        if self.name in self.list_escalier :
            self.description = self.description.replace("Escalier", color+"Escalier"+reset)
        else :
            self.description = self.description.replace(self.name, color+self.name+reset)
        print("\n"+self.description)
        input("\n > ")

    def enlever_dechet(self):

        #si list de dechets rempli

        if self.dechets :
            print("\n Quel "+color3+"dechet"+reset+" voulez-vous ramasser ? ")

            #demande le dechet à enlever à l'utilisateur

            dechet_choisi = input("\n > ")

            # verifie si il est dans la list des dechets

            if dechet_choisi in self.dechets :

                #si oui et si c'est un chat

                if dechet_choisi == "chat":

                    print("\n "+color3+"Vous avez declenché un combat contre le chat !"+reset)

                    #generation des capacité du chat

                    Chat_dangeureux.hp = randint(30, 80)
                    Chat_dangeureux.attack_damage = randint(3, 8)

                    #lancement du combat

                    Robot.combat(robot_aspirateur, Chat_dangeureux)

                    #après le combat si le chat à perdu

                    if Chat_dangeureux.hp <= 0 :
                        del self.dechets[self.dechets.index("chat")]
                        self.description = self.description.replace(dechet_choisi, color+dechet_choisi+color2+" carbonisé"+reset)
                        robot_aspirateur.score += 5

                        # si plus de dechet changer l'etat de la piece

                        if not self.dechets :
                            print("\n "+color2+"Pièce nettoyé !"+reset)
                            self.description = " "+color2+"Pièce nettoyé"+reset
                            self.propre = True
                            input("\n > ")


                else :

                    for dechets in self.dechets :

                        #si ce n'est pas un chatalors le supprimer de la liste

                        if dechet_choisi == dechets :
                            print("\n "+color+dechets+color2+" nettoyé !"+reset)
                            del self.dechets[self.dechets.index(dechets)]
                            self.description = self.description.replace(dechets, color+dechets+color2+" nettoyé"+reset)
                            robot_aspirateur.score += 5

                            # si il n'y a plus de dechets changer la desc et la variable booléene

                            if not self.dechets :
                                print("\n "+color2+"Pièce nettoyé !"+reset)
                                self.description = " "+color2+"Pièce nettoyé"+reset
                                self.propre = True
                                input("\n > ")

                            # si il reste encore des dechets demander à l'utilisateur s'il veut les ramasser

                            else :
                                print("\n Il reste des dechets, voulez-vous les ramasser (yes/no) ?")
                                reponse = input("\n > ")
                                if reponse == "yes":
                                    self.enlever_dechet()

            else :
                print("\n Ce dechet n'est pas présent dans cette pièce")
                input("\n > ")

        # sinon notifié qu'elle est propre

        else :
            print("\n "+color2+"Pièce propre"+reset)
            input("\n > ")

#création des instances des pièces

Room1 = Room(  "Salle de bain",  ["poils de chat","bol de chocapique"],          " Salle de bain : Il y a plein de poils de chat sur le sol et , on dirai que quelqu'un à fait tomber un bol de chocapique par ici , c'est fou !")
Room2 = Room(  "Salle à manger", ["poussières","chat"],                          " Salle à manger : Juste quelque poussières ici, oh et un chat .")
Room3 = Room(  "Chambre",        ["paquets de chips","chaussettes qui puent"],   " Chambre : Ce bureau est rempli de paquets de chips on dirai la chambre de mon frère, oh et en plus y'a des chaussettes qui puent mais à un point, c'est ouf !")
Room4 = Room(  "SalonTV",        ["popcorns","trace"],                           " SalonTV : Pourquoi y'a des popcorns partout , et, heu.., c'est quoi la trace la sur le canapé ...")
Room5 = Room(  "Cuisine",        ["poêles","couverts"] ,                         " Cuisine : Les poêles sont vraiment sales, et les couverts aussi surtout celui la avec ... de la mayo et du ...")
Room6 = Room(  "Toillete",       ["ce"] ,                                        " Toilette : Je préfère pas vous dire ce que je vois là .")
Room7 = Room(  "Grenier",        ["poussières"],                                 " Grenier : Y'a tellement de poussières que je peut meme pas voir si il y a d'autres dechets !" )

Room8 = Room(   "Escalier1",[],    " Escalier : rien à nettoyer")
Room9 = Room(   "Escalier2",[],    " Escalier : rien à nettoyer")

class Robot():

    # variable de la postion du robot

    position = randint(0,len(Room.list_rooms)-1)

    # propriété du robot

    def __init__(self, name):
        with(open("score.txt", "a")) as file :
            file.close()
        with(open("score.txt", "r")) as file :
            if not file.read() :
                with(open("score.txt", "w")) as file :
                    file.write(str(0))
                    file.close()
            else :
                file.close()

        self.name = name
        self.hpmax = 100
        self.hp = 100
        self.attack_damage = 10
        self.attaque1 = "\n Le chat a esquivé l'attaque !"
        self.attaque2 = "\n Aspiration réussi !"
        self.attaque3 = "\n Toupie effectué, c'est très efficace !"
        self.score = 0
        with(open("score.txt", "r")) as file :
            self.highscore = file.read()

    #affichage de l'emplacement des pieces

    def display_room(self):
        list_piece = []

        for room in Room.list_rooms :
            list_piece.append(room.name)

        #si la piece est nettoyer l'afficher en vert / si c'est un escalier l'afficher en orange / si c'est la piece dans la quelle tu est l'afficher en bleu

        for room in Room.list_rooms :

            #vert

            if room.propre == True and not list_piece[self.position] == room.name and room.escalier == False :
                list_piece[list_piece.index(room.name)] = color2+str(room.name)+reset

            #orange

            elif room.propre == True and not list_piece[self.position] == room.name and room.escalier == True :
                list_piece[list_piece.index(room.name)] = "\n | "+color4+"Escalier"+reset+" | \n"

        #bleu

        if list_piece[self.position] in Room.list_escalier :
            list_piece[self.position] = color+">> Escalier <<"+reset
        else :
            list_piece[self.position] = color+">> "+list_piece[self.position]+" <<"+reset

        #afficher

        list_piece = "\n | "+" | ".join(list_piece)+" | "

        print(list_piece)

    def deplacement(self, list_rooms):

        #afficher les pieces

        self.display_room()

        #demander ou l'utilisateur veut aller

        print("\n "+color+"1"+reset+" : left\n "+color+"2"+reset+" : right\n "+color+"3"+reset+" : Ne pas bouger")
        direction = input("\n > ")
        if direction == "1":

            # si le joueur est au bord il va à l'autre bord

            if self.position == 0 :
                self.position = len(list_rooms)-1

            # sinon il va à gauche

            else :
                self.position = self.position - 1

            if list_rooms[self.position].escalier :
                robot_aspirateur.score -= 1

        elif direction == "2":

            # si le joueur est au bord il va à l'autre bord

            if self.position == len(list_rooms)-1 :
                self.position = 0

            # # sinon il va à droite

            else :
                self.position = self.position + 1

            if list_rooms[self.position].escalier :
                robot_aspirateur.score -= 1



        elif direction == "3" :
            pass

        else :
            print("\n" * 10)
            self.deplacement(list_rooms)

    def combat(robot, adversaire):

        #affiche les stats du chat defini précédemment et celle du robot, constantes

        print("\n Chat : "+color+str(adversaire.hp)+" hp"+reset+" | "+color+str(adversaire.attack_damage)+" ad"+reset+"\n Vous : "+color+str(robot.hp)+" hp"+reset+" | "+color+str(robot.attack_damage)+" ad"+reset)

        # tant que personne a perdu proposer des action

        while robot.hp > 0 and adversaire.hp > 0 :
            print("\n "+color+"1"+reset+" : Attaquer\n "+color+"2"+reset+" : Se soigner")
            action = input("\n > ")
            if action == "1":
                Robot.attaque(robot, adversaire, "lui")
                Robot.attaque(adversaire, robot, "vous")
            elif action == "2":
                Robot.soin(robot, "vous")
                Robot.attaque(adversaire, robot, "vous")

        #quand quelqu'un perd afficher le resultat

        else :
            if robot.hp < 0 :
                print(" "+color3+"Vous avez perdu !"+reset)
            else :
                print(" "+color2+"Vous avez gagné le combat !"+reset)

            input("\n > ")

    def attaque(attaquant, adversaire, mot):

        # choisi un nombre entre 1 et 4 et en fonction faire une attaque differentes

        chance = randint(1,4)
        if chance > 2:
            print(attaquant.attaque2)
            adversaire.hp = adversaire.hp - attaquant.attack_damage
        elif chance == 1 :
            print(attaquant.attaque1)
        elif chance == 2 :
            print(attaquant.attaque3)
            adversaire.hp = adversaire.hp - attaquant.attack_damage*2

        #affiche le resultat de l'attaque

        print(" Il "+mot+" reste "+color+str(adversaire.hp)+" hp !"+reset)
        input("\n > ")

    def soin(self, mot):

        #soigne le robot

        self.hp = self.hp + 10
        if self.hp > self.hpmax :
            self.hp = self.hpmax
        print(" "+self.name+" soigné !")

        #affiche le resultat

        print(" Il "+mot+" reste "+color+str(self.hp)+" hp !"+reset)

        input("\n > ")

    def parametre(self):

        global running

        print("\n" * 10)
        print("\n "+color4+"HighScore"+reset+" : "+color+self.highscore+reset)
        print("\n "+color+"1"+reset+" : Exit\n "+color+"2"+reset+" : Règles\n "+color+"3"+reset+" : Retour")
        choix = input("\n > ")

        # Exit

        if choix == "1" :
            running = False

        # Règle

        elif choix == "2":

            print("\n Vous incarnez un "+color+"robot-aspirateur"+reset+", votre but : ")
            input("\n > ")
            print("\n "+color+"Déplacer-vous"+reset+" dans les différentes pieces de votre maison afin de les nettoyer !")
            input("\n > ")
            print("\n A chaque fois que vous "+color+"nettoyez ou gagnez des combats"+reset+" vous "+color4+"gagnez des points"+reset+" !")
            input("\n > ")
            print("\n "+color+"Prenez le chemin le plus rapide "+reset+"car à chaque fois que vous passez par un couloir ou un escalier vous"+color4+" perdez des points"+reset+" !")
            input("\n > ")
            print("\n "+color2+"Astuce"+reset+" : lorsque vous "+color+"sortez d'un coté"+reset+" de la maison vous "+color+"apparaissez de l'autre"+reset+" coté !")
            input("\n > ")
            print("\n Vous êtes dans la piece indiqué en "+color+"bleu !"+reset)
            input("\n > ")
            print("\n Certaine fois les "+color+"input"+reset+" sont là juste pour marquer un "+color+"temps d'arret"+reset+" comme actuellement, alors appuyer simplement sur ENTER pour continuer !")
            input("\n > ")
            print("\n Fier vous au "+color+"couleur"+reset+", le gameplay est intuitif !")
            input("\n > ")
            print("\n "+color2+"Bonne chance !"+reset)
            input("\n > ")

        elif choix == "3":
            print("\n" * 10)

        else :
            self.parametre()

    # demander à l'utilisateur l'action qu'il veut faire

    def action(self, list_rooms):
        if self.score > int(self.highscore) :
            self.highscore = str(self.score)
            with(open("score.txt", "w")) as file :
                file.write(str(self.highscore))
                file.close()

        global running

        #afficher les pieces

        self.display_room()

        # verifie si toutes les pieces sont "propre" et en fonction arrete ou non le jeu

        win = []
        for room in list_rooms :
            if room.propre == True :
                win.append(room.propre)
                if len(win) == len(list_rooms):
                    print(color2+"Vous avez gagner avec "+str(self.score)+" point !\n"+reset)
                    running = False

        if running == True :



            #affiche le score et les actions possibles

            print("\n "+color4+"Score"+reset+" : "+color+str(self.score)+reset)
            print("\n "+color+"1"+reset+" : Se deplacer\n "+color+"2"+reset+" : Observer\n "+color+"3"+reset+" : Ramasser\n\n "+color+"4"+reset+" : Paramètres")
            action_choisi = input("\n > ")

            # deplacement

            if action_choisi == "1":

                print("\n" * 10)

                self.deplacement(list_rooms)

            # observer la piece

            elif action_choisi == "2":

                print("\n" * 10)

                for room in list_rooms:
                    if list_rooms.index(room) == self.position :
                        room.display_desc()

            # rammasser dechet

            elif action_choisi == "3":

                print("\n" * 10)

                for room in list_rooms:
                    if list_rooms.index(room) == self.position :
                        room.enlever_dechet()

            # si l'utilisateur met "stop" alors la boucle du jeu s'arrete

            elif action_choisi == "4":
                self.parametre()

# instansiation du robot

robot_aspirateur = Robot("Knarfuxatorbot")

class Chat():

    def __init__(self, name):
        self.name = name
        self.hp = 666
        self.attack_damage = 666
        self.attaque1 = "\n Vous avez esquivé l'attaque !"
        self.attaque2 = "\n Griffure réussi !"
        self.attaque3 = "\n Le chat a sauté sur votre tête, c'est très efficace !"

#instansiation du chat

Chat_dangeureux = Chat("chat")

#lancement du jeu

while running :
    print("\n" * 10)
    robot_aspirateur.action(Room.list_rooms)
