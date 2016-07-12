import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from media import MovieMedia
from media import TvMedia
from media import MediaFactory

from nameparsers import MovieNameParser
from nameparsers import TvNameParser

MovieExpectedTitle = 'Some Weird Movie'
MovieExpectedYear = 2004

MovieExpectedDir = 'Movies'
MovieExpectedName = 'Some.Weird.Movie_2004'

class MockMovieNameParser(MovieNameParser):
    def parseName(self, rawName):
        return {
            'title': MovieExpectedTitle,
            'year': MovieExpectedYear
        }

    def __init__(self):
        MovieNameParser.__init__(self, None)

class MovieMediaTests(unittest.TestCase):
    def test_cosmetic_dir(self):
        movie = MovieMedia(MovieExpectedTitle, MovieExpectedYear)

        self.assertEqual(movie.getCosmeticDir(), MovieExpectedDir)

    def test_cosmetic_name(self):
        movie = MovieMedia(MovieExpectedTitle, MovieExpectedYear)

        self.assertEqual(movie.getCosmeticName(), MovieExpectedName)

TvExpectedShowTitle = 'Some Weird TV Show'
TvExpectedEpTitle = 'Weird Stuff Happened'
TvExpectedSeasonNumber = 6
TvExpectedEpisodeNumber = 5

TvExpectedDir = 'TV/Some.Weird.TV.Show/Season.6'
TvExpectedName = 'Some.Weird.TV.Show_[06x05]_Weird.Stuff.Happened'

class MockTvNameParser(TvNameParser):
    def parseName(self, rawName):
        return {
            'showTitle': TvExpectedShowTitle,
            'epTitle': TvExpectedEpTitle,
            'season': TvExpectedSeasonNumber,
            'episode': TvExpectedEpisodeNumber
        }

    def __init__(self):
        TvNameParser.__init__(self, None)

class TvMediaTests(unittest.TestCase):
    def test_cosmetic_dir(self):
        tv = TvMedia(TvExpectedShowTitle, TvExpectedEpTitle, TvExpectedSeasonNumber, TvExpectedEpisodeNumber)

        self.assertEqual(tv.getCosmeticDir(), TvExpectedDir)

    def test_cosmetic_name(self):
        tv = TvMedia(TvExpectedShowTitle, TvExpectedEpTitle, TvExpectedSeasonNumber, TvExpectedEpisodeNumber)

        self.assertEqual(tv.getCosmeticName(), TvExpectedName)

class MockTvNameParserFactory:
    def buildFromRawName(self, rawName):
        return MockTvNameParser()

class MockMovieNameParserFactory:
    def buildFromRawName(self, rawName):
        return MockMovieNameParser()

class MediaFactoryTests(unittest.TestCase):
    def test_build_tv(self):
        tv = MediaFactory().buildFromRawName(MockTvNameParserFactory(), '')

        self.assertEqual(tv.getCosmeticDir(), TvExpectedDir)
        self.assertEqual(tv.getCosmeticName(), TvExpectedName)

    def test_build_movie(self):
        movie = MediaFactory().buildFromRawName(MockMovieNameParserFactory(), '')

        self.assertEqual(movie.getCosmeticDir(), MovieExpectedDir)
        self.assertEqual(movie.getCosmeticName(), MovieExpectedName)

