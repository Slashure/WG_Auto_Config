""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Wireguard configurator
Auteur: Kasper van der Mark
Datum: 30-03-2023
Versie: 2.0

Dit programma creëert een Wireguard-configuratie en start de Wireguard-service.
Dit programma werkt alleen op linux, door de path en de sudo commando's.
VERANDER SLEUTELS!!

Vereisten:
pip install python-wireguard

Documentatie:
Wireguard-pakket: https://pypi.org/project/python-wireguard/
Wireguard:        https://www.wireguard.com/embedding/

Disclaimer:
Deze configurator is mede mogelijk gemaakt door ChatGPT, een AI-taalmodel getraind door OpenAI.
Voor veilig gebruik van dit Python-script dienen de sleutels te worden aangepast en vertrouwelijk te blijven.
Ik aanvaard geen enkele verantwoordelijkheid voor eventuele schade die kan ontstaan door het gebruik van dit script.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Importeer vereiste modules
from python_wireguard import Client, ServerConnection, Key
from gkey import gkey
import subprocess

# Definieer variabelen
local_ip = "10.10.10.2/24"
client_key_str, server_key_str = gkey('/home/user/Desktop/')
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
Address = {local_ip}

[Peer]
PublicKey = {server_key}
AllowedIPs = 10.10.10.0/24, 192.168.0.0/16 
Endpoint = {endpoint}:{port}
'''

# Schrijf configuratiebestand
with open('/etc/wireguard/wg0', 'w') as f:
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
    
