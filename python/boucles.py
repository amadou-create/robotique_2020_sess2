# en python il existe 2 types de boucles
#while = tant que 
#for = pour chaque
# le resultat de la condition d'une boucles est soit 
#True 
#False


nombre= 10
flag = True

while nombre >=0:
    print (nombre)
    nombre = nombre -1

while flag == True:
    print("ok")
    flag = False

for lettre in "maison":
    print("---------")

phrase = "bientot la pause"
for lettre in phrase:
    if lettre in "aeiuoy":
        print(lettre)