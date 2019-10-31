import pygame
import random


class GameState:
    """Defines the game state variables."""
    def __init__(self):
        argent = 0
        ralentire = 1
        booster = 1
        essence_max = 2000
        vitesse = 1
        rotation = 1
        valeur_gems = 1
        puissance = 1
        slow_fuel = 250

    def load(self, file):
        pass

    def save(self, file):
        pass

    def print(self):
        print('argent =', self.argent)
        print('ralentire =', self.ralentire)
        print('booster =', self.booster)
        

def creation_carte(plan, herbe, terre, pierre, obsidienne, bedrock, lave, fenetre, mineur, text):
    # crée la liste pour la carte
    # (0 = herbe, 1 = terre, 2 = pierre, 3 = obsidienne, 4 = bedrock, 5 = lave)

    carte = []  # on initiallise la carte(vide)

    # place tout les block
    for i in range(32):
        carte.append(0)
    for i in range(64):
        carte.append(1)

    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 19 or n == 20:
                carte.append(2)
            else:
                carte.append(1)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20:
                carte.append(3)
            elif n == 19 or n == 18 or n == 17:
                carte.append(2)
            else:
                carte.append(1)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20:
                carte.append(3)
            elif 16 <= n <= 19:
                carte.append(2)
            else:
                carte.append(1)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20 or n == 19:
                carte.append(3)
            elif 14 <= n <= 18:
                carte.append(2)
            else:
                carte.append(1)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20:
                carte.append(4)
            elif n == 19 or n == 18 or n == 17:
                carte.append(3)
            elif 8 <= n <= 16:
                carte.append(2)
            else:
                carte.append(1)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20 or n == 19:
                carte.append(4)
            elif 15 <= n <= 18:
                carte.append(3)
            else:
                carte.append(2)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if n == 20 or n == 19 or n == 18:
                carte.append(4)
            elif 13 <= n <= 17:
                carte.append(3)
            else:
                carte.append(2)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if 17 <= n <= 20:
                carte.append(4)
            elif 11 <= n <= 16:
                carte.append(3)
            else:
                carte.append(2)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if 16 <= n <= 20:
                carte.append(4)
            elif 7 <= n <= 15:
                carte.append(3)
            else:
                carte.append(2)
    for i in range(30):
        for l in range(32):
            n = random.randint(0, 20)
            if 15 <= n <= 20:
                carte.append(4)
            else:
                carte.append(3)
    for i in range(42):
        for l in range(32):
            n = random.randint(0, 20)
            if 14 <= n <= 20:
                carte.append(4)
            else:
                carte.append(3)


    for i in range(96):
        carte.append(5)

    #  colle chaque partie de la carte sur le fond

    k = 6
    b = 0
    x = 0
    for l in range(6):
        for p in range(58):
            m = 0
            for i in range(b, b + 32):
                if carte[i] == 0:
                    plan.blit(herbe, ((m * 80), k * 80))
                if carte[i] == 1:
                    plan.blit(terre, ((m * 80), k * 80))
                if carte[i] == 2:
                    plan.blit(pierre, ((m * 80), k * 80))
                if carte[i] == 3:
                    plan.blit(obsidienne, ((m * 80), k * 80))
                if carte[i] == 4:
                    plan.blit(bedrock, ((m * 80), k * 80))
                if carte[i] == 5:
                    plan.blit(lave, ((m * 80), k * 80))
                m += 1
            k += 1
            b += 32

        # chargement
        if x == 2:
            fenetre.fill((175, 225, 255))
            mineur2 = pygame.transform.rotate(mineur, 90)
            fenetre.blit(mineur2, (780, 320))
            fenetre.blit(text.render("Loading...", 1, (0, 0, 0)), (520, 530))
            x = 3
        if x == 1:
            fenetre.fill((175, 225, 255))
            mineur2 = pygame.transform.rotate(mineur, 90)
            fenetre.blit(mineur2, (560, 320))
            fenetre.blit(text.render("Loading..", 1, (0, 0, 0)), (520, 530))
            x = 2
        if x == 0:
            fenetre.fill((175, 225, 255))
            mineur2 = pygame.transform.rotate(mineur, 90)
            fenetre.blit(mineur2, (350, 320))
            fenetre.blit(text.render("Loading.", 1, (0, 0, 0)), (520, 530))
            x = 1
        if x == 3:
            x = 0
        pygame.display.flip()

    return carte, plan

