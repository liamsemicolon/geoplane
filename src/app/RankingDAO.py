import pickle
from Puntaje import Puntaje
class RankingDAO:
    def __init__(self):
        self.archivo = "dao/datos/puntajesFile.pkl"
    
    def pickleArchivoDePuntajes(self, listaDePuntajes):
        try:
            puntajeSaveFile = open(self.archivo,'wb')
            pickle.dump(listaDePuntajes, puntajeSaveFile)
            puntajeSaveFile.close()
        except EOFError as e:
            print("algo salio mal pickling: " + str(e))

    def unpickleArchivoDePuntajes(self):
        try:
            puntajeLoadFile = open(self.archivo,'rb')
            puntajeLoaded = []
            puntajeLoaded = pickle.load(puntajeLoadFile)
            puntajeLoadFile.close()
            return puntajeLoaded
        except EOFError as e:
            print(e)