import os
from files import File

class ContentFinder:
	def getCompleteContentFilePaths(self, excludeDirs, extensions):
		completeFilePaths = []

		for root, subdirs, files in os.walk(self.__completeDir):
			if any(d == root for d in excludeDirs):
				continue
			for file in files:
				completeFilePaths.append(os.path.join(root, file))

		# filter complete files for appropriate extensions
		return [f for f in completeFilePaths if f.endswith(tuple(extensions))]

	def __init__(self, completeDir):
		self.__completeDir = completeDir
