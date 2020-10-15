# on importe une librairie pour choisir un nombre aleatoire:
import random
#on cree une variable nombrecacheee
#on y stock un nombre aleatoir entre 0 et 100
#on fait appel a la fonction randint qui est dans la fonction random
nombre_cache = random.randint (0,100)

print("tape un nombre entre 0 et 100")
entre_joueur = int (input(">>"))

print (entre_joueur)

if entre_joueur > nombre_cache:
    print ("grang")

elif entre_joueur < nombre_cache:
    print ("plus petit")
    
else :
        print ("winner")
    


