""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
get_keys functie
Auteur: Kasper van der Mark
Datum: 29-03-2023
Versie: 1.0

Dit programma is een kleine functie die keys ophaalt uit een bestand.
de functie is bedoeld om in een groter programma gebruikt te worden,
voor een automatische wireguard configurator.

Disclaimer:
Deze configurator is mede mogelijk gemaakt door ChatGPT, een AI-taalmodel getraind door OpenAI.
Voor veilig gebruik van dit Python-script dienen de sleutels te worden aangepast en vertrouwelijk te blijven.
Ik aanvaard geen enkele verantwoordelijkheid voor eventuele schade die kan ontstaan door het gebruik van dit script.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from time import sleep

def main():
    print('dit is de gkey functie script')
    file_path = input('wat is het pad naar de keys: ')
    #file_path = ('/etc/wireguard')
    print('Dit is de path', file_path)
    client, server, test = gkey(file_path) 
    print("client: ", client)
    print("server: ", server)
    print("test", test)
    print("test gkey," gkey)

def gkey(file_path):
    """
    input: path naar de folder waar de wgclient.key en wgserver.pubstaan.
    output: twee strings met de keys
    gebruik: cient, server = get_keys(file_path)
    """
    while True:
        try:
            key_file_path = file_path + '/wgclient,key' #het is van belang dat je van meerdere variabelen 1 variabel maakt
            print(key_file_path)
            with open(file_path + '/wgclient.key', 'r') as file:
                client = file.read()
            with open(file_path + '/wgserver.pub', 'r') as file:
                server = file.read()
            with open(file_path + '/test.txt','r') as file: 
                test = file.read()
            return client, server, test
            print(test)
        except FileNotFoundError as error:
            print(error)
            print("Sleutel niet gevonden. Opnieuw proberen in 5 seconden...")
            sleep(5)

def test():
    """
    hier is de uitleg van de code...
    """
    while True:
        print('hallo wereld!')
        return 'hallo wereld'

if __name__=="__main__":
     main()
