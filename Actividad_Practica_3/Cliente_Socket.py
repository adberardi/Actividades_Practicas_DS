
#author: Antonio Berardi
import socket
import sys
import threading
import base64
from subprocess import check_output,run,STDOUT,CalledProcessError,call

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



def thread_catch():
    #Creando el socket para establecer la conexión udp
    socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_address_UDP = ("localhost",15601)
    socket_udp.bind(server_address_UDP)
    result = socket_udp.recv(460).decode("utf-8")
    print(format(result)+"\n")

    #resultado = call(["echo",'"'+result+'"',"|","base64","-d"])
    resultado = base64.decodebytes(result.encode("utf-8"))
    print(resultado)
    # result_string = base64.b64decode(result.decode("utf-8"))
    # print("/////// "+result_string)
    # pf = open("data.txt","w")
    # pf.write(result.decode("utf-8"))
    # pf.close()
    socket_udp.close()

def giveMeMsg(): 
    try:
        #Se crean los hilos
        t1 = threading.Thread(name="Hilo_1",target=thread_catch)
        t1.start()
        result_givememsg = sendMsg("givememsg 15601")
        t1.join()
        
        #res = run(["python3","Socket_UDP.py"],stderr=STDOUT)
        #print(res.returncode)
        print("------- Mensaje recibido:"+format(result_givememsg))
    except CalledProcessError as identifier_check_output:
        print(identifier_check_output)

def chkmsg():
    result_chkmsg = sendMsg("givememsg udp_port")
    print("------- Mensaje recibido:"+format(result_chkmsg))

def bye():
    result_bye = sendMsg("bye")
    print("------ Mensaje de despedida!------"+result_bye)




def main():
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





main()
print("     Ejecución finalizada!    ")
