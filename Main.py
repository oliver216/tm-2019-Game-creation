from Fonctions import *
from Fonctions_upgrade import *
from Fonctions_mineur import *
from Fonctions_gem import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# taille de la fenetre
w, h = 1280, 720

taille_fenetre = (w, h)
surface_fenetre = pygame.display.set_mode(taille_fenetre)  # crée la fenetre d'affichage
Fullscreen = False

# couleur (RGB, rouge, verte, bleu)
BLANC = (255, 255, 255)
BLEU = (175, 225, 255)
GRIS_NOIR = (40, 40, 40)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
JAUNE = (215, 150, 0)
MOD = (0, 0, 0) # couleur qui va etre modifié (noir de base)

# style des texts
text = pygame.font.SysFont("monospace", 30)
grand_text = pygame.font.SysFont("monospace", 80)
petit_text = pygame.font.SysFont("monospace", 20)

# en attente du chargement
surface_fenetre.fill(BLEU)
pygame.display.flip()

# création des blocks du plan
herbe = pygame.image.load("images/herbe.png")
herbe = pygame.transform.scale(herbe, (80, 80))
terre = pygame.image.load("images/terre.png")
terre = pygame.transform.scale(terre, (80, 80))
pierre = pygame.image.load("images/pierre.png")
pierre = pygame.transform.scale(pierre, (80, 80))
obsidienne = pygame.image.load("images/obsidienne.png")
obsidienne = pygame.transform.scale(obsidienne, (80, 80))
bedrock = pygame.image.load("images/bedrock.png")
bedrock = pygame.transform.scale(bedrock, (80, 80))
lave = pygame.image.load("images/lave.png")
lave = pygame.transform.scale(lave, (80, 80))

# panneau décoratif
panneau = pygame.image.load("images/panneau.png")
panneau = pygame.transform.scale(panneau, (40, 55))
menu_jeu = pygame.image.load("images/menu_jeu.png")
menu_jeu = pygame.transform.scale(menu_jeu, (1280, 450))
cadre = pygame.image.load("images/cadre.png")
cadre2 = cadre
cadre2 = pygame.transform.scale(cadre2, (500, 350))
cadre = pygame.transform.scale(cadre, (580, 250))

# usine d'amélioration
usine_1 = pygame.image.load("images/usine.png")
usine_1 = pygame.transform.scale(usine_1, (300, 200))
usine_2 = pygame.image.load("images/usine2.png")
usine_2 = pygame.transform.scale(usine_2, (300, 200))

# création du mineur et de ses variable
mineur = pygame.image.load("images/mineur.png")
mineur = pygame.transform.scale(mineur, (35, 70))
mineur2 = pygame.image.load("images/mineur2.png")
mineur2 = pygame.transform.scale(mineur2, (35, 70))
mineur_steel = pygame.image.load("images/mineur_steel.png")
mineur_steel = pygame.transform.scale(mineur_steel, (35, 70))
mineur_steel2 = pygame.image.load("images/mineur_steel2.png")
mineur_steel2 = pygame.transform.scale(mineur_steel2, (35, 70))
mineur_diamond = pygame.image.load("images/mineur_diamond.png")
mineur_diamond = pygame.transform.scale(mineur_diamond, (35, 70))
mineur_diamond2 = pygame.image.load("images/mineur_diamond2.png")
mineur_diamond2 = pygame.transform.scale(mineur_diamond2, (35, 70))

# création de la band (ce qui fait creuser le mineur)
band = pygame.image.load("images/band.png")
band = pygame.transform.scale(band, (35, 70))

# Tout les gems collectables
gem_bleu = pygame.image.load("images/gem_bleu.png")
gem_orange = pygame.image.load("images/gem_orange.png")
gem_rouge = pygame.image.load("images/gem_rouge.png")
gem_verte = pygame.image.load("images/gem_verte.png")
gem_violet = pygame.image.load("images/gem_violet.png")
gem_bleu = pygame.transform.scale(gem_bleu, (20, 20))
gem_orange = pygame.transform.scale(gem_orange, (20, 20))
gem_rouge = pygame.transform.scale(gem_rouge, (20, 20))
gem_verte = pygame.transform.scale(gem_verte, (20, 20))
gem_violet = pygame.transform.scale(gem_violet, (20, 20))

# plan sur le quel on joue
plan = pygame.Surface((2560, 28320))

