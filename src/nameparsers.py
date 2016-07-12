import re

from tvdbwrapper import TvdbWrapper
from imdbwrapper import ImdbWrapper

class TvNameParser:
    def parseName(self, rawName):
        # generally: {show title}{SxxExx}{year}{episode title}{descriptors}
        # We only care about the show title and season and episode numbers
        # Everything after SxxExx is ignored

        # Season and Episode number MUST be parsed or we fail

        splitters = ['.', ' ']

        for s in splitters:
            showTitle = []
            epTitle = []
            season = ""
            episode = ""

            for x in rawName.split(s):
                seNumMatch = re.match("^S?(\\d\\d)[Ex](\\d\\d)$", x)
                if seNumMatch:
                    season = seNumMatch.group(1)
                    episode = seNumMatch.group(2)
                    break

                showTitle.append(x)

            if season != "" and episode != "":
                ret = self.__tvdb.getEpisodeInfo(' '.join(showTitle), int(season), int(episode))

                if ret:
                    return ret
            

        return None

    def __init__(self, tvdb):
        self.__tvdb = tvdb

class MovieNameParser:
    def parseName(self, rawName):
        # generally: {title}{year}{descriptors}
        # Assume that year is not optional
        # Assume that the year always splits the title and descriptors

        splitters = ['.', ' ']

        for s in splitters:
            title = []
            potentialYearIndexes = []

            index = 0
            for x in rawName.split(s):
                if re.match("^[19]|[20]\\d\\d\\d$", x):
                    potentialYearIndexes.append({'index': index, 'year': x})
                
                index = index + 1
                title.append(x)

            for y in potentialYearIndexes:
                toSearch = [w for w in title[:y['index']]]
                year = y['year']
                ret = self.__imdb.getMovieInfo(' '.join(toSearch), year)
                if ret:
                    return ret    

        return None

    def __init__(self, imdb):
        self.__imdb = imdb

class NameParserFactory:
    def buildFromRawName(self, rawName):
        # show is tv if we can find SxxExx
        if re.match(".+S?\\d\\d[Ex]\\d\\d.?", rawName):
            return TvNameParser(TvdbWrapper())

        return MovieNameParser(ImdbWrapper())
