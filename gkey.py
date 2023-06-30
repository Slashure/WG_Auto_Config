"""""""""
Keygen/Keygetter
Auteur: Victor Liu
Datum: 30-06-2023
Versie: 6.0


Vereisten:
pip install python-wireguard

Documentatie:
Wireguard-pakket: https://pypi.org/project/python-wireguard/
Wireguard:        https://www.wireguard.com/embedding/

"""""""""

from time import sleep
import subprocess

def main():
    print('dit is de gkey functie script')
    keygen()
    file_path = input('wat is het pad naar de keys: ')
    #file_path = ('/home/user')
    client, server, = gkey(file_path) 
    print("client: ", client)
    print("server: ", server)

def gkey(file_path):
    while True:
        try:
            key_file_path = file_path + '/publickey' #het is van belang dat je van meerdere variabelen 1 variabel maakt
            print(key_file_path)
            with open(file_path + '/publickey', 'r') as file:
                public = file.read()
            with open(file_path + '/privatekey', 'r') as file:
                private = file.read()
            return public, private
            print(test)
        except FileNotFoundError as error:
            print(error)
            print("Sleutel niet gevonden. Opnieuw proberen in 5 seconden...")
            sleep(5)

def keygen():
    Ans = input('Wil je nieuwe keys genereren? (Y/N): ')
    if Ans in ['y', 'Y']:
        print ("Keygen start")
        subprocess.run(['sudo', 'rm', file_path +'/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'rm', file_path +'/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        privatekey = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
        publickey = subprocess.check_output(f"echo '{privatekey}' | wg pubkey", shell=True).decode("utf-8").strip()
        with open(file_path +'/publickey', 'w') as f:
            f.write(publickey)
        with open(file_path +'/privatekey', 'w') as f:
            f.write(privatekey)
    else:
        print("Abort Keygen")

if __name__=="__main__":
     main()
