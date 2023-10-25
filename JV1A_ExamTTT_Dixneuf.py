
tableau = [0,0,0]

cpt = 0
i = 0
tempDeJeux = 0

def affichageTableau( tableau):

    cpt = 0
    i = 0

    while(len(tableau) > cpt):
    
        for i in range (len(tableau)):
            print("*",end=" ")
            i +1

            
        print("") 
        cpt = cpt +1  



#affichageTableau(tableau)


def jouerX(tableau):

    #affichageTableau(tableau)
    cpt = 0
    i = 0

    colonneJouer = int(input("quelle colonne ?"))
    ligneJouer = int(input("quelle ligne ?"))
    
    while(len(tableau) > cpt):
    
        for i in range (len(tableau)):
            if(colonneJouer == cpt and ligneJouer == i):
                print("X",end=" ")
            else:
                print("*",end=" ")
            i +1

            
        print("") 
        cpt = cpt +1  


    # while(len(tableau) > cpt):
        
    #     if(cpt == colonneJouer):

    #         for i in range (len(tableau)):

    #             if(i == ligneJouer):
    #                 print("X")
    #             else:
    #                 print("*",end=" ")
    #             i +1

            
    #     print("") 
    #     cpt = cpt +1

jouerX(tableau)

def conditionDeVictoire (tableau):

    conditionGagner = 0
    JoueurGagnant = 0

    if(conditionGagner == 1):

        print("le joueur ", JoueurGagnant, " a gagner")
    else:
       1+1
        #le jeux continue
        




def finDeTableau(tableau):
     tempDeJeux = 0

     while(tempDeJeux <= 9):

        #deroulement de la partie

    

      tempDeJeux = tempDeJeux + 1

     print("Fin de la parie la grille est remplie")




def jeuComplet(tableau):
    1+1


#il sufirait de ralongé la taille du tableau et de modifier la condition de victoire a un alignement de 4 symbole pour passer sur un jeu de puissance 4