#Aqui escribiremos nuestro cliente que se conectara al servidor indicado
#clienteBasico
import socket, time

print("cliente 1.0")
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))
oracion=raw_input("Ingrese una oracion:")
socket1.send(oracion)
num=socket1.recv(1024)
print('Caracteres Enviados:',num)
tiempo=raw_input("Presione enter para terminar")
print "conexion terminada"
socket1.close()
