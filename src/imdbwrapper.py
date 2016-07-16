import requests
import logging

class ImdbWrapper:
    def __getQuery(self, title, year):
        qJoiner = '&'
        queryStart = '?'

        searchQ = 's=' + title.replace(' ', '+')
        typeQ = 'type=movie'
        yearQ = 'y=' + year

        return queryStart + searchQ + qJoiner + typeQ + qJoiner + yearQ

    def getMovieInfo(self, title, year):
        log = logging.getLogger('root')

        query = self.__getQuery(title,year)

        res = requests.get(self.__apiUrl + query).json()

        try:
            # assume the first result is correct.  This will probably come back to bite me
            movie = res['Search'][0]
        except:
            return None

        log.info('Found title {%s} and year {%s}', movie['Title'], movie['Year'])

        return {
            'title': movie['Title'],
            'year': movie['Year']
        }

    def __init__(self):
        self.__apiUrl = 'http://www.omdbapi.com/'
