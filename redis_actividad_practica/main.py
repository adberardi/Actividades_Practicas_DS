import redis 

r = redis.Redis()
r.mset({"Venezuela":"Caracas","España":"Madrid","Italia":"Roma"})

print("Insertando en SET.......")

print("Buscando capital de Venezuela: "+format(r.get("Venezuela")))