
#author: Antonio Berardi
import socket
import sys
import threading
import base64
import hashlib
from subprocess import Popen,PIPE,CalledProcessError

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

#Valida que el número sea múltiplo de 4, para que la librería base64 no tenga problemas de conversión.
def validate_multiple_four(number_to_validate):
    if number_to_validate%4 != 0:
        number_to_validate = number_to_validate * 4
    return number_to_validate

#Función encargada de construir el mensaje de obtener la longitud del mensaje.
def msgLen():
    result_msglen = sendMsg("msglen")
    length_message = result_msglen.decode("utf-8")
    print(length_message[3:6])
    # lm = validate_multiple_four(int(length_message[3:6]))
    # print("//////// :",lm)
    #print("------- Mensaje recibido:"+format(result_msglen[3:6]))



def thread_catch():
    #Creando el socket para establecer la conexión udp
    socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address_UDP = ("localhost",15006)
    socket_udp.bind(server_address_UDP)
    result = socket_udp.recv(448)
    #print(format(result)+"\n")
    #resultado = Popen(["echo","-n",'"'+result.decode("utf-8")+'"',"|","base64","-d"],stdout = PIPE)
    resultado = base64.decodebytes(result)
    print(format(resultado))
    md = hashlib.md5()
    md.update(resultado)
    # r2 = "Lorem ipsum dolor sit amet, cónsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat noñ proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "
    # r2 = r2.encode("utf-8")
    #md.update(r2)
    print(str(md.hexdigest()))
    # pf = open("data.txt","w")
    # pf.write(resultado.decode("utf-8"))
    # pf.close()
    socket_udp.close()

def giveMeMsg(): 
    try:
        #Se crean los hilos
        t1 = threading.Thread(name="Hilo_1",target=thread_catch)
        t1.start()
        result_givememsg = sendMsg("givememsg 15006")
        t1.join()
        print("------- Mensaje recibido: givememsg "+format(result_givememsg))
    except CalledProcessError as identifier_check_output:
        print(identifier_check_output)


def chkmsg():
    result_chkmsg = sendMsg("chkmsg "+str(md))
    print("------- Mensaje recibido:"+format(result_chkmsg))

def bye():
    result_bye = sendMsg("bye")
    print("------ Mensaje de despedida!------"+result_bye.decode("utf-8"))




def main():
    try:
        conn.connect(server_address)
        #socket.create_connection(("localhost",10601))
        print("------- Conectando socket")
        helloIam()
        msgLen()
        giveMeMsg()
        chkmsg()
        bye()
    except OSError as identifier:
        print(identifier)
    finally:
        conn.close()
        print("------- Cerrando conexión")




lm = 0
md = ""
main()
print("     Ejecución finalizada!    ")
