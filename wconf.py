""""""""""
Wireguard config
Auteur: Victor Liu
Datum: 30-06-2023
Versie: 6.0


Vereisten:
pip install python-wireguard

Documentatie:
Wireguard-pakket: https://pypi.org/project/python-wireguard/
Wireguard:        https://www.wireguard.com/embedding/

"""""""""
# Importeer vereiste modules
from python_wireguard import Client, ServerConnection, Key
from gkey import gkey
import subprocess

# Definieer variabelenpyth
local_ip = "10.10.10.2/24"
client_key_str, server_key_str = gkey('/home/vicc')
client_key = Key(client_key_str.strip())
print(client_key)
server_key = Key(server_key_str.strip())
print(server_key)
endpoint = "80.80.80.1"
port = 51820

# Stop en verwijder bestaande WireGuard-configuratie
subprocess.run(['sudo', 'wg-quick', 'down', 'wg0'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['sudo', 'rm', '/etc/wireguard/wg0.conf'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Maak WireGuard-client- en server-verbindingobjecten
client = Client('wg0', client_key, local_ip)
server_conn = ServerConnection(server_key, endpoint, port)
client.set_server(server_conn)

# Maak configuratiebestand
config = f'''[Interface]
PrivateKey = {client_key}
ListenPort = {port}
Address = {local_ip}

[Peer]
PublicKey = {server_key}
AllowedIPs = 10.10.10.0/24, 192.168.0.0/16 
Endpoint = {endpoint}:{port}
'''

# Schrijf configuratiebestand
with open('/etc/wireguard/wg0.conf', 'w') as f:
    f.write(config)

# Start WireGuard en controleer verbinding
subprocess.run(['sudo', 'wg-quick', 'up', 'wg0'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Starting WireGuard")
try:
    client.connect()
    print("WireGuard-verbinding is successvol.")
    subprocess.run('wg')
except:
    print("WireGuard-verbinding is mislukt.")
