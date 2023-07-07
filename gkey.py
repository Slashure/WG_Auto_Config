"""""""""
gkey.py
Keygen/Keygetter
Auteur: Victor Liu
Datum: 07-07-2023
Versie: 7.0 (eind)


Vereisten:
pip install python-wireguard

Documentatie:
Wireguard-pakket: https://pypi.org/project/python-wireguard/
Wireguard:        https://www.wireguard.com/embedding/

Dit script zorgt ervoor dat er keys gemaakt kunnen worden en dat de keys naar de auto config gestuurd worden
"""""""""

from time import sleep
import subprocess

def main():
    print('dit is de gkey functie script')
    keygen()
    file_path = input('wat is het pad naar de keys: ')
    #file_path = ('/home/user') #verander de pad naar de pad van de keys 
    client, server, = gkey(file_path) 
    print("client: ", client) #testprint
    print("server: ", server) #testprint

def gkey(file_path):
    while True:
        try:
            with open(file_path + '/publickey', 'r') as file:
                public = file.read()
            with open(file_path + '/privatekey', 'r') as file:
                private = file.read()
            return public, private
            print(test)
        except FileNotFoundError as error: #Als de file niet gevonden kan worden dan geeft het een error door
            print(error)
            print("Sleutel niet gevonden. Opnieuw proberen in 5 seconden...")
            sleep(5)

def keygen(): #In deze functies worden de Keys gegenereerd
    Ans = input('Wil je nieuwe keys genereren? (Y/N): ')
    if Ans in ['y', 'Y']:
        print ("Keygen start")
        subprocess.run(['sudo', 'rm', file_path +'/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #verwijderen van de publickey
        subprocess.run(['sudo', 'rm', file_path +'/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #verwijderen van de privatekey
        privatekey = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()#output in een variabel zetten
        publickey = subprocess.check_output(f"echo '{privatekey}' | wg pubkey", shell=True).decode("utf-8").strip()  #output in een variabel zetten
        with open(file_path +'/publickey', 'w') as f:
            f.write(publickey)
        with open(file_path +'/privatekey', 'w') as f:
            f.write(privatekey)
    else:
        print("Abort Keygen")

if __name__=="__main__":
     main()
