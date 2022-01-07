import socket

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 8080) )
mi_socket.listen(2)

while True:
    conection, addr = mi_socket.accept()
    print("Se establecio la conexión correctamente".encode())
    print(addr)

    peticion = conection.recv(1024)
    print(peticion)

    conection.send("es el servidor se conecto de forma correcta")
    conection.close()
