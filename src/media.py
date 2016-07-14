import os
import logging

from nameparsers import TvNameParser
from nameparsers import MovieNameParser

class Media:
    def __init__(self):
        self._wordSeparator = '.'
        self._categorySeparator = '_'

class MovieMedia(Media):
    def getCosmeticDir(self):
        return "Movies";

    def getCosmeticName(self):
        return self._wordSeparator.join(self.__titleWords) + \
            self._categorySeparator + \
            str(self.year)
        
    def __init__(self, title, year):
        Media.__init__(self)

        self.title = title
        self.__titleWords = title.split(' ')
        self.year = year

class TvMedia(Media):
    def getCosmeticDir(self):
        return os.path.join("TV", 
            self._wordSeparator.join(self.__showTitleWords), 
            "Season" + self._wordSeparator + str(int(self.season)));

    def getCosmeticName(self):
        return self._wordSeparator.join(self.__showTitleWords) + \
            self._categorySeparator + \
            "[" + str(self.season).zfill(2) + "x" + str(self.episode).zfill(2) + "]" + \
            self._categorySeparator + \
            self._wordSeparator.join(self.__epTitleWords)

    def __init__(self, showTitle, epTitle, season, episode):
        Media.__init__(self)

        self.showTitle = showTitle
        self.__showTitleWords = showTitle.split(' ')
        self.epTitle = epTitle
        self.__epTitleWords = epTitle.split(' ')
        self.season = season
        self.episode = episode

class MediaFactory:
    def buildFromRawName(self, nameParserFactory, rawName):
        log = logging.getLogger('root')

        parser = nameParserFactory.buildFromRawName(rawName)
        info = parser.parseName(rawName)

        if info and isinstance(parser, TvNameParser):
            log.info(
                'From {%s}. Found TV {%s-%s: S%sE%s}', 
                rawName,
                info['showTitle'],
                info['epTitle'],
                info['season'],
                info['episode'])

            return TvMedia(
                info['showTitle'], 
                info['epTitle'], 
                info['season'], 
                info['episode'])
        elif info and isinstance(parser, MovieNameParser):
            log.info(
                'From {%s}. Found Movie {%s-%s}', 
                rawName,
                info['title'],
                info['year'])

            return MovieMedia(info['title'], info['year'])

        log.warn('Could not build a media type from {' + rawName + '}')
        return None
        
