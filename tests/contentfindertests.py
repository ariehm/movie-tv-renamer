import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from contentfinders import ContentFinder

Extensions = ['.mkv', '.mp4', '.ts']
CompleteDir = 'test-filesystem'

Expected = [
    'Game.Of.Thrones.S06E05.random.descriptor.words.mp4',
    'Game.of.Thrones.S06E01.The.Red.Woman.do.re.mi.fa.so.mkv',
    'subfolder/The.Room.2003.blah.lol.mkv',
    'incomplete/Game.Of.Thrones.S06E03.1080p.blah.blah.ts'
]

class ContentFinderTests(unittest.TestCase):
    def test_no_exclude(self):
        completeFiles = ContentFinder.getCompleteContentFilePaths(CompleteDir, [], Extensions)

        self.assertEqual(len(completeFiles), 4)

        self.assertTrue(any(Expected[0] in f for f in completeFiles))
        self.assertTrue(any(Expected[1] in f for f in completeFiles))
        self.assertTrue(any(Expected[2] in f for f in completeFiles))
        self.assertTrue(any(Expected[3] in f for f in completeFiles))

    def test_exclude_incomplete(self):
        completeFiles = ContentFinder.getCompleteContentFilePaths(CompleteDir, [os.path.join('test-filesystem', 'complete', 'incomplete')], Extensions)

        self.assertEqual(len(completeFiles), 3)

        self.assertTrue(any(Expected[0] in f for f in completeFiles))
        self.assertTrue(any(Expected[1] in f for f in completeFiles))
        self.assertTrue(any(Expected[2] in f for f in completeFiles))
        self.assertFalse(any(Expected[3] in f for f in completeFiles))        



