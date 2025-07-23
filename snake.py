import msvcrt
import os
import time
import random

largeur = 20
hauteur = 10

def afficher_grille(serpent, fruit):
    grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]

    for y in range(hauteur):
        for x in range(largeur):
            if y == 0 or y == hauteur - 1 or x == 0 or x == largeur - 1:
                grille[y][x] = '#'

    # Placer le serpent
    for i, (x, y) in enumerate(serpent):
        if i == 0:
            grille[y][x] = 'O'  # tête
        else:
            grille[y][x] = 'o'  # corps

    # Placer fruit
    x_fruit, y_fruit = fruit
    grille[y_fruit][x_fruit] = "*"


    # Affichage
    os.system('cls')  
    for ligne in grille:
        print(''.join(ligne))

def lire_direction(direction_actuelle):
    if msvcrt.kbhit():
        touche = msvcrt.getch().decode('utf-8').lower()
        if touche == 'z' and direction_actuelle != (0, 1):
            return (0, -1)  # haut
        elif touche == 's' and direction_actuelle != (0, -1):
            return (0, 1)   # bas
        elif touche == 'q' and direction_actuelle != (1, 0):
            return (-1, 0)  # gauche
        elif touche == 'd' and direction_actuelle != (-1, 0):
            return (1, 0)   # droite
    return direction_actuelle

def deplacer_serpent(serpent, direction, fruit, score):
    x, y = serpent[0]
    dx, dy = direction
    nouvelle_tete = (x + dx, y + dy)

    if nouvelle_tete[0] <= 0 or nouvelle_tete[0] >= largeur-1 or nouvelle_tete[1] <= 0 or nouvelle_tete[1] >= hauteur-1:
        return None

    if nouvelle_tete in serpent:
        return None

    serpent.insert(0, nouvelle_tete)

    if nouvelle_tete == fruit:
        fruit = fruits()
        score += 1 
    else :
        serpent.pop()


    return serpent, fruit, score

def fruits():
    # Placer fruit
    x_fruit = random.randint(1, largeur - 2)
    y_fruit = random.randint(1, hauteur - 2)

    return (x_fruit, y_fruit)


def snake():
    serpent = [(10, 5)]  
    direction = (1, 0)  # vers la droite
    fruit = fruits()
    score = 0

    while True:
        afficher_grille(serpent, fruit)
        direction = lire_direction(direction)
        resultat = deplacer_serpent(serpent, direction, fruit, score)
        if resultat is None:
            print("Game Over!")
            break
        else:
            serpent, fruit, score = resultat
        print(f"Score: {score}")
        time.sleep(0.4)

snake()
