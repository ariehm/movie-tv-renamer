import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from files import MediaFile
from files import MediaFileFactory
from media import MovieMedia
from media import TvMedia

MovieFilePath = 'a/movie/is/no/one/awesome.movie.2004.mkv'
TvFilePath = 'a/tv/is/awesome.tv.S06E12.mp4'

ExpectedDir = 'TV/awesome.tv/Season.6'
ExpectedName = 'awesome.tv_[06x12]_best.episode.ever.mp4'

class MockMedia:
    def getCosmeticDir(self):
        return ExpectedDir;

    def getCosmeticName(self):
        return ExpectedName

class MediaFileTests(unittest.TestCase):
    def test_cosmetic_dir(self):
        file = MediaFile(MovieFilePath, MockMedia())
        
        self.assertEqual(file.getCosmeticDir(), ExpectedDir)

    def test_cosmetic_file_name(self):
        file = MediaFile(MovieFilePath, MockMedia())
        
        self.assertEqual(file.getCosmeticFileName(), ExpectedName + ".mkv")

FilePath = 'file/path'
MovieTitle = 'test title'
Year = 9999

TvShowTitle = 'test show title'
TvEpTitle = 'test ep title'
Season = 1111
Episode = 2222

class MockMovieMediaFactory:
    def buildFromRawName(self, nameParserFactory, rawName ):
        return MovieMedia(MovieTitle, Year)

class MockTvMediaFactory:
    def buildFromRawName(self, nameParserFactory, rawName ):
        return TvMedia(TvShowTitle, TvEpTitle, Season, Episode)

class MediaFileFactoryTests(unittest.TestCase):
    def test_build_movie_from_raw_name(self):
        file = MediaFileFactory().buildMediaFile(FilePath, None, MockMovieMediaFactory())

        self.assertEqual(file.fullName, FilePath)
        self.assertTrue(isinstance(file.media, MovieMedia))

    def test_build_tv_from_raw_name(self):
        file = MediaFileFactory().buildMediaFile(FilePath, None, MockTvMediaFactory())

        self.assertEqual(file.fullName, FilePath)
        self.assertTrue(isinstance(file.media, TvMedia))
