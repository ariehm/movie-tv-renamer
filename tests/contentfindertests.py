import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from contentfinders import ContentFinder

Extensions = ['.mkv', '.mp4', '.ts']
CompleteDir = 'test-filesystem'

Expected = [
	'Game.Of.Thrones.S06E05.1080p.WEBRip.x264.AAC2.0-P2P.mp4',
	'Game.of.Thrones.S06E01.The.Red.Woman.1080p.WEB-DL.DD5.1.H.264-NTb.mkv',
	'subfolder/The.Room.2003.blah.lol.mkv',
	'incomplete/Game.Of.Thrones.S06E03.1080p.WEBRip.x264.AAC2.0-P2P.ts'
]

class ContentFinderTests(unittest.TestCase):
	def setUp(self):
		self.contentFinder = ContentFinder(CompleteDir)

	def test_no_exclude(self):
		completeFiles = self.contentFinder.getCompleteContentFilePaths([], Extensions)

		self.assertEqual(len(completeFiles), 4)

		self.assertTrue(any(Expected[0] in f for f in completeFiles))
		self.assertTrue(any(Expected[1] in f for f in completeFiles))
		self.assertTrue(any(Expected[2] in f for f in completeFiles))
		self.assertTrue(any(Expected[3] in f for f in completeFiles))

	def test_exclude_incomplete(self):
		completeFiles = self.contentFinder.getCompleteContentFilePaths([os.path.join('test-filesystem', 'incomplete')], Extensions)

		self.assertEqual(len(completeFiles), 3)

		self.assertTrue(any(Expected[0] in f for f in completeFiles))
		self.assertTrue(any(Expected[1] in f for f in completeFiles))
		self.assertTrue(any(Expected[2] in f for f in completeFiles))
		self.assertFalse(any(Expected[3] in f for f in completeFiles))		



