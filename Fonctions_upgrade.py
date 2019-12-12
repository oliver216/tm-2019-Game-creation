import pygame
from pygame.locals import *


def upgrade(ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel, argent,
            surface_fenetre, petit_text, blanc, rectangle, cadre, son_ameliorer, son_error, usine):
    # tout les variable pour les améliorations du mineur + affichage de celle si

    prix_essence = ""
    valeur_essence = "max"
    message_essence = "Fuel : 40000"
    prix_vitesse = ""
    valeur_vitesse = "max"
    message_vitesse = "Speed : x2.5"
    prix_booster = ""
    valeur_booster = "max"
    message_booster = "Booster : x3"
    prix_ralentire = ""
    valeur_ralentire = "max"
    message_ralentire = "Break : x0.3"
    prix_rotation = ""
    valeur_rotation = "max"
    message_rotation = "Rotation : x3"
    prix_valeur_gems = ""
    valeur_valeur_gems = "max"
    message_valeur_gems = "Gems value : x3"
    prix_puissance = ""
    valeur_puissance = "max"
    message_puissance = "Diamond drill"
    prix_slow_fuel = ""
    valeur_slow_fuel = "max"
    message_slow_fuel = "Break's fuel : 3000"

    # le systeme d'amélioration
    if essence_max == 2000:
        prix_essence = 75
        message_essence = "Fuel : 2000 --> 3000"
        valeur_essence = "lvlup"
    if essence_max == 3000:
        prix_essence = 200
        message_essence = "Fuel : 3000 --> 4000"
        valeur_essence = "lvlup"
    if essence_max == 4000:
        prix_essence = 350
        message_essence = "Fuel : 4000 --> 5000"
        valeur_essence = "lvlup"
    if essence_max == 5000:
        prix_essence = 700
        message_essence = "Fuel : 5000 --> 6500"
        valeur_essence = "lvlup"
    if essence_max == 6500:
        prix_essence = 1200
        message_essence = "Fuel : 6500 --> 9000"
        valeur_essence = "lvlup"
    if essence_max == 9000:
        prix_essence = 1800
        message_essence = "Fuel : 9000 --> 12000"
        valeur_essence = "lvlup"
    if essence_max == 12000:
        prix_essence = 2600
        message_essence = "Fuel : 12000 --> 15000"
        valeur_essence = "lvlup"
    if essence_max == 15000:
        prix_essence = 4500
        message_essence = "Fuel : 15000 --> 20000"
        valeur_essence = "lvlup"
    if essence_max == 20000:
        prix_essence = 10000
        message_essence = "Fuel : 20000 --> 40000"
        valeur_essence = "lvlup"

    if vitesse == 1:
        prix_vitesse = 100
        message_vitesse = "Speed : x1 --> x1.2"
        valeur_vitesse = "lvlup"
    if vitesse == 1.2:
        prix_vitesse = 500
        message_vitesse = "Speed : x1.2 --> x1.4"
        valeur_vitesse = "lvlup"
    if vitesse == 1.4:
        prix_vitesse = 1200
        message_vitesse = "Speed : x1.4 --> x1.6"
        valeur_vitesse = "lvlup"
    if vitesse == 1.6:
        prix_vitesse = 2000
        message_vitesse = "Speed : x1.6 --> x1.8"
        valeur_vitesse = "lvlup"
    if vitesse == 1.8:
        prix_vitesse = 3200
        message_vitesse = "Speed : x1.8 --> x2"
        valeur_vitesse = "lvlup"
    if vitesse == 2:
        prix_vitesse = 6000
        message_vitesse = "Speed : x2 --> x2.5"
        valeur_vitesse = "lvlup"

    if booster == 1:
        prix_booster = 150
        message_booster = "booster : x1 --> x1.3"
        valeur_booster = "buy"
    if booster == 1.3:
        prix_booster = 400
        message_booster = "booster : x1.3 --> x1.6"
        valeur_booster = "lvlup"
    if booster == 1.6:
        prix_booster = 750
        message_booster = "booster : x1.6 --> x2"
        valeur_booster = "lvlup"
    if booster == 2:
        prix_booster = 1500
        message_booster = "booster : x2 --> x2.5"
        valeur_booster = "lvlup"
    if booster == 2.5:
        prix_booster = 2500
        message_booster = "booster : x2.5 --> x3"
        valeur_booster = "lvlup"

    if ralentire == 1:
        prix_ralentire = 200
        message_ralentire = "Break : x1 --> x0.8"
        valeur_ralentire = "buy"
    if ralentire == 0.8:
        prix_ralentire = 500
        message_ralentire = "Break : x0.8 --> x0.65"
        valeur_ralentire = "lvlup"
    if ralentire == 0.65:
        prix_ralentire = 1200
        message_ralentire = "Break : x0.65 --> x0.5"
        valeur_ralentire = "lvlup"
    if ralentire == 0.5:
        prix_ralentire = 2800
        message_ralentire = "Break : x0.5 --> x0.4"
        valeur_ralentire = "lvlup"
    if ralentire == 0.4:
        prix_ralentire = 4000
        message_ralentire = "Break : x0.4 --> x0.3"
        valeur_ralentire = "lvlup"

    if rotation == 1:
        prix_rotation = 120
        message_rotation = "Rotation : x1 --> x1.2"
        valeur_rotation = "lvlup"
    if rotation == 1.2:
        prix_rotation = 250
        message_rotation = "Rotation : x1.2 --> x1.5"
        valeur_rotation = "lvlup"
    if rotation == 1.5:
        prix_rotation = 600
        message_rotation = "Rotation : x1.5 --> x1.8"
        valeur_rotation = "lvlup"
    if rotation == 1.8:
        prix_rotation = 1000
        message_rotation = "Rotation : x1.8 --> x2.2"
        valeur_rotation = "lvlup"
    if rotation == 2.2:
        prix_rotation = 1800
        message_rotation = "Rotation : x2.2 --> x2.6"
        valeur_rotation = "lvlup"
    if rotation == 2.6:
        prix_rotation = 2600
        message_rotation = "Rotation : x2.6 --> x3"
        valeur_rotation = "lvlup"

    if valeur_gems == 1:
        prix_valeur_gems = 400
        message_valeur_gems = "Gems value : x1 --> x1.5"
        valeur_valeur_gems = "lvlup"
    if valeur_gems == 1.5:
        prix_valeur_gems = 1200
        message_valeur_gems = "Gems value : x1.5 --> x2"
        valeur_valeur_gems = "lvlup"
    if valeur_gems == 2:
        prix_valeur_gems = 2200
        message_valeur_gems = "Gems value : x2 --> x2.5"
        valeur_valeur_gems = "lvlup"
    if valeur_gems == 2.5:
        prix_valeur_gems = 4000
        message_valeur_gems = "Gems value : x2.5 --> x3"
        valeur_valeur_gems = "lvlup"

    if slow_fuel == 250:
        prix_slow_fuel = 250
        message_slow_fuel = "Break's fuel : 250 --> 400"
        valeur_slow_fuel = "lvlup"
    if slow_fuel == 400:
        prix_slow_fuel = 500
        message_slow_fuel = "Break's fuel : 400 --> 700"
        valeur_slow_fuel = "lvlup"
    if slow_fuel == 700:
        prix_slow_fuel = 1500
        message_slow_fuel = "Break's fuel : 700 --> 1200"
        valeur_slow_fuel = "lvlup"
    if slow_fuel == 1200:
        prix_slow_fuel = 3000
        message_slow_fuel = "Break's fuel : 1200 --> 1600"
        valeur_slow_fuel = "lvlup"
    if slow_fuel == 1600:
        prix_slow_fuel = 4500
        message_slow_fuel = "Break's fuel : 1600 --> 2000"
        valeur_slow_fuel = "lvlup"
    if slow_fuel == 2000:
        prix_slow_fuel = 6000
        message_slow_fuel = "Break's fuel : 2000 --> 3000"
        valeur_slow_fuel = "lvlup"

    if puissance == 1:
        prix_puissance = 3000
        message_puissance = "Steel drill (stone)"
        valeur_puissance = "buy"
    if puissance == 2:
        prix_puissance = 8000
        message_puissance = "Diamond drill (obsidian)"
        valeur_puissance = "buy"

    # système graphique des panneaus d'amélioration pour les deux usine
    if usine == 1:
        surface_fenetre.blit(cadre, (500, 50))
        surface_fenetre.blit(rectangle, (608, 77))
        surface_fenetre.blit(petit_text.render(str(prix_essence), 1, blanc), (540, 82))
        surface_fenetre.blit(petit_text.render(str(valeur_essence), 1, blanc), (610, 82))
        surface_fenetre.blit(petit_text.render(str(message_essence), 1, blanc), (690, 82))
        surface_fenetre.blit(rectangle, (608, 130))
        surface_fenetre.blit(petit_text.render(str(prix_vitesse), 1, blanc), (540, 135))
        surface_fenetre.blit(petit_text.render(str(valeur_vitesse), 1, blanc), (610, 135))
        surface_fenetre.blit(petit_text.render(str(message_vitesse), 1, blanc), (690, 135))
        surface_fenetre.blit(rectangle, (608, 183))
        surface_fenetre.blit(petit_text.render(str(prix_rotation), 1, blanc), (540, 188))
        surface_fenetre.blit(petit_text.render(str(valeur_rotation), 1, blanc), (610, 188))
        surface_fenetre.blit(petit_text.render(str(message_rotation), 1, blanc), (690, 188))
        surface_fenetre.blit(rectangle, (608, 236))
        surface_fenetre.blit(petit_text.render(str(prix_valeur_gems), 1, blanc), (540, 241))
        surface_fenetre.blit(petit_text.render(str(valeur_valeur_gems), 1, blanc), (610, 241))
        surface_fenetre.blit(petit_text.render(str(message_valeur_gems), 1, blanc), (690, 241))

    if usine == 2:
        surface_fenetre.blit(cadre, (300, 50))
        surface_fenetre.blit(rectangle, (408, 77))
        surface_fenetre.blit(petit_text.render(str(prix_booster), 1, blanc), (340, 82))
        surface_fenetre.blit(petit_text.render(str(valeur_booster), 1, blanc), (410, 82))
        surface_fenetre.blit(petit_text.render(str(message_booster), 1, blanc), (490, 82))
        surface_fenetre.blit(rectangle, (408, 130))
        surface_fenetre.blit(petit_text.render(str(prix_ralentire), 1, blanc), (340, 135))
        surface_fenetre.blit(petit_text.render(str(valeur_ralentire), 1, blanc), (410, 135))
        surface_fenetre.blit(petit_text.render(str(message_ralentire), 1, blanc), (490, 135))
        surface_fenetre.blit(rectangle, (408, 183))
        surface_fenetre.blit(petit_text.render(str(prix_slow_fuel), 1, blanc), (340, 188))
        surface_fenetre.blit(petit_text.render(str(valeur_slow_fuel), 1, blanc), (410, 188))
        surface_fenetre.blit(petit_text.render(str(message_slow_fuel), 1, blanc), (490, 188))
        surface_fenetre.blit(rectangle, (408, 236))
        surface_fenetre.blit(petit_text.render(str(prix_puissance), 1, blanc), (340, 241))
        surface_fenetre.blit(petit_text.render(str(valeur_puissance), 1, blanc), (410, 241))
        surface_fenetre.blit(petit_text.render(str(message_puissance), 1, blanc), (490, 241))

    quitter = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            quitter = 2
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter = 2
            else:
                quitter = 1
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if usine == 1:
                if 500 < event.pos[0] < 1080 and 50 < event.pos[1] < 300:
                    if 608 < event.pos[0] < 673 and 77 < event.pos[1] < 107 and prix_essence != "":
                        if prix_essence <= argent:
                            son_ameliorer.play()
                            if essence_max == 20000:
                                essence_max = 40000
                                argent -= 10000
                            if essence_max == 15000:
                                essence_max = 20000
                                argent -= 4500
                            if essence_max == 12000:
                                essence_max = 15000
                                argent -= 2600
                            if essence_max == 9000:
                                essence_max = 12000
                                argent -= 1800
                            if essence_max == 6500:
                                essence_max = 9000
                                argent -= 1200
                            if essence_max == 5000:
                                essence_max = 6500
                                argent -= 700
                            if essence_max == 4000:
                                essence_max = 5000
                                argent -= 350
                            if essence_max == 3000:
                                essence_max = 4000
                                argent -= 200
                            if essence_max == 2000:
                                essence_max = 3000
                                argent -= 75
                        else:
                            son_error.play()
                    if 608 < event.pos[0] < 673 and 130 < event.pos[1] < 160 and prix_vitesse != "":
                        if prix_vitesse <= argent:
                            son_ameliorer.play()
                            if vitesse == 2:
                                vitesse = 2.5
                                argent -= 6000
                            if vitesse == 1.8:
                                vitesse = 2
                                argent -= 3200
                            if vitesse == 1.6:
                                vitesse = 1.8
                                argent -= 2000
                            if vitesse == 1.4:
                                vitesse = 1.6
                                argent -= 1200
                            if vitesse == 1.2:
                                vitesse = 1.4
                                argent -= 500
                            if vitesse == 1:
                                vitesse = 1.2
                                argent -= 100
                        else:
                            son_error.play()
                    if 608 < event.pos[0] < 673 and 187 < event.pos[1] < 217 and prix_rotation != "":
                        if prix_rotation <= argent:
                            son_ameliorer.play()
                            if rotation == 2.6:
                                rotation = 3
                                argent -= 2600
                            if rotation == 2.2:
                                rotation = 2.6
                                argent -= 1800
                            if rotation == 1.8:
                                rotation = 2.2
                                argent -= 1000
                            if rotation == 1.5:
                                rotation = 1.8
                                argent -= 600
                            if rotation == 1.2:
                                rotation = 1.5
                                argent -= 250
                            if rotation == 1:
                                rotation = 1.2
                                argent -= 120
                        else:
                            son_error.play()
                    if 608 < event.pos[0] < 673 and 240 < event.pos[1] < 270 and prix_valeur_gems != "":
                        if prix_valeur_gems <= argent:
                            son_ameliorer.play()
                            if valeur_gems == 2.5:
                                valeur_gems = 3
                                argent -= 4000
                            if valeur_gems == 2:
                                valeur_gems = 2.5
                                argent -= 2200
                            if valeur_gems == 1.5:
                                valeur_gems = 2
                                argent -= 1200
                            if valeur_gems == 1:
                                valeur_gems = 1.5
                                argent -= 400
                        else:
                            son_error.play()
                else:
                    usine = 0
            if usine == 2:
                if 301 < event.pos[0] < 880 and 50 < event.pos[1] < 300:
                    if 408 < event.pos[0] < 473 and 77 < event.pos[1] < 107 and prix_booster != "":
                        if prix_booster <= argent:
                            son_ameliorer.play()
                            if booster == 2.5:
                                booster = 3
                                argent -= 2500
                            if booster == 2:
                                booster = 2.5
                                argent -= 1500
                            if booster == 1.6:
                                booster = 2
                                argent -= 750
                            if booster == 1.3:
                                booster = 1.6
                                argent -= 400
                            if booster == 1:
                                booster = 1.3
                                argent -= 150
                        else:
                            son_error.play()
                    if 408 < event.pos[0] < 473 and 130 < event.pos[1] < 160 and prix_ralentire != "":
                        if prix_ralentire <= argent:
                            son_ameliorer.play()
                            if ralentire == 0.4:
                                ralentire = 0.3
                                argent -= 4000
                            if ralentire == 0.5:
                                ralentire = 0.4
                                argent -= 2800
                            if ralentire == 0.65:
                                ralentire = 0.5
                                argent -= 1200
                            if ralentire == 0.8:
                                ralentire = 0.65
                                argent -= 500
                            if ralentire == 1:
                                ralentire = 0.8
                                argent -= 200
                        else:
                            son_error.play()
                    if 408 < event.pos[0] < 473 and 183 < event.pos[1] < 217 and prix_slow_fuel != "":
                        if prix_slow_fuel <= argent:
                            son_ameliorer.play()
                            if slow_fuel == 2000:
                                slow_fuel = 3000
                                argent -= 6000
                            if slow_fuel == 1600:
                                slow_fuel = 2000
                                argent -= 4500
                            if slow_fuel == 1200:
                                slow_fuel = 1600
                                argent -= 3000
                            if slow_fuel == 700:
                                slow_fuel = 1200
                                argent -= 1500
                            if slow_fuel == 400:
                                slow_fuel = 700
                                argent -= 500
                            if slow_fuel == 250:
                                slow_fuel = 400
                                argent -= 250
                        else:
                            son_error.play()
                    if 408 < event.pos[0] <= 473 and 240 < event.pos[1] < 270 and prix_puissance != "":
                        if prix_puissance < argent:
                            son_ameliorer.play()
                            if puissance == 2:
                                puissance = 3
                                argent -= 8000
                            if puissance == 1:
                                puissance = 2
                                argent -= 3000
                        else:
                            son_error.play()
                else:
                    usine = 0

            if 0 < event.pos[0] < 100 and 0 < event.pos[1] < 50:
                quitter = 3
            if 760 < event.pos[0] < 1060 and 310 < event.pos[1] < 482:
                usine = 1
                quitter = 4
            if 200 < event.pos[0] < 440 and 320 < event.pos[1] < 482:
                usine = 2
                quitter = 5

    return surface_fenetre, argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance,\
           slow_fuel, quitter, usine
