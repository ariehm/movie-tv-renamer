import re
import os
import media

from media import TvMedia
from media import MovieMedia

from nameparsers import NameParserFactory

class File:
	def __init__(self, filePath):
		self.directory = os.path.realpath(filePath)
		self.fileName = os.path.basename(filePath)
		self.fullName = filePath

class MediaFile(File):
	def getCosmeticDir(self):
		return self.media.getCosmeticDir()

	def getCosmeticFileName(self):
		return self.media.getCosmeticName() + self.__extension

	def __init__(self, filePath, media):
		File.__init__(self, filePath)		

		splitName = os.path.splitext(os.path.basename(filePath))

		self.__rawName = splitName[0]
		self.__extension = splitName[1]
		self.media = media

class MediaFileFactory:
	def buildMediaFile(self, filePath, nameParserFactory, mediaFactory):
		rawName = os.path.splitext(os.path.basename(filePath))[0]
		media = mediaFactory.buildFromRawName(nameParserFactory, rawName)
		return MediaFile(filePath, media)

class ReadWriteFile(File):
	def closeFile(self):
		if self.__fileHandle is None:
			return

		self.__fileHandle.close()
		self.__fileHandle = None

	def readLines(self, closeAfter=True):
		if self.__fileHandle is None: 
			self.__fileHandle = open(self.fullName, 'r+')

		ret = self.__fileHandle.readlines()

		if closeAfter: 
			self.__fileHandle.close()
			self.__fileHandle = None

		return ret

	def appendLines(self, linesToWrite, closeAfter=True):
		if self.__fileHandle is None: 
			self.__fileHandle = open(self.fullName, 'a')

		self.__fileHandle.writelines(linesToWrite)

		if closeAfter: 
			self.__fileHandle.close()
			self.__fileHandle = None
		
	def deleteLines(self, lineIndexesToDelete, closeAfter=True):
		if self.__fileHandle is None: 
			self.__fileHandle = open(self.fullName, 'r+')

		self.__fileHandle.seek(0)
		allLines = self.__fileHandle.readlines()
		newLines = []

		index = -1
		for l in allLines:
			index = index + 1
			if any(i == index for i in lineIndexesToDelete):
				continue

			newLines.append(l)

		self.__fileHandle.seek(0)
		self.__fileHandle.truncate(0)
		
		self.__fileHandle.writelines(newLines)

		if closeAfter: 
			self.__fileHandle.close()
			self.__fileHandle = None

	def __init__(self, fullName):
		File.__init__(self, fullName)

		self.__fileHandle = None

class HandledContentFile(ReadWriteFile):
	def pruneNonExistentFilePaths(self):
		handledFilePaths = ReadWriteFile.readLines(self, False)

		index = 0
		lineIndexesToRemove = []

		for i in handledFilePaths:
			if os.path.exists(i.rstrip()) == False:
				lineIndexesToRemove.append(index)
			index = index + 1

		ReadWriteFile.deleteLines(self, lineIndexesToRemove)

	def addHandledFilePath(self, contentFilePath):
		ReadWriteFile.appendLines(self, [contentFilePath + "\n"])

	def getHandledFilePaths(self):
		return [l.rstrip() for l in ReadWriteFile.readLines(self)]

	def __init__(self, filePath):
		ReadWriteFile.__init__(self, filePath)