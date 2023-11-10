from RankingDAO import RankingDAO
class Ranking:
    
    def cargarRankingsPickle():
        rankingDao = RankingDAO()
        puntajesDelRanking = rankingDao.unpickleArchivoDePuntajes()
        return puntajesDelRanking
    
    def guardarRankingPickle(listaDePuntajes):
        rankingDao = RankingDAO()
        rankingDao.pickleArchivoDePuntajes( listaDePuntajes)
        
    def mostrarRanking(self):
        pass