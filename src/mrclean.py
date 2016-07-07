import os
import shutil
import files

class TranmissionCleanCommand:
	def shouldExecute(self, filePathToClean):
		raise NotImplementedError()

	def executeClean(self, filePathToClean):
		raise NotImplementedError()

	def __init__(self, ratioThreshold):
		self.__ratioThreshold = ratioThreshold

class CopyCleanCommand:
	def shouldExecute(self, filePathToClean):
		return True

	def executeClean(self, filePathToClean):
		os.remove(filePathToClean)			

class SymLinkCleanCommand:
	def shouldExecute(self, filePathToClean):
		return True

	def executeClean(self, filePathToClean):
		mediaFile = files.MediaFile(filePathToClean)
		mediaFile.getMediaInfo()

		backupLocation = os.path.join(
			self.__backupRoot, contentFile.getCosmeticDir(), 
			contentFile.getCosmeticFileName())

		shutil.move(filePathToClean, backupLocation)
		os.remove(os.path.splitext(backupLocation)[0])
				
	def __init__(self, backupRoot):
		self.__backupRoot = backupRoot

class MrClean:
	def clean(self, filePathsToClean):
		for filePath in filePathsToClean:
			if all(b.shouldExecute(filePath) for b in self.__cmds):
				for c in self.__cmds:
					c.executeClean(filePath)

	def __init__(self, cleanUpCommands):
		self.__cmds = cleanUpCommands
