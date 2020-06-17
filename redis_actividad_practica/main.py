import threading
import redis
from redlock import Redlock


r = redis.Redis(host="localhost",port=6379,db=0)
r.set("pais","venezuela")
redis_server = [{"host":"127.0.0.1","port":6379,"db":0}]


def main():
    try:
        padlock = Redlock(redis_server)
        l = padlock.lock(r.get("pais"),1000)
        print("Pais: "+r.get("pais").decode("utf-8"))
        #Permite conocer el ttl de la variable
        print(str(l.validity))
        padlock.unlock(l)
    except redis.RedisError as identifier:
        print(identifier)



t1 = threading.Thread(name="Hilo_1",target=main)
t1.start()