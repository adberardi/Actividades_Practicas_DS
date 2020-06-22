import threading
import redis
from redlock import Redlock


def main():
    try:
        #Se obtiene el nombre del hilo.
        n = threading.currentThread().getName()
        #print(str(r.smembers("Hilo")))
        #Se actualiza el recurso con el número de Hilo
        r.sadd("Hilo",int(n[5]))

        #Se bloquea el recurso
        l = padlock.lock(str(r.smembers("Hilo")),4000)

        #Se imprime el contenido del recurso bloqueado
        print("Soy: "+ n +". Datos: "+l.resource)

        #Se libera el recurso.
        padlock.unlock(l)

    except Exception as identifier:
        print(identifier)


#Se establece la conexión del servidor redis indicando dirección o nombre del host, puerto y base de datos a la que se conectará.
r = redis.Redis(host="localhost",port=6379)

#Se establece la dirección y puerto del servidor redis para emplear el manejo de bloqueos.
redis_server = [{"host":"127.0.0.1","port":6379}]
padlock = Redlock(redis_server)

#El recurso a compartir con el resto de los hilos.
r.sadd("Hilo",0)

#Cada hilo representará una computadora.
t1 = threading.Thread(name="Hilo_1",target=main)
t2 = threading.Thread(name="Hilo_2",target=main)
t3 = threading.Thread(name="Hilo_3",target=main)
t4 = threading.Thread(name="Hilo_4",target=main)
t5 = threading.Thread(name="Hilo_5",target=main)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

#Se elimina los datos almacenados en el par clave-valor Hilo del servidor redis.
r.srem("Hilo","0")
r.srem("Hilo","1")
r.srem("Hilo","2")
r.srem("Hilo","3")
r.srem("Hilo","4")
r.srem("Hilo","5")