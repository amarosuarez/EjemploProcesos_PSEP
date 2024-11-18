from multiprocessing import Process, Queue

from random import randint
from time import sleep


def producer(q, id):
    # Envia 10 mensajes
    for i in range(10):

        if q.full():
            print(f"Proceso {id}: La cola esta llena")

        # Envia el mensaje número 1
        q.put(i)
        print(f"Proceso {id}:" + str(i) + " Enviado")
        sleep(randint(1, 5))

    # Envia el mensaje None (!True)
    q.put(None)
    print(f"El productor {id} ha acabado")


def consumer(q, id):
    while True:

        if q.empty():
            print(f"Consumidor {id}: Cola vacía")

        # Recibe el mensaje
        item = q.get()

        # No hay más elementos
        if item is None:
            break

        print(f"Consumidor {id}:" + str(item) + " Recibido")

        sleep(randint(1, 5))
    print(f"El consumidor {id} ha acabado")


if __name__ == "__main__":

    productores = []

    consumidores = []

    # Crea una cola
    queue = Queue(maxsize=3)

    # Se crean los procesos Productor y Consumidor
    for i in range(3):
        productores.append(Process(target=producer, args=(queue, i,)))
        consumidores.append(Process(target=consumer, args=(queue, i,)))

    # Se inician los procesos
    for i in range(3):
        productores[i].start()

    # Se inician los procesos
    for i in range(3):
        consumidores[i].start()

    # Se espera a que termine el proceso 1
    for i in range(3):
        productores[i].join()

    # Se espera a que termine el proceso 2
    for i in range(3):
        consumidores[i].join()

    print("Todas las tareas han acabado")