import socket
import pickle

class RankingServer:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 12345
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        self.puntajes = []

    # Abre conexión
    def abrir(self):
        print(f"Escucha en {self.host}:{self.port}")
        while True:
            cliente_socket, dir = self.socket.accept()
            print(f"Conexión aceptada en {dir}")
            self.manejo_cliente(cliente_socket)

    # Lógica de manejo de clientes
    def manejo_cliente(self, cliente_socket):
        try:
            data = cliente_socket.recv(1024)
            if data:
                peticion = pickle.loads(data)
                # Si pide carga, carga los datos. Si pide guardar, guarda los datos.
                if peticion == "load":
                    respuesta = self.unpickle_archivo_de_puntajes()
                elif peticion[0] == "save":
                    self.pickle_archivo_de_puntajes(peticion[1])
                    respuesta = "Guardado exitoso"
                else:
                    respuesta = "Petición inválida"
                print(respuesta)
                cliente_socket.send(pickle.dumps(respuesta))
        except Exception as e:
            print(f"Error en recibir peticion: {e}")
            raise
        finally:
            cliente_socket.close()

    def pickle_archivo_de_puntajes(self, lista_de_puntajes):
        try:
            with open("puntajesFile.pkl", 'wb') as puntaje_save_file:
                pickle.dump(lista_de_puntajes, puntaje_save_file)
        except Exception as e:
            print(f"Error pickling: {e}")

    def unpickle_archivo_de_puntajes(self):
        try:
            with open("puntajesFile.pkl", 'rb') as puntaje_load_file:
                puntaje_loaded = pickle.load(puntaje_load_file)
                self.puntajes = puntaje_loaded
            return puntaje_loaded
        except Exception as e:
            print(f"Error unpickling: {e}")
            return list()
    
    def __del__(self):
        self.socket.close()

if __name__ == "__main__":
    server = RankingServer()
    server.abrir()
