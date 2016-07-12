import requests

class ImdbWrapper:
    def __getQuery(self, title, year):
        qJoiner = '&'
        queryStart = '?'

        searchQ = '?s=' + '+'.join(title)
        typeQ = 'type=movie'
        yearQ = 'y=' + year

        return queryStart + searchQ + qJoiner + typeQ + qJoiner + yearQ

    def getMovieInfo(self, title, year):
        res = requests.get(self.__apiUrl + self.__getQuery(title, year)).json()

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