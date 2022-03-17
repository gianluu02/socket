#Importo il socket ed il json
import socket
import json
import pprint

#Dichiaro una porta e gli assegno un valore (127.0.0.1) e dopo una porta (65434)
HOST="127.0.0.1"
PORT=65434

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        comandi=input('Comandi che puoi utilizzare:\n #list: per vedere i voti inseriti;\n #set /nomestudente: per inserire uno studente;\n #put /nomestudente/materia/voto/ore: per aggiungere i voti della materia allo studente;\n #get /nomestudente: per richiedere i voti di uno studente;\n #exit: per chiudere solo il client.\n')
        messaggio={
            'Comando': comandi
        }
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        if comandi=='#list':
            stud_dict=json.loads(data)
            print ("Dizionario studenti ")
            pp=pprint.PrettyPrinter(indent=4)
            pp.pprint(stud_dict)
        elif comandi=='exit':
            print(data.decode())
            break
        elif comandi.find('#get')!=-1:
            deserialized_dict=json.load(data)
        else:
           deserialized_dict=data.decode()
           print(data.decode())#deserialized_dict
    s.close()