import socket
import json
import os
import sys
import signal
import csv
import threading
import time
from Moneda import Moneda 
from UDPClient import Client


class PService(threading.Thread):
    def __init__(self):
        super().__init__()
        self.shutdown_flag = threading.Event()
       
    def run(self):
        c_sock = Client(10000)     
        print('Thread Socket Client #%s started' % self.ident)
        
        while not self.shutdown_flag.is_set():            
            #Se lee el archivo y se convierte a lista
            data = Moneda.convert_json_data("config.txt")
            
            #convertimos la lista a JSON
            send_divisas = Moneda.generate_json(data)
            #envío al servidor el mensaje
            c_sock.SendtoServer(send_divisas)
            value = c_sock.ReceiveServer() 
            if value == True:
                print("OK")
            self.shutdown_flag.wait(30)  
           
        print ("Socket Cliente Closed")
        c_sock.close()
        print('Thread Socket Client #%s Stopped' % self.ident)

class ServiceExit(Exception):
    pass

def service_shutdown(signal_receive,frame):
    print ("captured signal(Crtl+C):%d"% signal_receive)
    raise ServiceExit()

def main():
    signal.signal(signal.SIGINT,service_shutdown)
    print ("starting the main program")

    try:
        pS1= PService()
        pS1.start()

        while True:
            time.sleep(0.5)
    except ServiceExit:

        pS1.shutdown_flag.set()
        pS1.join()
        
    print ("Finalizando programa")
main()

#m = Main()
#m.main()