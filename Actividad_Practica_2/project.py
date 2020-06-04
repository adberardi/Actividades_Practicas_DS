import threading
from time import sleep

def main():
	#Se guarda el nombre del hilo.
	thread_name = threading.current_thread().getName()
	#Se aplica el bloqueo. El contador interno decrementa a "0".
	flag = toLock.acquire()
	try:
		#Se valida por el nombre el hilo que función determinada a ejecutar.
		#En este caso se usa un solo archivo, en el que ambos hilos pueden tener acceso.
		#Uno guardará un nuevo dato al archivo, y el otro mostrará toda la información que contenga este.
		#El archivo a usar se llamó "data.txt"
		if thread_name == "Hilo_2":
			readFile()
		if thread_name == "Hilo_1":
			saveFile()
	except Exception as e:
		print("Se presento error en ejecución",e)
	finally:
		if flag:
			#Si el bloqueo está activo se libera. El contador interno incrementa "1"
			toLock.release()
		#Finaliza la ejecución de la función principal.
		print("-->Recurso liberado! del hilo ",thread_name)

def saveFile():
    #Se guarda la nueva información en el archivo.
	try:
		#Se emplea sleep() para prolongar los tiempos de ejecución entre ambos hilos,
		# y obtener una salida de datos organizada en la terminal.
		#Para la función "saveFile" se le asignó un tiempo de espera de "1" segundo.
		#Mientras que en la función "readFile" se le asignó un tiemp de "2" segundos.
		sleep(4)
		pf = open("./data.txt","r+")
		cont = 1
		for line in pf:
			#Recorre todo el archivo linea por linea.
			#La variable "cont" corresponde al total de lineas que posee el archivo antes de ser modificado.
			cont = cont+1
		#Se almacena el nuevo dato en el archivo "data.txt".
		pf.write("Dato: "+str(cont)+"\n")
		pf.close()
	except Exception as e:
		print("Error al guardar dato |",e)
	finally:
		print("Guardando...... ")

def readFile():
    #Lee el archivo que fue modificado por el otro hilo.
	try:
		#Se emplea sleep() para prolongar los tiempos de ejecución entre ambos hilos,
		sleep(2)
		pf = open("./data.txt","r")
		print("	Información dentro del Archivo: \n",pf.read())
		pf.close()
	except Exception as e:
		print("Archivo data.txt no existe ",e)



#Invocación de hilos

#Se crean los hilos
t1 = threading.Thread(name="Hilo_1",target=main)
t2 = threading.Thread(name="Hilo_2",target=main)

#Se iniciliaza el Semáforo en "1".
padlock = 1
toLock = threading.Semaphore(padlock)


#Se inician los hilos creados anteriormente
t1.start()
t2.start()

#Se indica con el Join que el programa principal espere ambos hilos para finalizar la ejecución en su totalidad.
#en caso de que no se emplee el "join", los hilos terminan de forma separada.
t1.join()
t2.join()
print(":::: Ejecución terminada")
