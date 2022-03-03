import socket
import json

HOST="127.0.0.1"
PORT=22006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    students={
        "Giuseppe Gallo ":[("Matematica", 9, 0), ("Italiano", 7, 3),("Inglese", 7.5, 4), ("Storia", 7.5, 4), ("Geografia", 5, 7)]
        "Antonio Barbera":[("Matematica", 8, 1), ("Italiano", 6, 1),("Inglese", 9.5, 0), ("Storia", 8, 2), ("Geografia", 8, 1)]
        "Nicola Spina ":  [("Matematica", 7.5, 2), ("Italiano", 6, 2),("Inglese", 4, 3), ("Storia", 8.5, 2), ("Geografia", 8, 2)]
    }
    contatore=1
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address = s.accept()
    with clientsocket as cs:
        print("Connessione da ", address)
        while True:
            data=cs.recv(1024)
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            stringa=data['stringa']
            if stringa != "KO":
                ris="Messaggio numero " + str(contatore) + ": " + stringa
                contatore += 1
            else:
                ris='Ricevuto "KO" dal server, chiudo la connessione con il client.'
            cs.sendall(ris.encode("UTF-8"))

    while True:
        clientsocket, address = cs.accept()
        print("\Connessione ricevuta da %s" str(address))
        while True:
            data=c.recv(1024)
            data=data.decode()
            data=data.strip()
            print ("[*]Received: %s" % data)

            if data == "#list" :
            elif data.find('#get') != -1:
            elif data.find('#put') != -1:
            elif data.find('#set') != -1:
            elif data == "#close":
            print (clientsocket.getpeername())
            pp=pprint.PrettyPrinter(indent=4)
            pp.pprint(students)
            clientsocket.close()

            print("Stringa ricevuta "+ stringa)
          if stringa!="KO":
             ris=stringa+" "+str(contatore)
             contatore+=1
             ris=str(ris)
             clientsocket.sendall(ris.encode("UTF-8"))