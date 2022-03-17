import socket
import json
#Per l'esecuzione di questo esercizio sono andato a sfogliare alcuni
#notebook che erano stati fatti l'anno scorso, i quali mi sono stati utili
#sia per ripassare alcuni concetti riguardanti il ciclo for sia per ripassare
#alcune funzioni, o almeno utilizzi/gestioni, delle tuple. Però ho completato 
#la parte finale a casa, e di conseguenza non sono riuscito a testare il
#programma: mi auguro che non abbia fatto alcun tipo di errore di battitura,
#non essendo riuscito appunto a visualizzare gli errori che mi avrebbero aiutato
#nell'individuazione degli eventuali refusi.
import pprint
from textwrap import indent

HOST='127.0.0.1'
PORT=65434
contatore=1
students={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[*] In ascolto su %s:%d "%(HOST, PORT))
    cs, address=s.accept()#accetta la conversione     	
    while True:
        print("Connessione a ", address)
        while True:
            data=cs.recv(1024)
            if not data:
                break
            data=data.decode() 
            data=data.strip()
            data=json.loads(data)
            comando=data['Comando']
            print ("[*] Received: %s" % data)
            #list : per vedere i voti inseriti
            #set /nomestudente : per inserire uno studente
            #put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente
            #get /nomestudente : per richiedere i voti di uno studente
            #exit : per chiudere solo il client
            #close : per chiudere sia client sia server
            #Digita il comando list; dizionario studenti eccetera.
	        #La close non è più da fare
            if comando=="#list":
                serialized_dict = json.dumps(students)
                cs.sendall(serialized_dict.encode())
            elif (comando.find('#set')!=-1):
                stringa=comando.split('/')
                nome=stringa[1]
                if nome in students:
                    cs.sendall("studente già presente".encode())
                else:
                    students[nome]=[]
                    cs.sendall("studente già inserito".encode())
            elif (stringa.find('#put')!=-1):
                presente=False
                stringhe=comando.split('/')
                nome=stringhe[1]
                materia=stringhe[2]
                if nome in students:
                    for stud, mat in students.items():
                        if (stud==nome):
                            for i in mat:
                                print(mat)
                                if (mat==i[0]):
                                    print (mat)
                                    presente=True
                if (presente==False):
                    voto=int(stringhe[3])
                    ore=int(stringhe[4])
                    mater=[materia, voto, ore]
                    students[nome].append(mater)
                    cs.sendall("inserimento appena effettuato".encode())
                else:
                    cs.sendall("trovata ridondanza con la materia".encode())
            elif (comando.find('#get')!=-1):
                stringaS=""
                stringa=comando.split('/')
                nome=stringa[1]
                if nome in students:
                    serialized_dict=json.dump(students[nome])
                    cs.sendall(serialized_dict.encode())
                else:
                    lista=["Lo studente non è stato trovato"]
                    serialized_dict=json.dumps(lista)
                    cs.sendall(serialized_dict.encode())
            else:
                cs.sendall("Il comando non è stato trovato. Ritenta".encode())ù
                print(cs.getpeername)
                pp=pprint.PrettyPrinter(indent=4)
                pp.pprint(students)

            cs.close()
            #fine
	