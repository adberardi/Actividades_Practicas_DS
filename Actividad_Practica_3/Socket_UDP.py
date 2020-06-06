
#author: Antonio Berardi
import socket
import sys
from subprocess import check_output, STDOUT, CalledProcessError

#Creando el socket para establecer la conexión udp
socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Abriendo archivo que contendrá el mensaje en el servidor.

try:
    pf = open("data.txt","w")
    server_address = ("localhost",15006)
    # msg = "givememsg 15006"
    # socket_udp.sendto(msg.encode(),server_address)
    result = socket_udp.recvfrom(445)
    pf.write(format(result)+"\n")
    #pf.write(check_output(["nc","-u","-l","-p","15006"],stderr=STDOUT, timeout=1000))
    #pf.write("Socket_UDP!\n")
except CalledProcessError as identifier_check_output:
    print(identifier_check_output)
""" finally:
    socket_udp.close() """


print("Socket_UDP!")
pf.close()