import threading
import time
import redis
from redlock import Redlock

def acces_resource():
    print("Hello world")

def main():
    try:
        n = threading.currentThread().getName()
        print(str(r.smembers("Hilo")))
        r.sadd("Hilo",int(n[5]))
        l = padlock.lock(str(r.smembers("Hilo")),1000)
        #print(l.resource)
        #time.sleep(int(n[5]))
        #r.incrby("pais",int(l.resource.decode("utf-8")))
        #r.incr("pais")
        #print(" El primero en llegar fue: "+l.resource.decode("utf-8"))
        print("Soy: "+ n +". Datos: "+l.resource)
        padlock.unlock(l)


    except Exception as identifier:
        print(identifier)



r = redis.StrictRedis(host="localhost",port=6379,db=0)
redis_server = [{"host":"127.0.0.1","port":6379,"db":0}]
padlock = Redlock(redis_server)
#r.set("pos",1)
r.sadd("Hilo",0)
print(str(r.smembers("Hilo")))
#l = padlock.lock(r.get("pos"),1000)
# v = int(l.resource.decode("utf-8"))+1
# l.resource = str(v).encode("utf-8")

t1 = threading.Thread(name="Hilo_1",target=main)
t2 = threading.Thread(name="Hilo_2",target=main)
t3 = threading.Thread(name="Hilo_3",target=main)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

r.srem("Hilo","0")
r.srem("Hilo","1")
r.srem("Hilo","2")
r.srem("Hilo","3")