# surface graphique utuliser
cube = pygame.Surface((120, 120))
cube.fill(GRIS_NOIR)
rectangle = pygame.Surface((65, 30))
rectangle.fill(JAUNE)
ombre = pygame.Surface(taille_fenetre)
ombre.fill(NOIR)
ombre2 = ombre

# timer pour le refresh de l'image
timer = pygame.time.Clock()

# quelque text utuliser plusieur fois
back = text.render("Back", 1, NOIR)
back2 = text.render("Menu", 1, NOIR)
loading = text.render("Loading...", 1, NOIR)
perdu = text.render(" You have autodestroyed !", 1, BLANC)

volume = 1.6  # plus tard on pourras changer le volume

# charge les bruitages du jeu
son_collision = pygame.mixer.Sound("sounds/collision.wav")
son_collision.set_volume(0.32 * volume)
son_collecter = pygame.mixer.Sound("sounds/collecter.wav")
son_collecter.set_volume(0.1 * volume)
son_ameliorer = pygame.mixer.Sound("sounds/amelioration.wav")
son_ameliorer.set_volume(0.4 * volume)
son_click = pygame.mixer.Sound("sounds/click.wav")
son_click.set_volume(0.2 * volume)
son_oiseau1 = pygame.mixer.Sound("sounds/oiseau1.wav")
son_oiseau1.set_volume(0.12 * volume)
son_oiseau2 = pygame.mixer.Sound("sounds/oiseau2.wav")
son_oiseau2.set_volume(0.12 * volume)
son_error = pygame.mixer.Sound("sounds/error.wav")
son_error.set_volume(1.2 * volume)
son_usine1 = pygame.mixer.Sound("sounds/usine1.wav")
son_usine1.set_volume(0.25 * volume)
son_usine2 = pygame.mixer.Sound("sounds/usine2.wav")
son_usine2.set_volume(0.25 * volume)
son_moteur = pygame.mixer.Sound("sounds/moteur.wav")
son_moteur.set_volume(0.1 * volume)
son_moteur_boost = pygame.mixer.Sound("sounds/moteur_boost.wav")
son_moteur_boost.set_volume(0.3 * volume)
son_moteur_slow = pygame.mixer.Sound("sounds/moteur_slow.wav")
son_moteur_slow.set_volume(0.07 * volume)
son_panne_essence = pygame.mixer.Sound("sounds/panne_essence.wav")
son_panne_essence.set_volume(0.32 * volume)

