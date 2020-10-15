# les conditions permettent de de verifier une comparaison
# le resultat d'une comparaison est soit vrai ou faux
# si le resultat est vrai on excute le code de la onditions
# il existe 3 conditions possibl :
# si = if  
# sinon si = elif
#sinon = sinon

# les different operateurs de comparaisons sont :
# > stritement plus grand
# < plus petit
# == egal
# >= plus grand ou egal
#<= plus petit ou egal
#
#!= different


chiffre = 10

if chiffre %2 == 0:
    print("chiffre paire")

else:
    print("impair")

if chiffre > 10:
    print ("plus grand que 10")

elif chiffre < 10:
    print ("plus petit que 10")

else:
    print ("egal 10")

text = "maison"
lettre = "i"

if lettre in text:
    print ( lettre, "est dans ", text)

else:
    print (lettre, "n'est pas dan", text)