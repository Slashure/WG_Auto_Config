""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
get_keys functie
Auteur: Victor Liu
Datum: 29-06-2023
Versie: 3.0

Dit programma is een kleine functie die keys ophaalt uit een bestand.
de functie is bedoeld om in een groter programma gebruikt te worden,
voor een automatische wireguard configurator.

Disclaimer:
Deze configurator is mede mogelijk gemaakt door ChatGPT, een AI-taalmodel getraind door OpenAI.
Voor veilig gebruik van dit Python-script dienen de sleutels te worden aangepast en vertrouwelijk te blijven.
Ik aanvaard geen enkele verantwoordelijkheid voor eventuele schade die kan ontstaan door het gebruik van dit script.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from time import sleep
import subprocess

def main():
    print('dit is de gkey functie script')
    keygen()


    #file_path = input('wat is het pad naar de keys: ')
    file_path = ('/home/vicc')
    print('Dit is de path', file_path)
    client, server, = gkey(file_path) 
    print("client: ", client)
    print("server: ", server)
    print("test gkey", gkey)

def gkey(file_path):
    """
    input: path naar de folder waar de wgclient.key en wgserver.pubstaan.
    output: twee strings met de keys
    gebruik: cient, server = get_keys(file_path)
    """
    while True:
        try:
            key_file_path = file_path + '/publickey' #het is van belang dat je van meerdere variabelen 1 variabel maakt
            print(key_file_path)
            with open(file_path + '/publickey', 'r') as file:
                client = file.read()
            with open(file_path + '/privatekey', 'r') as file:
                server = file.read()
            return client, server
            print(test)
        except FileNotFoundError as error:
            print(error)
            print("Sleutel niet gevonden. Opnieuw proberen in 5 seconden...")
            sleep(5)

def keygen():
    Ans = input('Wil je nieuwe keys genereren? (Y/N): ')
    if Ans in ['y', 'Y']:
        print ("Keygen start")
        print("pizza")

        subprocess.run(['sudo', 'rm', '/home/vicc/publickey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'rm', '/home/vicc/privatekey'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        privatekey = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
        publickey = subprocess.check_output(f"echo '{privatekey}' | wg pubkey", shell=True).decode("utf-8").strip()
        print(publickey)
        print(privatekey)
        with open('/home/vicc/publickey', 'w') as f:
            f.write(publickey)
        with open('/home/vicc/privatekey', 'w') as f:
            f.write(privatekey)
    else:
        print("Abort Keygen")


def test():
    """
    hier is de uitleg van de code...
    """
    while True:
        print('hallo wereld!')
        return 'hallo wereld'

if __name__=="__main__":
     main()
