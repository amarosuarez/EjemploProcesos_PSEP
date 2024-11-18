from multiprocessing import Process, Pipe

def proceso1(pipe):
    print("Enviando...")
    pipe.send("Hola proceso 2")
    pipe.close()

def proceso2(pipe):
    mensaje = pipe.recv()
    print("Recibido: ", mensaje)
    pipe.close()

if __name__ == "__main__":
    pipe1, pipe2 = Pipe()

    p1 = Process(target=proceso1, args=[pipe1])
    p2 = Process(target=proceso2, args=[pipe2])

    p1.start()
    p2.start()
    p1.join()
    p2.join()