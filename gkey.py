"""
gkey.py
key generator/key getter
Auteur: Victor Liu
Datum: 30-03-2023
Versie: 6.1

Dit script zorgt ervoor dat er keys gemaakt kunnen worden en dat de keys naar de auto config gestuurd worden
"""
from time import sleep
import subprocess

def main():
    print('dit is de gkey functie script')
    #file_path = input('wat is het pad naar de keys: ')
    file_path = ('/home/vicc') #verander de pad naar de pad van de keys 
    client, server, = gkey(file_path) 

def gkey(file_path):
    keygen()
    while True:
        try:
            with open(file_path + '/publickey', 'r') as file:
                client = file.read()
            with open(file_path + '/privatekey', 'r') as file:
                server = file.read()
            return client, server
            
        except FileNotFoundError as error: #Als de file niet gevonden kan worden dan geeft het een error doors`Ss`
            print(error)
            print("Sleutel niet gevonden. Opnieuw proberen in 5 seconden...")
            sleep(5)

def keygen(): #In deze functies worden de Keys gegenereerd
    Ans = input('Wil je nieuwe keys genereren? (Y/N): ')
    if Ans in ['y', 'Y']: #Wacht op de yes command van de user
        print ("Keygen start")
        subprocess.run(['sudo', 'rm', '/home/vicc/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #verwijderen van de publickey
        subprocess.run(['sudo', 'rm', '/home/vicc/privatekey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #verwijderen van de privatekey
        privatekey = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip() #output in een variabel zetten
        publickey = subprocess.check_output(f"echo '{privatekey}' | wg pubkey", shell=True).decode("utf-8").strip() #output in een variabel zetten
        with open('/home/vicc/publickey', 'w') as f: #bestand maken
            f.write(publickey) #Key in de bestand schrijven
        with open('/home/vicc/privatekey', 'w') as f: #bestand maken
            f.write(privatekey) #Key in de bestand schrijven
    else:
        print("Abort Keygen") #message sturen als iemand iets anders dan y,Y intikt

if __name__=="__main__":
     main()
