import pickle
from Localizacion import Localizacion
class LocalizacionDAO:
    def __init__(self):
        self.archivo = "dao/datos/localizacionesFile.pkl"
    
    def pickleArchivoDeLocalizaciones(self, listaDeLocalizaciones):
        try:
            localizacionSaveFile = open(self.archivo,'wb')
            pickle.dump(listaDeLocalizaciones, localizacionSaveFile)
            localizacionSaveFile.close()
        except EOFError as e:
            print("algo salio mal pickling: " + str(e))

    def unpickleArchivoDePuntajes(self):
        try:
            localizacionSaveFile = open(self.archivo,'rb')
            localizacionLoaded = []
            localizacionLoaded = pickle.load(localizacionSaveFile)
            localizacionSaveFile.close()
            return localizacionLoaded
        except EOFError as e:
            print(e)