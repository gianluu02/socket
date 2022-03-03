#FAULISI GIANLUCA
#calcolatrice client per calcoServer.py versione multithread
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=2

def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5 
    primoNumero=random.randInt(0,100)#Random primo numero
    operazione=random.randInt(0,3)#Random dell'operazione
    secondoNumero=random.randInt(0,100)#Random seconda operazione
    #STABILISCO IL NUMERO A UN'OPERAZIONE
    if operazione=="0": 
       operazione="+"
    elif operazione=="1":
       operazione="-"
    elif operazione=="2":
       operazione="*"
    elif operazione=="3":
       operazione="/"
    
    print(primoNumero,secondoNumero,operazione)

    #primoNumero=3
    #operazione="+"
    #secondoNumero=5

    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    #COMPONGO IL MESSAGGIO
    messaggio={'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero}
    #RICEVO
    messaggio=json.dumps(messaggio)


    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    
    
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for num in range(NUM_WORKERS):
        genera_richieste(num, SERVER_ADDRESS, SERVER_PORT)#GENERO LE RICHIESTE
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range(NUM_WORKERS):
        trd = threading.Thread(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT))
        # ad ogni iterazione appendo il thread creato alla lista threads
        threads.append(trd)
    # 5 avvio tutti i thread
    for thread in threads:
        thread.start()
    # 6 aspetto la fine di tutti i thread 
    for thread in threads:
        thread.join()
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    processes=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range(NUM_WORKERS):
        process = multiprocessing.Process(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT))
        # ad ogni iterazione appendo il thread creato alla lista threads
        processes.append(process)
    # 8 avvio tutti i processi
    for process in processes:
        process.start()
    # 9 aspetto la fine di tutti i processi 
    for process in processes:
        process.join()
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
