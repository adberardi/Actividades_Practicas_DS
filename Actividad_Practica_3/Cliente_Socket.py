
#author: Antonio Berardi
import socket
import sys
import os
import threading
import base64
import hashlib
from subprocess import Popen,PIPE,CalledProcessError,call, check_output

#Crear socket.
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Indicando dirección IP o dominio a conectarse, y por último el puerto.
server_address = ("192.168.24.1",10601)
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
    result_helloIam = sendMsg("helloiam adberardi.13")
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
    # socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # server_address_UDP = ("192.168.24.1",15601)
    #socket_udp.bind(server_address_UDP)
    #socket_udp.sendto(server_address_UDP)
    #result = socket_udp.recv(444)
    #resultado = base64.decodebytes(result)
    #os.system("nc -u -l -p 15601")
    resultado = Popen(["nc", "-ulp 15601"],stdout=PIPE)
    r = resultado.communicate()
    #result = subprocess.check_output(["nc","-ulp","15601"])
    # pf = open("data.txt","w")
    # pf.write(str(result))
    # pf.close()
    #resultado = os.system("echo -n "+str(result)+" | base64 -d")
    #resultado = base64.decodebytes(str(result).encode("utf-8"))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Soy resultado"+format(r[0])+"\n")
    resultado_msg = Popen(["echo", "-n",r[0],"|","base64 -d"],stdout=PIPE)
    r_m = resultado_msg.communicate()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Soy r_m-> "+format(base64.decodebytes(r[0]).decode("utf-8"))+"\n")
    md = hashlib.md5()
    md.update(base64.b64decode(r[0].decode("utf-8")))
    #md.update("Lo unico que se interpone entre ti y tu sueo, es la voluntad de intentarlo y la creencia de que en realidad es posible. Joel Brown\n".encode("utf-8"))
    print(str(md.hexdigest()))

    #socket_udp.close()

def giveMeMsg(): 
    try:
        #Se crean los hilos
        t1 = threading.Thread(name="Hilo_1",target=thread_catch)
        t1.start()
        result_givememsg = sendMsg("givememsg 15601")
        t1.join()
        print("------- Mensaje recibido: givememsg "+format(result_givememsg))
    except CalledProcessError as identifier_check_output:
        print(identifier_check_output)


def chkmsg():
    #result_chkmsg = sendMsg("chkmsg d27293aa83074dfd5c6289f35efafeda")
    
    result_chkmsg = sendMsg("chkmsg "+md)
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
