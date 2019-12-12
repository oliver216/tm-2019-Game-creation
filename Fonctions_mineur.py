from math import *


def collision_mineur(mineur_x, mineur_y, sense):
    # calcule les 3 point de collision du mineur

    # collision du point 1
    col1x = mineur_x + 18  # pour x
    col1y = mineur_y + 70  # pour y

    if sense < 245:
        x = 245 - sense
        col1x -= 0.26 * x
        col1y -= 0.56 * x
    if sense < 204:
        x = 204 - sense
        col1x -= 0.3 * x
        col1y -= 0.7 * x
    if sense > 270:
        x = sense - 270
        col1x += x
        col1y -= 0.15 * x
    if sense > 312:
        x = sense - 312
        col1x -= 0.63 * x
        col1y -= 0.7 * x

    # collision du point 2
    col2x = mineur_x  # pour x
    col2y = mineur_y + 34  # pour y

    if sense < 270:
        x = 270 - sense
        col2x += 0.56 * x
        col2y -= 0.17 * x
    if sense < 222:
        x = 222 - sense
        col2x -= 0.26 * x
        col2y -= 0.4 * x
    if sense > 270:
        x = sense - 270
        col2x += 0.6 * x
        col2y += 0.36 * x
    if sense > 320:
        x = sense - 320
        col2x -= 0.34 * x
        col2y -= 0.8 * x

    # collision du point 3
    col3x = mineur_x + 35  # pour x
    col3y = mineur_y + 34  # pour y
    if sense < 270:
        x = 270 - sense
        col3x += 0.3 * x
        col3y += 0.35 * x
    if sense < 229:
        x = 229 - sense
        col3x -= 0.4 * x
        col3y -= 0.6 * x
    if sense > 270:
        x = sense - 270
        col3x += 0.3 * x
        col3y -= 0.18 * x
    if sense > 316:
        x = sense - 316
        col3x -= 0.5 * x
        col3y -= 0.3 * x

    return col1x, col1y, col2x, col2y, col3x, col3y


def collision_plan(carte, ax, ay, bx, by, cx, cy):
    #  detecte la surface miné

    x = 0
    if ax < 0:
        a_x = -ax
        a_x += 2560
        x = int(a_x/2560)
        x = -x
    if ax > 2560:
        x = int(ax/2560)
    ax -= 2560 * x
    x = 0
    if bx < 0:
        b_x = -bx
        b_x += 2560
        x = int(b_x / 2560)
        x = -x
    if bx > 2560:
        x = int(bx / 2560)
    bx -= 2560 * x
    x = 0
    if cx < 0:
        c_x = -cx
        c_x += 2560
        x = int(c_x / 2560)
        x = -x
    if cx > 2560:
        x = int(cx / 2560)
    cx -= 2560 * x

    ay -= 480
    ay = int(ay / 80)
    ax = int(ax / 80)

    m = 32 * ay
    m += ax
    m = carte[m]

    by -= 480
    by = int(by / 80)
    bx = int(bx / 80)

    n = 32 * by
    n += bx
    n = carte[n]

    cy -= 480
    cy = int(cy / 80)
    cx = int(cx / 80)

    p = 32 * cy
    p += cx
    p = carte[p]
    if n == 5 or m == 5 or p == 5:  # si il touche de la lave
        return 4
    elif n == 4 or m == 4 or p == 4:  # si il touche de la bedrock
        return 3
    elif n == 3 or m == 3 or p == 3:  # si il touche de l'obsidienne
        return 2
    if n == 2 or m == 2 or p == 2:  # si il touche de la pierre
        return 1
    else:
        return 0


def vitesse_mineur(x, y, sense, b, v, s):
    # gére la vitesse et la direction du mineur

    sense = radians(sense)

    v_x = cos(sense)
    v_y = sin(sense)

    x += v_x * b * v * 1.6 * s
    y -= v_y * b * v * 1.6 * s

    return x, y


def correction(c_x, mineur_x, mineur_y, sense, sense2, rotation):
    # correction divers

    c_y = mineur_y - 120  # gère la caméra sur l'axe y

    # limit le déplacement de la caméra
    if c_x > mineur_x - 200:
        c_x = mineur_x - 200
    if c_x < mineur_x + 200 - 1280:
        c_x = mineur_x + 200 - 1280

    if c_y > 27600:
        c_y = 27600

    # bloque la rotation du mineur
    if sense > 340:
        sense = 340
    if sense < 200:
        sense = 200

    # correction de la rotation du mineur
    if sense < 270 and sense2 > sense:
        mineur_x -= 0.11 * rotation
    if sense2 < sense < 270:
        mineur_x += 0.11 * rotation
    if 260 < sense < 270 and sense2 < sense:
        mineur_y += 0.1 * rotation
    if 260 < sense < 270 and sense2 > sense:
        mineur_y -= 0.1 * rotation
    if 270 < sense < 280 and sense2 < sense:
        mineur_y -= 0.1 * rotation
    if 270 < sense < 280 and sense2 > sense:
        mineur_y += 0.1 * rotation

    return c_x, c_y, sense, mineur_x, mineur_y


def creuser(band_time, band2, plan, mineur_x, mineur_y):
    # système de creusement dans le plan

    mineur_x2 = mineur_x
    x = 0

    while mineur_x2 > 2560:
        mineur_x2 -= 2560
        x += 1
    while mineur_x2 < 0:
        mineur_x2 += 2560
        x -= 1

    if band_time >= 12:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 10:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 8:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 6:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 4:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 2:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
    if band_time >= 0.6:
        plan.blit(band2, (mineur_x - 2560 * x, mineur_y))
        band_time = 0

    return band_time
