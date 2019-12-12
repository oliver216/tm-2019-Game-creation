import pygame
import random


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
    # Recupère les donné de la sauvegarde selectionné

    save_file = open("Save/save" + save + ".txt", "r")

    argent = float(save_file.readline())
    ralentire = float(save_file.readline())
    booster = float(save_file.readline())
    essence_max = float(save_file.readline())
    vitesse = float(save_file.readline())
    rotation = float(save_file.readline())
    valeur_gems = float(save_file.readline())
    puissance = float(save_file.readline())
    slow_fuel = float(save_file.readline())
    save_file.close()

    return argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel


def sauvegarder(save, argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel):
    # sauvegadre les donné de la partie

    save_file = open("Save/save" + save + ".txt", "w")

    save_file.write(str(argent)+"\n"+str(ralentire)+"\n"+str(booster)+"\n"+str(essence_max)+"\n"+str(vitesse)+"\n"+
                    str(rotation)+"\n"+str(valeur_gems)+"\n"+str(puissance)+"\n"+str(slow_fuel))
    save_file.close()


def son_oiseau(oiseau1, oiseau2):
    # fait des bruitages aléatoire dans la ville

    son = random.randint(1, 1800)

    if son == 1:
        oiseau1.play()
    if son == 2:
        oiseau2.play()
