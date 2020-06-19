import threading
import time
import redis
import os
from redlock import Redlock

def acces_resource():
    print("Hello world")

def main():
    try:
        r = redis.Redis(host="localhost",port=6379,db=0)
        r.set("pais","venezuela")
        redis_server = [{"host":"127.0.0.1","port":6379,"db":0}]
        padlock = Redlock(redis_server)
        l = padlock.lock(r.get("pais"),5000)
        n = threading.currentThread().getName()
        #Permite conocer el ttl de la variable
        #print(str(l.validity))

        if l.validity > 0 and n != "Hilo_2":
            print("Soy el hilo: "+ n +". Pais: "+r.get("pais").decode("utf-8"))
        else:
            time.sleep(5)

        padlock.unlock(l)
        
    except redis.RedisError as identifier:
        print(identifier)





t1 = threading.Thread(name="Hilo_1",target=main)
t2 = threading.Thread(name="Hilo_2",target=main)
t3 = threading.Thread(name="Hilo_3",target=main)
# t4 = threading.Thread(name="Hilo_4",target=main)
# t5 = threading.Thread(name="Hilo_5",target=main)

t1.start()
t2.start()
t3.start()
# t4.start()
# t5.start()

t1.join()
t2.join()
t3.join()
# t4.join()
# t5.join()