#author: Antonio Berardi

import socket
import sys
from subprocess import check_output, STDOUT, CalledProcessError

#Crear socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Indicando dirección IP o dominio a conectarse, y por último el puerto.
server_address = ("localhost",10601)
#print("------- Nombre puerto {}, número {} ".format(*server_address))



#Función encargada de enviar el mensaje al servidor.
def sendMsg(message):
    print("------ Enviando mensaje")
    conn.send(message.encode())
    msg = ""
    msg = conn.recv(16)
    return msg

#Función encargada de construir el mensaje de autenticación con el servidor.
def helloIam():
    result_helloIam = sendMsg("helloiam usuario_2")
    print("------- Mensaje recibido:"+format(result_helloIam[0:2]))

#Función encargada de construir el mensaje de obtener la longitud del mensaje.
def msgLen():
    result_msglen = sendMsg("msglen")
    print("------- Mensaje recibido:"+format(result_msglen[3:6]))

def giveMeMsg():
    result_givememsg = sendMsg("givememsg 15006")
    try:
        r = check_output(["python3","Socket_UDP.py"],stderr=STDOUT)
        print("------- Resultado:"+format(r))
    except CalledProcessError as identifier_check_output:
        print(identifier_check_output)
    finally:
        print("------- Mensaje recibido:"+format(result_givememsg))

def chkmsg():
    result_chkmsg = sendMsg("givememsg udp_port")
    print("------- Mensaje recibido:"+format(result_chkmsg))

def bye():
    pass

try:
    conn.connect(server_address)
    #socket.create_connection(("localhost",10601))
    print("------- Conectando socket")
    helloIam()
    msgLen()
    giveMeMsg()
except OSError as identifier:
    print(identifier)
finally:
    conn.close()
    print("------- Cerrando conexión")

print("Welcome!")
