#aqui se creara el servidor para comenzar la conexion


import SocketServer

class MiTcpHandler(SocketServer.BaseRequestHandler):
    #esto se llamara en cada conexion
    def handle(self):
        #se usa para recibir desde el cliente
        self.oracion=self.request.recv(1024).strip()
        #esto leera la cantidad de caracteres que tienen la oracion
        self.num=len(self.oracion)
        self.request.send(str(self.num))
        print("Cliente 1 dice:",self.oracion,"caracteres recibidos : ",self.num)




def main():

    print("Servidor 1.0\n")
    host="localhost"
    port=9999

    server1=SocketServer.TCPServer((host,port),MiTcpHandler)
    print("Servidor Corriendo...")
    server1.serve_forever()#fucnionara hasta que se cierre el programa

main()
