import socket
import pickle

class RankingClient:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        self.socket.connect((self.host, self.port))

    def enviar_peticion(self, peticion):
        try:
            self.socket.send(pickle.dumps(peticion))
            byRec = self.socket.recv(1024)
            print(str(byRec))
            respuesta = None
            if peticion == "load":
                respuesta = pickle.loads(byRec)
            elif peticion[0] == "save":
                respuesta = byRec
            return respuesta
        except Exception as e:
            print(f"Error en peticion: {e}")
            raise

    def cerrar_conexion(self):
        self.socket.close()

    def cargar(self):
        self.conectar()
        peticion = "load"
        respuesta = self.enviar_peticion(peticion)
        print("Datos cargados:", respuesta)
        self.cerrar_conexion()
        return respuesta

    def guardar(self, listaDePuntajes):
        self.conectar()
        peticion = ("save", listaDePuntajes)
        respuesta = self.enviar_peticion(peticion)
        print("Respuesta de guardado:", respuesta)
        self.cerrar_conexion()