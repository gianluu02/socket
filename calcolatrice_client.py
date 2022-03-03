import socket
import json

HOST="127.0.0.1"
PORT=22006

def invia_comandi(sock_service):
    while True:
        primoNum=input("Inserisci il primo numero exit() per uscire: ")
        if primoNum=="exit()":
            break
        primoNum=float(primoNum)
        operazione=input("Inserisci l'operazione (+,-,*,/,%): ")
        secondoNum=float(input("Inserisci il secondo numero: "))
        messaggio={
            'primoNum':primoNum, 
            'operazione':operazione, 
            'secondoNum':secondoNum
        }
         #trasforma l'oggetto in una stringa
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(1024)
        print("Ris: ", data.decode())

def connessione_server(address,port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(HOST,PORT)