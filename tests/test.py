import unittest
import os
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from contentfindertests import ContentFinderTests
from nameparsertests import TvNameParserTests
from nameparsertests import MovieNameParserTests
from nameparsertests import NameParserFactoryTests
from mediatests import TvMediaTests
from mediatests import MovieMediaTests
from mediatests import MediaFactoryTests
from mediafiletests import MediaFileTests
from mediafiletests import MediaFileFactoryTests
from renamertests import RenamerTests
from mrcleantests import MrCleanTests

TestCases = (ContentFinderTests,
	TvNameParserTests,
	MovieNameParserTests,
	TvMediaTests,
	MovieMediaTests,
	MediaFileTests,
	RenamerTests,
	MrCleanTests,
	MediaFileFactoryTests,
	MediaFactoryTests,
	NameParserFactoryTests)

def load_tests(loader):
    suite = unittest.TestSuite()
    for t in TestCases:
        tests = loader.loadTestsFromTestCase(t)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
	suite = load_tests(unittest.TestLoader())
	unittest.TextTestRunner(verbosity=2).run(suite)