# affiche le menu
menu2 = 0
save = "1"
menu = True
game = True
while menu:  # boulce affichant le menu

    for event in pygame.event.get():
        if event.type == QUIT:
            menu = False
            game = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu = False
                game = False
        if menu2 == 1:
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if 470 < event.pos[0] < 590 and 250 < event.pos[1] < 370:
                        son_click.play()
                        save = "1"
                        menu2 = 2
                    if 690 < event.pos[0] < 810 and 250 < event.pos[1] < 370:
                        son_click.play()
                        save = "2"
                        menu2 = 2
                    if 470 < event.pos[0] < 590 and 450 < event.pos[1] < 570:
                        son_click.play()
                        save = "3"
                        menu2 = 2
                    if 690 < event.pos[0] < 810 and 450 < event.pos[1] < 570:
                        son_click.play()
                        save = "4"
                        menu2 = 2
        if menu2 == 0:
            if event.type == KEYDOWN:
                if event.key != K_ESCAPE:
                    son_click.play()
                    game = True
                    menu2 = 1
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if 0 < event.pos[0] < 195 and 0 < event.pos[1] < 50:
                        if Fullscreen:
                            surface_fenetre = pygame.display.set_mode(taille_fenetre)
                            Fullscreen = False
                        else:
                            surface_fenetre = pygame.display.set_mode(taille_fenetre, pygame.FULLSCREEN)
                            Fullscreen = True
                    else:
                        son_click.play()
                        game = True
                        menu2 = 1
        if menu2 == 1:
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if 0 < event.pos[0] < 100 and 0 < event.pos[1] < 50:
                        son_click.play()
                        menu2 = 0

    if menu2 == 0:

        surface_fenetre.fill(BLEU)
        surface_fenetre.blit(menu_jeu, (0, 270))
        surface_fenetre.blit(text.render("Fullscreen", 1, NOIR), (15, 10))
        surface_fenetre.blit(grand_text.render("Always deeper", 1, NOIR), (315, 120))
        surface_fenetre.blit(text.render("Press any key to continue", 1, NOIR), (390, 350))
        pygame.display.flip()

    if menu2 == 1:

        surface_fenetre.fill(BLEU)
        surface_fenetre.blit(back, (15, 5))
        surface_fenetre.blit(text.render("Select a save", 1, NOIR), (530, 100))
        surface_fenetre.blit(cube, (470, 250))
        surface_fenetre.blit(cube, (690, 250))
        surface_fenetre.blit(cube, (470, 450))
        surface_fenetre.blit(cube, (690, 450))
        surface_fenetre.blit(text.render("save 1", 1, BLANC), (475, 335))
        surface_fenetre.blit(text.render("save 2", 1, BLANC), (695, 335))
        surface_fenetre.blit(text.render("save 3", 1, BLANC), (475, 535))
        surface_fenetre.blit(text.render("save 4", 1, BLANC), (695, 535))
        pygame.display.flip()

    if menu2 == 2:

        # fenetre de chargement
        surface_fenetre.fill(BLEU)
        surface_fenetre.blit(loading, (520, 530))
        pygame.display.flip()

        # charge la sauvegarde selectionné
        argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, slow_fuel_max = charger(save)

        # entrée dans la partie, revient ici à chaque fin de partie
        while game:

            # crée la carte aléatoirement
            plan.fill(BLEU)
            plan.blit(panneau, (540, 425))
            plan.blit(usine_1, (760, 282))
            plan.blit(usine_2, (200, 282))
            carte, plan = creation_carte(plan, herbe, terre, pierre, obsidienne, bedrock, lave,
                                         surface_fenetre, mineur, text)

            # crée tout les gems
            list_gems = creation_gems(carte, gem_rouge, gem_bleu, gem_verte, gem_violet, gem_orange, puissance)

            # camera
            c_x, c_y = 0, 0

            # atribut de départ
            mineur_x, mineur_y = 622, 442
            mineur3 = mineur
            mineur4 = mineur2
            mineur5 = mineur
            drill_time = 1
            sense = 270
            boost_time = -300
            boost = 1
            stat_boost = 150
            moteur_time = 100
            ombre.set_alpha(0)
            MOD = (0, 0, 0)
            mod_x = 0
            essence = essence_max
            slow_fuel = slow_fuel_max
            nb_gems_orange = 0
            nb_gems_violet = 0
            nb_gems_verte = 0
            nb_gems_bleu = 0
            nb_gems_rouge = 0

            start = 0
            continuer = True
            usine = 0

            # zone d'amélioration
            while start == 0:

                # affichage dans la ville
                surface_fenetre.fill(BLEU)
                surface_fenetre.blit(plan, (0 - c_x, 0 - c_y))
                affichage_gems(surface_fenetre, list_gems, c_x, c_y, mineur_x)
                surface_fenetre.blit(mineur3, (mineur_x - c_x, mineur_y - c_y))
                surface_fenetre.blit(text.render("Fuel : " + str(int(essence)), 1, NOIR), (13, 40))
                if booster > 1:
                    surface_fenetre.blit(text.render("Boost : " + str(int(stat_boost)), 1, NOIR), (14, 75))
                if ralentire < 1:
                    surface_fenetre.blit(text.render("Break : " + str(int(slow_fuel)), 1, NOIR), (14, 110))
                surface_fenetre.blit(text.render(str(int(argent)), 1, NOIR), (1170, 15))
                surface_fenetre.blit(gem_orange, (1142, 20))
                surface_fenetre.blit(back2, (15, 5))
                surface_fenetre.blit(text.render("Press any key to start", 1, NOIR), (435, 600))

                # tout les variable pour les améliorations du mineur + affichage de celle si
                surface_fenetre, argent, ralentire, booster, essence_max, vitesse, rotation, valeur_gems, puissance, \
                slow_fuel_max, quitter, usine = upgrade(ralentire, booster, essence_max, vitesse, rotation, valeur_gems,
                                                    puissance, slow_fuel_max, argent, surface_fenetre, petit_text,
                                                    BLANC, rectangle, cadre, son_ameliorer, son_error, usine)

                if puissance == 2:
                    mineur3 = mineur_steel
                    mineur4 = mineur_steel2
                if puissance == 3:
                    mineur3 = mineur_diamond
                    mineur4 = mineur_diamond2
                essence = essence_max
                slow_fuel = slow_fuel_max
                son_oiseau(son_oiseau1, son_oiseau2)

                # action de menu de la ville
                if quitter == 1:
                    start = 80
                if quitter == 2:
                    continuer = False
                    game = False
                    menu = False
                    start = 100
                if quitter == 3:
                    son_click.play()
                    menu2 = 0
                    continuer = False
                    game = False
                    start = 100
                if quitter == 4:
                    son_click.play()
                    son_usine1.play()
                if quitter == 5:
                    son_click.play()
                    son_usine2.play()

                timer.tick(60)
                pygame.display.flip()

            # animation de depart
            while 0 < start <= 80:
                c_y += 4.025
                surface_fenetre.fill(BLEU)
                surface_fenetre.blit(plan, (0 - c_x, 0 - c_y))
                affichage_gems(surface_fenetre, list_gems, c_x, c_y, mineur_x)
                surface_fenetre.blit(mineur3, (mineur_x - c_x, mineur_y - c_y))
                surface_fenetre.blit(text.render("Fuel : " + str(int(essence)), 1, NOIR), (13, 5))
                if booster > 1:
                    surface_fenetre.blit(text.render("Boost : " + str(int(stat_boost)), 1, NOIR), (14, 40))
                if ralentire < 1:
                    surface_fenetre.blit(text.render("Break : " + str(int(slow_fuel)), 1, NOIR), (14, 75))
                surface_fenetre.blit(text.render(str(int(argent)), 1, NOIR), (1170, 15))
                surface_fenetre.blit(gem_orange, (1142, 20))
                pygame.display.flip()
                start -= 1
                timer.tick(60)

            # crée les fonction de touche
            k_droit = False
            k_gauche = False
            k_c_droit = False
            k_c_gauche = False
            k_ralentire = False
            k_boost = False

            # Boucle pour tout les touches que le joueur peut utiliser
            while continuer:
                for event in pygame.event.get():
                    # quitter
                    if event.type == QUIT:
                        continuer = False
                        game = False
                        menu = False
                        start = 100
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.mixer.stop()
                            son_collision.play()
                            perdu = text.render(" You have autodestroyed !", 1, BLANC)
                            continuer = False

                    # mineur rotation droit, gauche
                    if event.type == KEYDOWN:
                        if event.key == K_d or event.key == K_RIGHT:
                            k_droit = True
                    if event.type == KEYUP:
                        if event.key == K_d or event.key == K_RIGHT:
                            k_droit = False
                    if event.type == KEYDOWN:
                        if event.key == K_a or event.key == K_LEFT:
                            k_gauche = True
                    if event.type == KEYUP:
                        if event.key == K_a or event.key == K_LEFT:
                            k_gauche = False

                    # boost et ralentissement
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE or event.key == K_w or event.key == K_UP:
                            k_boost = True
                    if event.type == KEYUP:
                        if event.key == K_SPACE or event.key == K_w or event.key == K_UP:
                            k_boost = False
                    if event.type == KEYDOWN:
                        if event.key == K_s or event.key == K_DOWN:
                            k_ralentire = True
                    if event.type == KEYUP:
                        if event.key == K_s or event.key == K_DOWN:
                            k_ralentire = False

                    # camera droit, gauche
                    if event.type == KEYDOWN:
                        if event.key == K_e or event.key == K_KP0:
                            k_c_droit = True
                    if event.type == KEYUP:
                        if event.key == K_e or event.key == K_KP0:
                            k_c_droit = False
                    if event.type == KEYDOWN:
                        if event.key == K_q or event.key == K_RCTRL:
                            k_c_gauche = True
                    if event.type == KEYUP:
                        if event.key == K_q or event.key == K_RCTRL:
                            k_c_gauche = False

                sense2 = sense  # stock la direction avant modification
                boost2 = boost  # stock la valeur du boost avant modification
                essence -= 1 * boost * vitesse  # perte d'essence

                # vérifie quel touche sont appuyés et fait les déplcement nécessaire
                if k_droit:
                    sense += 0.35 * rotation
                if k_gauche:
                    sense -= 0.35 * rotation

                boost_time -= 1
                if k_boost:
                    if boost_time < -300:
                        boost = booster
                        boost_time = 150
                if boost_time > 0:
                    boost = booster
                if boost_time <= 0:
                    boost = 1
                if k_ralentire and slow_fuel > 0:
                    boost = ralentire
                    slow_fuel -= 1

                if k_c_droit:
                    c_x += 10
                if k_c_gauche:
                    c_x -= 10

                if boost_time >= 0:
                    stat_boost = boost_time
                if boost_time < 0:
                    stat_boost = - boost_time/2
                if boost_time < -300:
                    stat_boost = 150

                # regarde la surface miné
                col1x, col1y, col2x, col2y, col3x, col3y = collision_mineur(mineur_x, mineur_y, sense)
                col = collision_plan(carte, col1x, col1y, col2x, col2y, col3x, col3y)
                surface = 1
                if col == 1:
                    if puissance == 2:
                        surface = 0.5
                    if puissance == 3:
                        surface = 0.75
                if col == 2:
                    if puissance == 3:
                        surface = 0.4

                # correction diverse et blocage camera/rotation
                c_x, c_y, sense, mineur_x, mineur_y = correction(c_x, mineur_x, mineur_y, sense, sense2, rotation)
                # déplace le mineur
                mineur_x, mineur_y = vitesse_mineur(mineur_x, mineur_y, sense, boost, vitesse, surface)
                # donne les points de collisions du mineur
                col1x, col1y, col2x, col2y, col3x, col3y = collision_mineur(mineur_x, mineur_y, sense)
                # test les collision entre les gems et le mineur
                argent, couleur = collision_gems(list_gems, argent, valeur_gems,
                                                 col1x, col1y, col2x, col2y, col3x, col3y, son_collecter)
                # test les collision avec le plan
                col = collision_plan(carte, col1x, col1y, col2x, col2y, col3x, col3y)

                if couleur == 15:
                    nb_gems_orange += 1
                if couleur == 30:
                    nb_gems_violet += 1
                if couleur == 50:
                    nb_gems_verte += 1
                if couleur == 80:
                    nb_gems_bleu += 1
                if couleur == 150:
                    nb_gems_rouge += 1

                # gestion de l'ombre
                if mineur_y <= 12442:
                    ombre.set_alpha(int((mineur_y - 442) / 60))
                if mineur_y >= 16080:
                    ombre.set_alpha(200 - int((mineur_y - 16080) / 60))

                # changement du couleur du text pour une meilleur lisibilité
                if mod_x < 256:
                    MOD = (mod_x, mod_x, mod_x)
                if mod_x < 256:
                    mod_x += 3

                # son du mineur
                if moteur_time == 100 or boost != boost2:
                    son_moteur.stop()
                    son_moteur_boost.stop()
                    son_moteur_slow.stop()
                    if boost == 1:
                        son_moteur.play()
                    if boost == booster:
                        son_moteur_boost.play()
                    if boost == ralentire:
                        son_moteur_slow.play()
                if moteur_time == 100:
                    moteur_time = 0
                moteur_time += 1

                # perd la partie
                if essence <= 0:
                    pygame.mixer.stop()
                    son_panne_essence.play()
                    continuer = False
                    perdu = text.render("  You run out of fuel !", 1, BLANC)

                if col == 1 and puissance == 1:
                    perdu = text.render(" You crashed into stone !", 1, BLANC)
                    pygame.mixer.stop()
                    son_collision.play()
                    continuer = False
                if col == 2 and puissance != 3:
                    perdu = text.render("You crashed into obsidian", 1, BLANC)
                    pygame.mixer.stop()
                    son_collision.play()
                    continuer = False
                if col == 3:
                    perdu = text.render("You crashed into bedrock !", 1, BLANC)
                    pygame.mixer.stop()
                    son_collision.play()
                    continuer = False
                if col == 4:
                    perdu = text.render(" You smelted into lava !", 1, BLANC)
                    pygame.mixer.stop()
                    son_collision.play()
                    continuer = False

                # rotation du mineur (affichage)
                if 6 < drill_time <= 12:
                    mineur5 = pygame.transform.rotate(mineur4, sense - 270)
                else:
                    mineur5 = pygame.transform.rotate(mineur3, sense - 270)
                if drill_time == 12:
                    drill_time = 0
                drill_time += 1

                """band2 = pygame.transform.rotate(band, sense - 270)
                plan.blit(band2, (mineur_x, mineur_y))  # creuse dans le plan"""

                # affiche tout a l'ecran
                surface_fenetre.fill(BLEU)
                plan_infinit(surface_fenetre, plan, c_x, c_y, mineur_x)
                affichage_gems(surface_fenetre, list_gems, c_x, c_y, mineur_x)
                surface_fenetre.blit(mineur5, (mineur_x - c_x, mineur_y - c_y))
                surface_fenetre.blit(ombre, (0, 0))
                surface_fenetre.blit(text.render("Fuel : " + str(int(essence)), 1, MOD), (13, 5))
                if booster > 1:
                    surface_fenetre.blit(text.render("Boost : " + str(int(stat_boost)), 1, MOD), (14, 40))
                if ralentire < 1:
                    surface_fenetre.blit(text.render("Break : " + str(int(slow_fuel)), 1, MOD), (14, 75))
                surface_fenetre.blit(text.render(str(int(argent)), 1, MOD), (1170, 15))
                surface_fenetre.blit(gem_orange, (1142, 20))
                pygame.display.flip()

                timer.tick(60)

            # attende pour redemarer la partie
            while start == 0:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            son_click.play()
                            start = 1
                    if event.type == QUIT:
                        game = False
                        menu = False
                        start = 1
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            game = False
                            menu = False
                            start = 1

                # argent totale gagner au cours de la partie
                argent_totale = (nb_gems_orange * 15 + nb_gems_violet * 30 +
                                 nb_gems_verte * 50 + nb_gems_bleu * 80 + nb_gems_rouge * 150) * valeur_gems

                # affichage de la fenetre de fin de partie
                surface_fenetre.fill(BLEU)
                plan_infinit(surface_fenetre, plan, c_x, c_y, mineur_x)
                affichage_gems(surface_fenetre, list_gems, c_x, c_y, mineur_x)
                surface_fenetre.blit(mineur5, (mineur_x - c_x, mineur_y - c_y))
                surface_fenetre.blit(ombre, (0, 0))
                surface_fenetre.blit(text.render("Fuel : " + str(int(essence)), 1, MOD), (13, 5))
                if booster > 1:
                    surface_fenetre.blit(text.render("Boost : " + str(int(stat_boost)), 1, MOD), (14, 40))
                if ralentire < 1:
                    surface_fenetre.blit(text.render("Break : " + str(int(slow_fuel)), 1, MOD), (14, 75))
                surface_fenetre.blit(text.render(str(int(argent)), 1, MOD), (1170, 15))
                surface_fenetre.blit(gem_orange, (1142, 20))
                surface_fenetre.blit(cadre2, (400, 150))
                surface_fenetre.blit(perdu, (422, 180))
                for i in range(5):
                    surface_fenetre.blit(petit_text.render("Gems    collected : ", 1, BLANC), (500, 240 + i*28))
                surface_fenetre.blit(petit_text.render("Total gems value : ", 1, BLANC), (500, 420))
                surface_fenetre.blit(petit_text.render(str(nb_gems_orange), 1, BLANC), (745, 240))
                surface_fenetre.blit(petit_text.render(str(nb_gems_violet), 1, BLANC), (745, 268))
                surface_fenetre.blit(petit_text.render(str(nb_gems_verte), 1, BLANC), (745, 296))
                surface_fenetre.blit(petit_text.render(str(nb_gems_bleu), 1, BLANC), (745, 324))
                surface_fenetre.blit(petit_text.render(str(nb_gems_rouge), 1, BLANC), (745, 352))
                surface_fenetre.blit(petit_text.render(str(int(argent_totale)), 1, BLANC), (755, 420))
                surface_fenetre.blit(gem_orange, (560, 242))
                surface_fenetre.blit(gem_violet, (560, 270))
                surface_fenetre.blit(gem_verte, (560, 298))
                surface_fenetre.blit(gem_bleu, (560, 326))
                surface_fenetre.blit(gem_rouge, (560, 354))
                surface_fenetre.blit(gem_orange, (722, 422))
                surface_fenetre.blit(text.render("Press space to go to town", 1, MOD), (420, 560))
                pygame.display.flip()

                timer.tick(60)

            # fenetre de chargement
            surface_fenetre.fill(BLEU)
            surface_fenetre.blit(loading, (520, 530))
            pygame.display.flip()
            # sauvegadre les donné de la partie
            sauvegarder(save, argent, ralentire, booster, essence_max,
                        vitesse, rotation, valeur_gems, puissance, slow_fuel_max)

pygame.quit()
