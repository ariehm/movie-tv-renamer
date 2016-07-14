import logging

from tvdb_api import Tvdb

class TvdbWrapper:
    def getEpisodeInfo(self, showTitle, seasonNumber, episodeNumber):
        log = logging.getLogger('root')

        try:
            self.__series = self.__tvdb[showTitle]
            return {
                'showTitle': self.__series['seriesname'],
                'epTitle': self.__series[seasonNumber][episodeNumber]['episodename'],
                'season': seasonNumber,
                'episode': episodeNumber
            }

        except Exception as e:
            log.exception(e)
            log.info('Could not find %s on tvdb', showTitle)
            return None

    def __init__(self):
        self.__tvdb = Tvdb()