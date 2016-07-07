import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from nameparsers import TvNameParser
from nameparsers import MovieNameParser
from nameparsers import NameParserFactory

TvRawNamePeriods = 'Some.Weird.TV.Show.S06E05.1080p.WEBRip.x264.AAC2.0-P2P'
TvRawNameSpaces = 'Some Weird TV Show S06E05 1080p WEBRip x264 AAC2 0-P2P'
TvRawNameAltSeId = 'Some.Weird.TV.Show.06x05.1080p.WEBRip.x264.AAC2.0-P2P'

TvExpectedShowTitle = 'Some Weird TV Show'
TvExpectedEpTitle = 'Weird Stuff Happened'
TvExpectedSeasonNumber = 6
TvExpectedEpisodeNumber = 5

class MockTvdbWrapper:
	def getEpisodeInfo(self, showTitle, seasonNumber, episodeNumber):
		print('showTitle: ' + showTitle)
		print('seasonNumber: ' + str(seasonNumber))
		print('episodeNumber: ' + str(episodeNumber))

		if 'S06E05' in showTitle or '06x05' in showTitle:
			return None

		return {
			'showTitle': showTitle,
			'epTitle': TvExpectedEpTitle,
			'season': seasonNumber,
			'episode': episodeNumber
		}

class TvNameParserTests(unittest.TestCase):
	def setUp(self):
		self.parser = TvNameParser(MockTvdbWrapper())

	def test_raw_name_with_periods(self):
		movieInfo = self.parser.parseName(TvRawNamePeriods)

		self.assertEqual(movieInfo['showTitle'], TvExpectedShowTitle)
		self.assertEqual(movieInfo['epTitle'], TvExpectedEpTitle)
		self.assertEqual(movieInfo['season'], TvExpectedSeasonNumber)
		self.assertEqual(movieInfo['episode'], TvExpectedEpisodeNumber)

	def test_raw_name_with_spaces(self):
		movieInfo = self.parser.parseName(TvRawNameSpaces)

		self.assertEqual(movieInfo['showTitle'], TvExpectedShowTitle)
		self.assertEqual(movieInfo['epTitle'], TvExpectedEpTitle)
		self.assertEqual(movieInfo['season'], TvExpectedSeasonNumber)
		self.assertEqual(movieInfo['episode'], TvExpectedEpisodeNumber)

	def test_raw_name_with_alt_SE_id(self):
		movieInfo = self.parser.parseName(TvRawNameAltSeId)

		self.assertEqual(movieInfo['showTitle'], TvExpectedShowTitle)
		self.assertEqual(movieInfo['epTitle'], TvExpectedEpTitle)
		self.assertEqual(movieInfo['season'], TvExpectedSeasonNumber)
		self.assertEqual(movieInfo['episode'], TvExpectedEpisodeNumber)

MovieRawNamePeriods = 'Some.Weird.Movie.2004'
MovieRawNameSpaces = 'Some Weird Movie 2004'
MovieRawNamePeriodsYearInTitle = '1998.Was.A.Weird.Year.2004'

MovieExpectedTitle = 'Some Weird Movie'
MovieExpectedTitleWithYearInTitle = '1998 Was A Weird Year'
MovieExpectedYear = 2004

class MockImdbWrapper:
	def getMovieInfo(self, title, year):
		print('title: ' + title)
		print('year: ' + year)

		if '2004' != year:
			return None

		return {
			'title': title,
			'year': int(year)
		}

class MovieNameParserTests(unittest.TestCase):
	def setUp(self):
		self.parser = MovieNameParser(MockImdbWrapper())

	def test_raw_name_with_periods(self):
		movieInfo = self.parser.parseName(MovieRawNamePeriods)

		self.assertEqual(movieInfo['title'], MovieExpectedTitle)
		self.assertEqual(movieInfo['year'], MovieExpectedYear)

	def test_raw_name_with_spaces(self):
		movieInfo = self.parser.parseName(MovieRawNameSpaces)

		self.assertEqual(movieInfo['title'], MovieExpectedTitle)
		self.assertEqual(movieInfo['year'], MovieExpectedYear)

	def test_raw_name_with_year_in_title(self):
		movieInfo = self.parser.parseName(MovieRawNamePeriodsYearInTitle)

		self.assertEqual(movieInfo['title'], MovieExpectedTitleWithYearInTitle)
		self.assertEqual(movieInfo['year'], MovieExpectedYear)

class NameParserFactoryTests(unittest.TestCase):
	def test_build_tv_parser_periods(self):
		self.assertTrue(isinstance(NameParserFactory().buildFromRawName(TvRawNamePeriods), TvNameParser))

	def test_build_tv_parser_spaces(self):
		self.assertTrue(isinstance(NameParserFactory().buildFromRawName(TvRawNameSpaces), TvNameParser))

	def test_build_tv_parser_alt_id(self):
		self.assertTrue(isinstance(NameParserFactory().buildFromRawName(TvRawNameAltSeId), TvNameParser))

	def test_build_movie_parser(self):
		self.assertTrue(isinstance(NameParserFactory().buildFromRawName(MovieRawNamePeriods), MovieNameParser))