def plan_infinit(fenetre, plan, cx, cy, mineur_x):
    # permet au plan d'être infinit a droit et a gauche

    mineur_x += 1280
    if mineur_x < 0:
        mineur_x = -mineur_x
        mineur_x += 2560
        x = int(mineur_x/2560)
        x = -x
    else:
        x = int(mineur_x / 2560)
    fenetre.blit(plan, (2560 * x -2560 - cx, 0 - cy))
    fenetre.blit(plan, (2560 * x - cx, 0 - cy))


def charger(save):
    # recupère les donné de la sauvegarde selectionner

    fichier_argent = open("Sauvegarde/sauvegarde" + save + "/argent.txt", "r")
    argent = float(fichier_argent.read())
    fichier_argent.close()
    fichier_ralentire = open("Sauvegarde/sauvegarde" + save + "/ralentire.txt", "r")
    ralentire = float(fichier_ralentire.read())
    fichier_ralentire.close()
    fichier_booster = open("Sauvegarde/sauvegarde" + save + "/booster.txt", "r")
    booster = float(fichier_booster.read())
    fichier_booster.close()
    fichier_essence_max = open("Sauvegarde/sauvegarde" + save + "/essence_max.txt", "r")
    essence_max = float(fichier_essence_max.read())
    fichier_essence_max.close()
    fichier_vitesse = open("Sauvegarde/sauvegarde" + save + "/vitesse.txt", "r")
    vitesse = float(fichier_vitesse.read())
    fichier_vitesse.close()
    fichier_rotation = open("Sauvegarde/sauvegarde" + save + "/rotation.txt", "r")
    rotation = float(fichier_rotation.read())
    fichier_rotation.close()
    fichier_valeur_gems = open("Sauvegarde/sauvegarde" + save + "/valeur_gemmes.txt", "r")
    valeur_gems = float(fichier_valeur_gems.read())
    fichier_valeur_gems.close()
    fichier_puissance = open("Sauvegarde/sauvegarde" + save + "/puissance.txt", "r")
    puissance = float(fichier_puissance.read())
    fichier_puissance.close()
    fichier_slow_fuel = open("Sauvegarde/sauvegarde" + save + "/slow_fuel.txt", "r")
    slow_fuel = float(fichier_slow_fuel.read())
    fichier_slow_fuel.close()
    return argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel


def sauvegarder(save, argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel):
    # sauvegadre les donné de la partie

    fichier_argent = open("Sauvegarde/sauvegarde" + save + "/argent.txt", "w")
    fichier_argent.write(str(argent))
    fichier_argent.close()
    fichier_ralentire = open("Sauvegarde/sauvegarde" + save + "/ralentire.txt", "w")
    fichier_ralentire.write(str(ralentire))
    fichier_ralentire.close()
    fichier_booster = open("Sauvegarde/sauvegarde" + save + "/booster.txt", "w")
    fichier_booster.write(str(booster))
    fichier_booster.close()
    fichier_essence_max = open("Sauvegarde/sauvegarde" + save + "/essence_max.txt", "w")
    fichier_essence_max.write(str(essence_max))
    fichier_essence_max.close()
    fichier_vitesse = open("Sauvegarde/sauvegarde" + save + "/vitesse.txt", "w")
    fichier_vitesse.write(str(vitesse))
    fichier_vitesse.close()
    fichier_rotation = open("Sauvegarde/sauvegarde" + save + "/rotation.txt", "w")
    fichier_rotation.write(str(rotation))
    fichier_rotation.close()
    fichier_valeur_gems = open("Sauvegarde/sauvegarde" + save + "/valeur_gemmes.txt", "w")
    fichier_valeur_gems.write(str(valeur_gems))
    fichier_valeur_gems.close()
    fichier_puissance = open("Sauvegarde/sauvegarde" + save + "/puissance.txt", "w")
    fichier_puissance.write(str(puissance))
    fichier_puissance.close()
    fichier_slow_fuel = open("Sauvegarde/sauvegarde" + save + "/slow_fuel.txt", "w")
    fichier_slow_fuel.write(str(slow_fuel))
    fichier_slow_fuel.close()


def son_oiseau(oiseau1, oiseau2):
    # fait des bruitages aléatoire dans la ville

    son = random.randint(1, 1800)

    if son == 1:
        oiseau1.play()
    if son == 2:
        oiseau2.play()

if __name__ == '__main__':
    print('testing')

    state = GameState()
    state.print()