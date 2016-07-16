import unittest
import os
import sys

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
from configtests import ConfigTests
from maintests import MainTests

TestCases = (
    ContentFinderTests,
    TvNameParserTests,
    MovieNameParserTests,
    NameParserFactoryTests,
    TvMediaTests,
    MovieMediaTests,
    MediaFileTests,
    MediaFileFactoryTests,
    RenamerTests,
    MrCleanTests,
    MediaFactoryTests,
    ConfigTests,
    MainTests)

def load_tests(loader):
    suite = unittest.TestSuite()
    for t in TestCases:
        tests = loader.loadTestsFromTestCase(t)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    suite = load_tests(unittest.TestLoader())
    unittest.TextTestRunner(verbosity=2).run(suite)
