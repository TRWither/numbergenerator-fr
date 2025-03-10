import random 
import sys 

def main():
    print("Bienvenue dans ce générateur de nombre aléatoire !")
    start = input("Entrez 1 pour générer un nombre entre 1 et 10 et entrez 2 pour générer un nombre entre 1 et 100 ")
    if start == "1":
        one_to_ten()
    elif start == "2":
        one_to_hundred()
    else:
        print("Veuillez entrer un nombre valide")
        main()
def one_to_ten():
    number = random.randint(1, 10)
    print(number)
    endd = input("Veux-tu recommencer ? (oui/non): ")
    if endd == "oui":
        main()
    else:
        sys.exit()

def one_to_hundred():
    numberr = random.randint(1, 100)
    print(numberr)
    end = input("Veux-tu recommencer ? (oui/non): ")
    if end == "oui":
        main()
    else:
        sys.exit()



main()

