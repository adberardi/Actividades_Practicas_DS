import socket
import sys

#Crear socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Indicando dirección IP o dominio a conectarse, y por último el puerto.
server_address = ("localhost",10601)

#print("------- Nombre puerto {}, número {} ".format(*server_address))


def sendHelloIam():
    conn.send("helloiam usuario_2".encode())
    print("------ Enviando mensaje")
    msg = conn.recv(16)
    print("------- Mensaje recibido:"+format(msg))

try:
    conn.connect(server_address)
    #socket.create_connection(("localhost",10601))
    print("------- Conectando socket")
    sendHelloIam()
except OSError as identifier:
    print("------- Error se presntó:"+identifier)
finally:
    conn.close()
    print("------- Cerrando conexión")

print("Welcome!")
