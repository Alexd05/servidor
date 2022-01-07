import socket 

mi_socket = socket.socket()
mi_socket.connect( ('localhost', 8080) )

mi_socket.send("hola")
response = mi_socket.recv(1024)

print(response)
mi_socket.close()
