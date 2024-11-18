from multiprocessing import Process, Pipe
from random import randint


def bombo(pipe):
    numeros = []
    while True:
        if pipe.recv()==0:
            numero = randint(1, 100)
            while numero in numeros:
                numero = randint(1, 100)
            numeros.append(numero)
            print('El ', numero)
            pipe.send(numero)
        else:
            pipe.close()
            break
    #pipe.close()

def jugador(pipe):
    creditos = 10
    apuesta = randint(1,100)
    print("Apuesto por el ", apuesta)
    while creditos>0:
        pipe.send(0)
        creditos-=1
        numero = pipe.recv()
        if numero == apuesta:
            print("¡¡He ganado!!")
            pipe.send(1)
            break
        else:
            print("Me cachis!")
    pipe.close()

if __name__ == "__main__":
    pipe1, pipe2 = Pipe()

    p1 = Process(target=bombo, args=[pipe1])
    p2 = Process(target=jugador, args=[pipe2])

    p1.start()
    p2.start()
    p1.join()
    p2.join()