import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from renamers import Renamer
from media import MovieMedia
from files import MediaFile

RenameRoot = 'the/rename/root'
FilePath = 'a/movie/is/no/one/awesome.movie.2004.mkv'
ExpectedTitle = 'awesome movie'
ExpectedYear = 2004
ExpectedCosmeticPath = 'Movies/awesome.movie_2004.mkv'
ExpectedRenamePath = os.path.join(RenameRoot, ExpectedCosmeticPath)

class RenamerTests(unittest.TestCase):
	def setUp(self):
		self.renamer = Renamer(RenameRoot)
		self.contentFile = MediaFile(FilePath, MovieMedia(ExpectedTitle, ExpectedYear))

	def test_rename_path(self):
		renamePath = self.renamer.getRenamePath(self.contentFile)
		self.assertEqual(renamePath, ExpectedRenamePath)

