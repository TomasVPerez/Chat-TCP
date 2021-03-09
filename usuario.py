import socket
import threading

nickname = input("Elegi un nombre de usuario: ")

usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usuario.connect(("127.0.0.1", 55555))

def recibir():
    while True:
            try:
                mensaje = usuario.recv(1024).decode('ascii') #recibimos mensajes del servidor(q se comporta como usuario)
                if mensaje == 'NICK':
                    usuario.send(nickname.encode('ascii')) 
                    pass
                else:
                    print(mensaje) #si no recibimos la palabra clave vemos que quiere el servidor
            except:
                print("Ocurrio un error ") 
                usuario.close()
                break

def escribir():
    while True:
        mensaje = f'{nickname}: {input("")}' #esperamos input de los usuarios constantemente, o mandan mensaje o cierran el chat
        usuario.send(mensaje.encode('ascii')) #enviamos el mensaje al servidor (lo van a ver todos los usuarios por su funcion controlar)

recibirThread = threading.Thread(target=recibir) #usamos threads para ejecutar mas de una funcion a la vez
recibirThread.start()

escribirThread = threading.Thread(target=escribir)
escribirThread.start()



