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
        l = padlock.lock(r.get("pais"),3000)
        print("Pais: "+r.get("pais").decode("utf-8"))
        #Permite conocer el ttl de la variable
        #print(str(l.validity))
        
        padlock.unlock(l)
    except redis.RedisError as identifier:
        print(identifier)





t1 = threading.Thread(name="Hilo_1",target=main)
t2 = threading.Thread(name="Hilo_2",target=main)
t3 = threading.Thread(name="Hilo_3",target=main)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()