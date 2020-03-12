from zeep import Client
from zeep.wsse.username import UsernameToken

exec(open("nrdm_ws_credentials.py").read())

def main ():

    client = Client('https://services.rods.pitt.edu/nrdm-ws-2.2-SNAPSHOT/NRDMService?wsdl',wsse=UsernameToken(nrdm_username, nrdm_password))
    print("Is Alive?", client.service.isAlive())


if __name__ == '__main__':
    main()


