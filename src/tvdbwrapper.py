from tvdb_api import Tvdb

class TvdbWrapper:
    def getEpisodeInfo(self, showTitle, seasonNumber, episodeNumber):
        try:
            self.__series = self.__tvdb[' '.join(showTitle)]
            return {
                'showTitle': series['seriesname'],
                'epTitle': series[seasonNumber][episodeNumber]['episodename'],
                'season': seasonNumber,
                'episode': episodeNumber
            }
        except:
            return None

    def __init__(self):
        self.__tvdb = Tvdb()