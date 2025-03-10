import random, sys

def main():
    print("Bienvenue dans ce générateur de nombres aléatoires !")

    # Ajout d'une boucle infinie pour permettre à l'utilisateur d'utiliser
    # l'outil plusieurs fois sans avoir à le redémarrer
    try:
        while True:
            # Demande à l'utilisateur d'entrer le minimum et le maximum
            # Comme ils sont récupérés sous forme de strings, on les convertit
            # en entiers avec int()
            n_min = int(input("Entrez le nombre minimum: "))
            n_max = int(input("Entrez le nombre maximum: "))

            # Ensuite, on génère le nombre aléatoire et on l'imprime
            n_result = random.randint(n_min, n_max)

            print(n_result)
    # Quitte le programme si l'utilisateur appuie sur Ctrl+C ou Ctrl+D
    # en affichant une nouvelle ligne avant de sortir
    except KeyboardInterrupt or EOFError:
        print()
        sys.exit()

# Plus conventionnel
if __name__ == "__main__":
    main()