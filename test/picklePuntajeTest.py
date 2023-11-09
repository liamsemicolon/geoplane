from unittest import TestCase 
from src.app.Puntaje import Puntaje
from src.dao.RankingDAO import RankingDAO

class picklePuntajeTest(TestCase):
    def test_crearUnaListaVaciaYGuardarlaYLeerlaYAgregarleUnPuntajeNuevoYCompararla():
        archivo = "pickle.tkl"
        listaAntesPickle = []
        listaResultadoEsperado = []
        
        puntaje1 = Puntaje("a",1,2)
        puntaje2 = Puntaje("a",1,2)
        puntaje3 = Puntaje("a",1,2)
        puntaje4 = Puntaje("a",1,2)
        ultimoPuntajeAgregar = Puntaje("a",1,2)
        
        listaAntesPickle.append(puntaje1)
        listaAntesPickle.append(puntaje2)
        listaAntesPickle.append(puntaje3)
        listaAntesPickle.append(puntaje4)
    
        PuntajeDao = RankingDAO()
        PuntajeDao.pickleArchivoDePuntajes(archivo, listaAntesPickle)
        listaDespuesPickle = []
        listaDespuesPickle = PuntajeDao.unpickleArchivoDePuntajes(archivo)
        listaDespuesPickle.append(ultimoPuntajeAgregar)
        
    
        listaResultadoEsperado.append(puntaje1)
        listaResultadoEsperado.append(puntaje2)
        listaResultadoEsperado.append(puntaje3)
        listaResultadoEsperado.append(puntaje4)
        listaResultadoEsperado.append(ultimoPuntajeAgregar)
        
        assert listaDespuesPickle is listaResultadoEsperado
        