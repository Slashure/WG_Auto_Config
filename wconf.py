""""""""""
Wcon.py
Wireguard config
Auteur: Victor Liu
Datum: 07-07-2023
Versie: 8.0 eind


Vereisten:
pip install python-wireguard

Documentatie:
Wireguard-pakket: https://pypi.org/project/python-wireguard/
Wireguard:        https://www.wireguard.com/embedding/
Een script dat automatisch een configuratie maakt. Het is wel van belang dat de gkey.py bestand erbij gebruikt moet worden om keys te generen en in de config te doen

"""""""""
# Importeer vereiste modules
from python_wireguard import Client, ServerConnection, Key
from gkey import gkey
import subprocess

#Variablelen
#Client key en serverkey worden uit de script van gkey gehaald
client_key_str, server_key_str = gkey('/home/vicc') #pad waar de keys op dat moment zijn

#interface variabelen
client_key = Key(client_key_str.strip())
listen_port= 51820
local_ip = "10.10.10.2/24"

#peer variabelen
server_key = Key(server_key_str.strip())
endpoint = "80.80.80.2"
port = 51820


# Stop en verwijder bestaande WireGuard-configuratie
subprocess.run(['sudo', 'wg-quick', 'down', 'wg0'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  #stop huidige wireguard interface
subprocess.run(['sudo', 'rm', '/etc/wireguard/wg0.conf'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #Verwijder config file

# Maak WireGuard-client- en server-verbindingobjecten
client = Client('wg0', client_key, local_ip)
server_conn = ServerConnection(server_key, endpoint, port)
client.set_server(server_conn)

# Maak configuratiebestand
config = f'''[Interface]
PrivateKey = {client_key}
ListenPort = {listen_port}
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
