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

        log.info('Send query to IMDB {%s}', query)

        res = requests.get(self.__apiUrl + query).json()

        try:
            # assume the first result is correct.  This will probably come back to bite me
            movie = res['Search'][0]
        except:
            return None

        return {
            'title': movie['Title'],
            'year': movie['Year']
        }

    def __init__(self):
        self.__apiUrl = 'http://www.omdbapi.com/'